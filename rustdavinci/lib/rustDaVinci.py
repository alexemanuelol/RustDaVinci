#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QSettings, Qt, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QFileDialog, QApplication, QLabel


from pynput import keyboard
from io import BytesIO
from PIL import Image

import urllib.request
import pyautogui
import datetime
import numpy
import time
import cv2
import os

from lib.rustPaletteData import rust_palette
from lib.captureArea import capture_area
from lib.color_functions import hex_to_rgb
from ui.dialogs.captureDialog import CaptureAreaDialog
from ui.settings.default_settings import default_settings


class rustDaVinci():

    def __init__(self, parent):
        """ RustDaVinci class init """
        self.parent = parent
        self.settings = QSettings()
        
        # PIL.Image images original/ quantized
        self.org_img_template = None
        self.org_img = None
        self.quantized_img = None

        # Start painting booleans
        self.org_img_ok = False
        self.image_get_method = 0

        # Use double clicks
        self.use_double_click = False

        # Keyboard interrupt variables
        self.pause_key = None
        self.skip_key = None
        self.abort_key = None
        self.is_paused = False
        self.is_skip_color = False
        self.is_abort = False

        # Pixmaps
        self.pixmap_on_display = 0
        self.org_img_pixmap = None
        self.quantized_img_pixmap_normal = None
        self.quantized_img_pixmap_high = None

        # Painting control tools
        self.ctrl_remove = 0
        self.ctrl_update = 0
        self.ctrl_size = []
        self.ctrl_brush = []
        self.ctrl_opacity = []
        self.ctrl_color = []

        # Canvas coordinates/ ratio
        self.canvas_x = 0
        self.canvas_y = 0
        self.canvas_w = 0
        self.canvas_h = 0

        # Statistics
        self.img_colors = []
        self.tot_pixels = 0
        self.pixels = 0
        self.lines = 0
        self.estimated_time = 0

        # Delays
        self.click_delay = 0
        self.line_delay = 0
        self.ctrl_area_delay = 0
        self.use_double_click = False

        # Hotkey display QLabel
        self.hotkey_label = None


    def update(self):
        """ Updates pyauogui delays, booleans and paint image button"""
        self.click_delay = float(int(self.settings.value("click_delay", default_settings["click_delay"]))/1000)
        self.line_delay = float(int(self.settings.value("line_delay", default_settings["line_delay"]))/1000)
        self.ctrl_area_delay = float(int(self.settings.value("ctrl_area_delay", default_settings["ctrl_area_delay"]))/1000) 
        self.use_double_click = bool(self.settings.value("double_click", default_settings["double_click"]))
        
        # Update the pyautogui delay
        pyautogui.PAUSE = self.click_delay

        if int(self.settings.value("ctrl_w", default_settings["ctrl_w"])) == 0 or int(self.settings.value("ctrl_h", default_settings["ctrl_h"])) == 0:
            self.parent.ui.paint_image_PushButton.setEnabled(False)
        elif self.org_img_ok and int(self.settings.value("ctrl_w", default_settings["ctrl_w"])) != 0 and int(self.settings.value("ctrl_h", default_settings["ctrl_h"])) != 0:
            self.parent.ui.paint_image_PushButton.setEnabled(True)


    def load_image_from_file(self):
        """ Load image from a file """
        title = "Select the image to be painted"
        fileformats = "Images (*.png *.jpg *.jpeg *.gif *.bmp)"
        path = QFileDialog.getOpenFileName(self.parent, title, None, fileformats)[0]

        if path.endswith(('.png', '.jpg', 'jpeg', '.gif', '.bmp')):
            try:
                # Pixmap for original image
                self.org_img_pixmap = QPixmap(path)

                # The original PIL.Image object
                self.org_img_template = Image.open(path).convert("RGBA")
                self.org_img = self.org_img_template

                self.convert_transparency()
                self.create_pixmaps()

                if bool(self.settings.value("show_preview_load", default_settings["show_preview_load"])):
                    if int(self.settings.value("quality", default_settings["quality"])) == 0:
                        self.pixmap_on_display = 1
                    else:
                        self.pixmap_on_display = 2

                    if self.parent.is_expanded:
                        self.parent.label.hide()
                    self.parent.expand_window()
                else:
                    self.pixmap_on_display = 0

            except Exception as e:
                self.org_img = None
                self.org_img_ok = False
                msg = QMessageBox(self.parent)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERROR! Could not load the selected image...")
                msg.setInformativeText(str(e))
                msg.exec_()

        self.update()


    def load_image_from_url(self):
        """ Load image from url """
        dialog = QInputDialog(self.parent)
        dialog.setInputMode(QInputDialog.TextInput)
        dialog.setLabelText("Load image from URL:")
        dialog.resize(500,100)
        ok_clicked = dialog.exec_()
        url = dialog.textValue()

        if ok_clicked and url != "":
            try:
                headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
                request = urllib.request.Request(url, None, headers)
                self.org_img_template = Image.open(urllib.request.urlopen(request)).convert("RGBA")

                # Pixmap for original image
                self.org_img_template.save("temp_url_image.png")
                self.org_img_pixmap = QPixmap("temp_url_image.png", "1")
                os.remove("temp_url_image.png")

                # The original PIL.Image object
                self.org_img = self.org_img_template

                self.convert_transparency()
                self.create_pixmaps()

                if bool(self.settings.value("show_preview_load", default_settings["show_preview_load"])):
                    if int(self.settings.value("quality", default_settings["quality"])) == 0:
                        self.pixmap_on_display = 1
                    else:
                        self.pixmap_on_display = 2

                    if self.parent.is_expanded:
                        self.parent.label.hide()
                    self.parent.expand_window()
                else:
                    self.pixmap_on_display = 0

            except Exception as e:
                self.org_img = None
                self.org_img_ok = False
                msg = QMessageBox(self.parent)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERROR! Could not load the selected image...")
                msg.setInformativeText(str(e))
                msg.exec_()

        self.update()


    def convert_transparency(self):
        """ Paste the org_img on top of an image with background color """
        background_color = rust_palette.index(hex_to_rgb(self.settings.value("background_color", default_settings["background_color"])))
        # Set transparency in image to default background
        try:
            self.org_img = self.org_img_template
            temp_org_img = Image.new("RGBA", self.org_img.size, color=rust_palette[background_color])
            temp_org_img.paste(self.org_img, (0 ,0), mask=self.org_img)
            self.org_img = temp_org_img
            self.org_img = self.org_img.convert("RGB")
        except Exception as e:
            None


    def create_pixmaps(self):
        """ Create quantized pixmaps """
        # Pixmap for quantized image of quality normal
        temp_normal = self.quantize_to_palette(self.org_img, True, 0)
        temp_normal.save("temp_normal.png")
        self.quantized_img_pixmap_normal = QPixmap("temp_normal.png")
        os.remove("temp_normal.png")

        # Pixmap for quantized image of quality high
        temp_high = self.quantize_to_palette(self.org_img, True, 1)
        temp_high.save("temp_high.png")
        self.quantized_img_pixmap_high = QPixmap("temp_high.png")
        os.remove("temp_high.png")

        self.org_img_ok = True


    def convert_img(self):
        """ Convert the image to fit the canvas and quantize the image.
        Updates:    quantized_img,
                    x_correction,
                    y_correction
        Returns:    False, if the image type is invalid.
        """
        org_img_w = self.org_img.size[0]
        org_img_h = self.org_img.size[1]
            
        wpercent = (self.canvas_w / float(org_img_w))
        hpercent = (self.canvas_h / float(org_img_h))
    
        hsize = int((float(org_img_h) * float(wpercent)))
        wsize = int((float(org_img_w) * float(hpercent)))
    
        x_correction = 0
        y_correction = 0
    
        if hsize <= self.canvas_h: 
            resized_img = self.org_img.resize((self.canvas_w, hsize), Image.ANTIALIAS)
            y_correction = int((self.canvas_h - hsize)/2)
        elif wsize <= self.canvas_w: 
            resized_img = self.org_img.resize((wsize, self.canvas_h), Image.ANTIALIAS)
            x_correction = int((self.canvas_w - wsize)/2)
        else: 
            resized_img = self.org_img.resize((self.canvas_w, self.canvas_h), Image.ANTIALIAS)
    
        self.quantized_img = self.quantize_to_palette(resized_img)
        if self.quantized_img == False:
            self.org_img = None
            self.quantized_img = None
            self.org_img_ok = False
            return False

        self.canvas_x += x_correction
        self.canvas_y += y_correction
        self.canvas_w = self.quantized_img.size[0]
        self.canvas_h = self.quantized_img.size[1]
        return True


    def quantize_to_palette(self, image, pixmap = False, pixmap_q = 0):
        """ Convert an RGB, RGBA or L mode image to use a given P image's palette.
        Returns:    The quantized image
        """
        # Select the palette to be used
        palette_data = Image.new("P", (1, 1))
        palette = ()

        # Choose how many colors in the palette
        if bool(self.settings.value("hidden_colors", default_settings["hidden_colors"])):
            if bool(self.settings.value("brush_opacities", default_settings["brush_opacities"])):
                for data in rust_palette:
                    palette = palette + data
            else:
                for i, data in enumerate(rust_palette):
                    if i == 64:
                        palette = palette + (2, 2, 2) * 192
                        break
                    palette = palette + data
        else:
            if bool(self.settings.value("brush_opacities", default_settings["brush_opacities"])):
                for i, data in enumerate(rust_palette):
                    if (i >= 0 and i <= 19) or (i >= 64 and i <= 83) or (i >= 128 and i <= 147) or (i >= 192 and i <= 211):
                        palette = palette + data
                palette = palette + (2, 2, 2) * 176
            else:
                for i, data in enumerate(rust_palette):
                    if i == 20:
                        palette = palette + (2, 2, 2) * 236
                        break
                    palette = palette + data

        palette_data.putpalette(palette)

        palette_data.load()
        self.org_img = image
        self.org_img.load()

        if self.org_img.mode == "RGBA":
            self.org_img = image.convert("RGB")

        if not pixmap:
            quality = int(self.settings.value("quality", default_settings["quality"]))
            if quality == 0:
                im = image.im.convert("P", 0, palette_data.im)
            elif quality == 1:
                im = image.im.convert("P", 1, palette_data.im) # Dithering
        else:
            im = image.im.convert("P", pixmap_q, palette_data.im)
    
        try: return image._new(im)
        except AttributeError: return image._makeself(im)


    def clear_image(self):
        """ Clear the image """
        self.org_img = None
        self.quantized_img = None
        self.org_img_ok = False
        self.update()


    def locate_canvas_area(self):
        """ Locate the coordinates/ ratio of the canvas area.
        Updates:    self.canvas_x,
                    self.canvas_y,
                    self.canvas_w,
                    self.canvas_h
        """
        dialog = CaptureAreaDialog(self.parent, 0)
        ans = dialog.exec_()
        if ans == 0: return False

        self.parent.hide()
        canvas_area = capture_area()
        self.parent.show()

        if canvas_area == False:
            return False
        elif canvas_area[2] == 0 or canvas_area[3] == 0:
            msg = QMessageBox(self.parent)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid coordinates and ratio. Drag & drop the top left corner of the canvas to the bottom right corner.")
            msg.exec_()
            return False

        msg = QMessageBox(self.parent)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Coordinates:\n" + 
                    "X =\t\t" + str(canvas_area[0]) + "\n" +
                    "Y =\t\t" + str(canvas_area[1]) + "\n" +
                    "Width =\t" + str(canvas_area[2]) + "\n" +
                    "Height =\t" + str(canvas_area[3]))
        msg.exec_()

        self.canvas_x = canvas_area[0]
        self.canvas_y = canvas_area[1]
        self.canvas_w = canvas_area[2]
        self.canvas_h = canvas_area[3]
        return True


    def locate_control_area_manually(self):
        """"""
        dialog = CaptureAreaDialog(self.parent, 1)
        ans = dialog.exec_()
        if ans == 0: return False

        self.parent.hide()
        ctrl_area = capture_area()
        self.parent.show()

        if ctrl_area == False:
            self.update()
            return False
        elif ctrl_area[2] == 0 and ctrl_area[3] == 0:
            msg = QMessageBox(self.parent)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid coordinates and ratio. Drag & drop the top left corner of the canvas to the bottom right corner.")
            msg.exec_()
            self.update()
            return False

        btn = QMessageBox.question(self.parent, None,
            "Coordinates:\n" + 
            "X =\t\t" + str(ctrl_area [0]) + "\n" +
            "Y =\t\t" + str(ctrl_area [1]) + "\n" +
            "Width =\t" + str(ctrl_area [2]) + "\n" +
            "Height =\t" + str(ctrl_area [3]) + "\n\n" +
            "Would you like to update the painting controls area coordinates?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if btn == QMessageBox.Yes:
            self.settings.setValue("ctrl_x", str(ctrl_area[0]))
            self.settings.setValue("ctrl_y", str(ctrl_area[1]))
            self.settings.setValue("ctrl_w", str(ctrl_area[2]))
            self.settings.setValue("ctrl_h", str(ctrl_area[3]))

        self.update()


    def locate_control_area_automatically(self):
        """"""
        self.parent.hide()
        ctrl_area = self.locate_control_area_opencv()
        self.parent.show()

        msg = QMessageBox(self.parent)
        if ctrl_area == False:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Couldn't find the painting control area automatically... Please try to manually capture it instead...")
            msg.exec_()
        else:
            btn = QMessageBox.question(self.parent, None,
                "Coordinates:\n" + 
                "X =\t\t" + str(ctrl_area [0]) + "\n" +
                "Y =\t\t" + str(ctrl_area [1]) + "\n" +
                "Width =\t" + str(ctrl_area [2]) + "\n" +
                "Height =\t" + str(ctrl_area [3]) + "\n\n" +
                "Would you like to update the painting controls area coordinates?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if btn == QMessageBox.Yes:
                self.settings.setValue("ctrl_x", str(ctrl_area[0]))
                self.settings.setValue("ctrl_y", str(ctrl_area[1]))
                self.settings.setValue("ctrl_w", str(ctrl_area[2]))
                self.settings.setValue("ctrl_h", str(ctrl_area[3]))
            
            self.update()


    def locate_control_area_opencv(self):
        """ Automatically tries to find the painting control area with opencv.
        Returns:    ctrl_x,
                    ctrl_y,
                    ctrl_w,
                    ctrl_h
                    False, if no control area was found
        """
        screenshot = pyautogui.screenshot()
        screen_w, screen_h = screenshot.size

        image_gray = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_BGR2GRAY)

        tmpl = cv2.imread("opencv_template/rust_palette_template.png", 0)
        tmpl_w, tmpl_h = tmpl.shape[::-1]

        x_coord, y_coord = 0, 0
        threshold = 0.8

        for loop in range(50):
            matches = cv2.matchTemplate(image_gray, tmpl, cv2.TM_CCOEFF_NORMED)
            loc = numpy.where(matches >= threshold)

            x_list, y_list = [], []
            for point in zip(*loc[::-1]):
                x_list.append(point[0])
                y_list.append(point[1])

            if x_list:
                x_coord = int(sum(x_list) / len(x_list))
                y_coord = int(sum(y_list) / len(y_list))
                return x_coord, y_coord, tmpl_w, tmpl_h
    
            tmpl_w, tmpl_h = int(tmpl.shape[1]*1.035), int(tmpl.shape[0]*1.035)
            tmpl = cv2.resize(tmpl, (int(tmpl_w), int(tmpl_h)))

            if tmpl_w > screen_w or tmpl_h > screen_h or loop == 49: return False


    def calc_ctrl_tools_pos(self):
        """ This function calculates the positioning of the different controls in the painting control area.
        The brush size, type and opacity along with all the different colors.
        Updates:    self.ctrl_remove
                    self.ctrl_update
                    self.ctrl_size
                    self.ctrl_brush
                    self.ctrl_opacity
                    self.ctrl_color
        """
        ctrl_x = int(self.settings.value("ctrl_x", default_settings["ctrl_x"]))
        ctrl_y = int(self.settings.value("ctrl_y", default_settings["ctrl_y"]))
        ctrl_w = int(self.settings.value("ctrl_w", default_settings["ctrl_w"]))
        ctrl_h = int(self.settings.value("ctrl_h", default_settings["ctrl_h"]))

        # Calculate the distance between two items on a row of six items (Size)
        first_x_coord_of_six_v1 = ctrl_x + (ctrl_w/6.5454)
        second_x_coord_of_six_v1 = ctrl_x + (ctrl_w/3.4285)
        dist_btwn_x_coords_of_six_v1 = second_x_coord_of_six_v1 - first_x_coord_of_six_v1
    
        # Calculate the distance between two items on a row of six items (Opacity)
        first_x_coord_of_six_v2 = ctrl_x + (ctrl_w/7.5789)
        second_x_coord_of_six_v2 = ctrl_x + (ctrl_w/3.5555)
        dist_btwn_x_coords_of_six_v2 = second_x_coord_of_six_v2 - first_x_coord_of_six_v2
    
        # Calculate the distance between two items on a row of four items (Colors width)
        first_x_coord_of_four = ctrl_x + (ctrl_w/6)
        second_x_coord_of_four = ctrl_x + (ctrl_w/2.5714)
        dist_btwn_x_coords_of_four = second_x_coord_of_four - first_x_coord_of_four
    
        # Calculate the distance between two items on a column of eight items (Colors height)
        first_y_coord_of_eight = ctrl_y + (ctrl_h/2.3220)
        second_y_coord_of_eight = ctrl_y + (ctrl_h/1.9855)
        dist_btwn_y_coords_of_eight = second_y_coord_of_eight - first_y_coord_of_eight
    
        # Set the point location of the remove & update buttons
        self.ctrl_remove = ((ctrl_x + (ctrl_w/2.7692)), (ctrl_y + (ctrl_h/19.5714)))
        self.ctrl_update = ((ctrl_x + (ctrl_w/1.5652)), (ctrl_y + (ctrl_h/19.5714)))
    
    
        for size in range(6):
            self.ctrl_size.append((  first_x_coord_of_six_v1 + 
                                     (size * dist_btwn_x_coords_of_six_v1), 
                                     (ctrl_y + (ctrl_h/6.9661))))
    
        for brush in range(4):
            self.ctrl_brush.append(( first_x_coord_of_four + 
                                     (brush * dist_btwn_x_coords_of_four), 
                                     (ctrl_y + (ctrl_h/4.2371))))
    
        for opacity in range(6):
            self.ctrl_opacity.append((   first_x_coord_of_six_v2 + 
                                         (opacity * dist_btwn_x_coords_of_six_v2), 
                                         (ctrl_y + (ctrl_h/3.0332))))
    
        for row in range(8):
            for column in range(4):
                if (row == 0 or row == 4) and column == 3: continue
                if (row == 1 or row == 5) and (column == 2 or column == 3): continue
                if row == 2 and column == 0: continue
                if row == 3 and (column == 0 or column == 1): continue
                if row == 6 and column == 2: continue
                if row == 7 and (column == 1 or column == 2): continue
                self.ctrl_color.append(  (first_x_coord_of_four + (column * dist_btwn_x_coords_of_four),
                                         (first_y_coord_of_eight + (row * dist_btwn_y_coords_of_eight))))
        
        # Hidden colors location
        if bool(self.settings.value("hidden_colors", default_settings["hidden_colors"])):
            self.ctrl_color.append((ctrl_x + (ctrl_w/18.0000), ctrl_y + (ctrl_h/2.1518)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/4.2353), ctrl_y + (ctrl_h/2.1406)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/13.0909), ctrl_y + (ctrl_h/1.8430)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/3.6923), ctrl_y + (ctrl_h/1.9116)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.8228), ctrl_y + (ctrl_h/1.8853)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.3714), ctrl_y + (ctrl_h/1.8348)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.0746), ctrl_y + (ctrl_h/1.9116)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.0667), ctrl_y + (ctrl_h/1.8430)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.8947), ctrl_y + (ctrl_h/1.6440)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.3333), ctrl_y + (ctrl_h/1.6181)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.2857), ctrl_y + (ctrl_h/1.6440)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.0827), ctrl_y + (ctrl_h/1.6506)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.0588), ctrl_y + (ctrl_h/1.6310)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.0588), ctrl_y + (ctrl_h/1.6118)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.8462), ctrl_y + (ctrl_h/1.4472)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.4545), ctrl_y + (ctrl_h/1.4784)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.3846), ctrl_y + (ctrl_h/1.4838)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.3333), ctrl_y + (ctrl_h/1.4784)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.1803), ctrl_y + (ctrl_h/1.4523)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.1077), ctrl_y + (ctrl_h/1.4421)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.0746), ctrl_y + (ctrl_h/1.4731)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/18.0000), ctrl_y + (ctrl_h/1.4679)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/3.7895), ctrl_y + (ctrl_h/1.4371)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/16.0000), ctrl_y + (ctrl_h/1.3258)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/3.8919), ctrl_y + (ctrl_h/1.3258)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/3.4286), ctrl_y + (ctrl_h/1.3301)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/16.0000), ctrl_y + (ctrl_h/1.2088)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/3.6923), ctrl_y + (ctrl_h/1.2342)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/4.0000), ctrl_y + (ctrl_h/1.2018)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/3.2000), ctrl_y + (ctrl_h/1.1983)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.9200), ctrl_y + (ctrl_h/1.2342)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.4845), ctrl_y + (ctrl_h/1.1844)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.3714), ctrl_y + (ctrl_h/1.1844)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.0746), ctrl_y + (ctrl_h/1.2053)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/16.0000), ctrl_y + (ctrl_h/1.1048)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/4.2353), ctrl_y + (ctrl_h/1.1078)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.3333), ctrl_y + (ctrl_h/1.1078)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.0667), ctrl_y + (ctrl_h/1.1048)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/3.3488), ctrl_y + (ctrl_h/1.0327)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/3.4286), ctrl_y + (ctrl_h/1.0512)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.4694), ctrl_y + (ctrl_h/1.0327)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/2.7692), ctrl_y + (ctrl_h/1.1982)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/2.0571), ctrl_y + (ctrl_h/1.2160)))
            self.ctrl_color.append((ctrl_x + (ctrl_w/1.3211), ctrl_y + (ctrl_h/1.4784)))


    def calc_statistics(self):
        """ Calculate what colors, how many pixels and lines for the painting
        Updates:    self.img_colors, 
                    self.tot_pixels,
                    self.pixels,
                    self.lines
        """
        # Fill the colors_to_skip list
        colors_to_skip = []
        temp_skip_colors = self.settings.value("skip_colors", default_settings["skip_colors"], "QStringList")
        if len(temp_skip_colors) != 0:
            for color in temp_skip_colors:
                colors_to_skip.append(rust_palette.index(hex_to_rgb(color)))

        # Append background color to colors_to_skip
        if bool(self.settings.value("skip_background_color", default_settings["skip_background_color"])):
            background_color = rust_palette.index(hex_to_rgb(self.settings.value("background_color", default_settings["background_color"])))
            colors_to_skip.append(background_color)
        colors_to_skip = list(map(int, colors_to_skip))

        minimum_line_width = int(self.settings.value("minimum_line_width", default_settings["minimum_line_width"]))

        self.img_colors = []
        self.tot_pixels = 0
        self.pixels = 0
        self.lines = 0

        pixel_arr = self.quantized_img.load()


        for color in self.quantized_img.getcolors():
            if color[1] not in colors_to_skip:
                self.tot_pixels += color[0]
                self.img_colors.append(color[1])

        for color in self.img_colors:
            if color in colors_to_skip: continue
    
            is_first_point_of_row = True
            is_last_point_of_row = False
            is_prev_color = False
            is_line = False
            pixels_in_line = 0
    
            for y in range(self.canvas_h):
                is_first_point_of_row = True
                is_last_point_of_row = False
                is_prev_color = False
                is_line = False
                pixels_in_line = 0
    
                for x in range(self.canvas_w):
                    if x == (self.canvas_w - 1): is_last_point_of_row = True
    
                    if is_first_point_of_row:
                        is_first_point_of_row = False
                        if pixel_arr[x, y] == color:
                            is_prev_color = True
                            pixels_in_line = 1
                        continue
    
                    if pixel_arr[x, y] == color:
                        if is_prev_color:
                            if is_last_point_of_row:
                                if pixels_in_line >= minimum_line_width: self.lines += 1
                                else:
                                    self.pixels += (pixels_in_line + 1)
                            else: is_line = True; pixels_in_line += 1
                        else:
                            if is_last_point_of_row: self.pixels += 1
                            else:
                                is_prev_color = True
                                pixels_in_line = 1
                    else:
                        if is_prev_color:
                            if is_line:
                                is_line = False
    
                                if is_last_point_of_row:
                                    if pixels_in_line >= minimum_line_width: self.lines += 1
                                    else: 
                                        self.pixels += (pixels_in_line + 1)
                                    continue
    
                                if pixels_in_line >= minimum_line_width: self.lines += 1
                                else: self.pixels += (pixels_in_line + 1)
                                pixels_in_line = 0
                            else: self.pixels += 1
                            is_prev_color = False
                        else:
                            is_line = False
                            pixels_in_line = 0


    def calc_est_time(self):
        """ Calculate estimated time for the painting process.
        Updates:    Estimated time for clicking and lines
                    Estimated time for only clicking
        """
        one_click_time = self.click_delay + 0.001
        one_click_time = one_click_time*2 if self.use_double_click else one_click_time
        one_line_time = self.line_delay * 5
        change_color_time = len(self.img_colors) * (self.ctrl_area_delay + (2 * self.click_delay))
        other_time = 0.5 + (3 * self.click_delay)
        est_time_lines = int((self.pixels * one_click_time) + (self.lines * one_line_time) + change_color_time + other_time)
        est_time_click = int((self.tot_pixels * one_click_time) + change_color_time + other_time)

        if not bool(self.settings.value("draw_lines", default_settings["draw_lines"])):
            self.prefer_lines = False
            self.estimated_time = est_time_click
        elif est_time_lines < est_time_click:
            self.prefer_lines = True
            self.estimated_time = est_time_lines
        else:
            self.prefer_lines = False
            self.estimated_time = est_time_click

    
    def click_pixel(self, x = 0, y = 0):
        """"""
        if isinstance(x, tuple):
            pyautogui.click(x[0], x[1])
            if self.use_double_click:
                pyautogui.click(x[0], x[1])
        else:
            pyautogui.click(x, y)
            if self.use_double_click:
                pyautogui.click(x, y)


    def draw_line(self, point_A, point_B):
        """ Draws a line between point_A and point_B. """
        pyautogui.PAUSE = self.line_delay
        pyautogui.mouseDown(button="left", x=point_A[0], y=point_A[1])
        pyautogui.keyDown("shift")
        pyautogui.moveTo(point_B[0], point_B[1])
        pyautogui.keyUp("shift")
        pyautogui.mouseUp(button="left")
        pyautogui.PAUSE = self.click_delay


    def key_event(self, key):
        """ Key-press handler. """
        try: key_str = str(key.char)
        except: key_str = str(key.name)

        if key_str == self.pause_key:       # PAUSE
            self.is_paused = not self.is_paused
        elif key_str == self.skip_key:      # SKIP CURRENT COLOR
            self.is_paused = False
            self.is_skip_color = True
        elif key_str == self.abort_key:      # EXIT 
            self.is_paused = False
            self.is_abort = True


    def start_painting(self):
        """ Start the painting """
        # Load settings
        self.update()
        ctrl_x = int(self.settings.value("ctrl_x", default_settings["ctrl_x"]))
        ctrl_y = int(self.settings.value("ctrl_h", default_settings["ctrl_y"]))
        ctrl_w = int(self.settings.value("ctrl_w", default_settings["ctrl_w"]))
        ctrl_h = int(self.settings.value("ctrl_h", default_settings["ctrl_h"]))

        self.pause_key = str(self.settings.value("pause_key", default_settings["pause_key"])).lower()
        self.skip_key = str(self.settings.value("skip_key", default_settings["skip_key"])).lower()
        self.abort_key = str(self.settings.value("abort_key", default_settings["abort_key"])).lower()

        # Fill the colors_to_skip list
        colors_to_skip = []
        temp_skip_colors = self.settings.value("skip_colors", default_settings["skip_colors"], "QStringList")
        if len(temp_skip_colors) != 0:
            for color in temp_skip_colors:
                colors_to_skip.append(rust_palette.index(hex_to_rgb(color)))

        # Append background color to colors_to_skip
        if bool(self.settings.value("skip_background_color", default_settings["skip_background_color"])):
            background_color = rust_palette.index(hex_to_rgb(self.settings.value("background_color", default_settings["background_color"])))
            colors_to_skip.append(background_color)
        colors_to_skip = list(map(int, colors_to_skip))

        minimum_line_width = int(self.settings.value("minimum_line_width", default_settings["minimum_line_width"]))
        update_canvas = bool(self.settings.value("update_canvas", default_settings["update_canvas"]))
        update_canvas_end = bool(self.settings.value("update_canvas_end", default_settings["update_canvas_end"]))
        show_info = bool(self.settings.value("show_information", default_settings["show_information"]))
        hide_preview_paint = bool(self.settings.value("hide_preview_paint", default_settings["hide_preview_paint"]))
        use_hidden_colors = bool(self.settings.value("hidden_colors", default_settings["hidden_colors"]))
        use_brush_opacities = bool(self.settings.value("brush_opacities", default_settings["brush_opacities"]))

        # Boolean reset
        self.is_paused = False
        self.is_skip_color = False
        self.is_abort = False
        
        # Locate canvas, convert image, calculate tools positioning, statistics and estimated time
        if not self.locate_canvas_area(): return
        if not self.convert_img(): return

        # Clear the log
        self.parent.ui.log_TextEdit.clear()
        self.parent.ui.log_TextEdit.append("Calculating statistics...")
        QApplication.processEvents()

        self.calc_ctrl_tools_pos()
        self.calc_statistics()
        self.calc_est_time()

        question = "Dimensions: \t\t\t\t" + str(self.canvas_w) + " x " + str(self.canvas_h)
        question += "\nNumber of colors:\t\t\t" + str(len(self.img_colors))
        question += "\nTotal Number of pixels to paint: \t" + str(self.tot_pixels)
        question += "\nNumber of pixels to paint:\t\t" + str(self.pixels)
        question += "\nNumber of lines:\t\t\t" + str(self.lines)
        question += "\nEst. painting time:\t\t\t" + str(time.strftime("%H:%M:%S", time.gmtime(self.estimated_time)))
        question += "\n\nWould you like to start the painting?"
        if show_info:
            btn = QMessageBox.question(self.parent, None, question, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if btn == QMessageBox.No:
                return

        if bool(self.settings.value("window_topmost", default_settings["window_topmost"])):
            self.parent.setWindowFlags(self.parent.windowFlags() | Qt.WindowStaysOnTopHint)
            self.parent.show()

        if hide_preview_paint and self.parent.is_expanded:
            self.parent.preview_clicked()
        
        self.parent.ui.log_TextEdit.append("Start time:\t" + str((datetime.datetime.now()).time().strftime("%H:%M:%S")))
        self.parent.ui.log_TextEdit.append("Est. time:\t" + str(time.strftime("%H:%M:%S", time.gmtime(self.estimated_time))))
        self.parent.ui.log_TextEdit.append("Est. finished:\t" + str((datetime.datetime.now() + datetime.timedelta(seconds=self.estimated_time)).time().strftime("%H:%M:%S")))
        QApplication.processEvents()

        start_time = time.time()

        # Start keyboard listener
        listener = keyboard.Listener(on_press=self.key_event)
        listener.start()

        self.hotkey_label = QLabel(self.parent)
        self.hotkey_label.setGeometry(QRect(10, 425, 221, 21))
        self.hotkey_label.setText(self.pause_key + " = Pause        " + self.skip_key + " = Skip        " + self.abort_key + " = Abort")
        self.hotkey_label.show()

        pixel_arr = self.quantized_img.load()

        self.click_pixel(self.ctrl_size[0]) # To set focus on the rust window
        time.sleep(.5)
        self.click_pixel(self.ctrl_size[0])
        self.click_pixel(self.ctrl_brush[self.settings.value("brush", default_settings["brush"])])

        pixel_progress = 0
        prev_progress_multiplier = -1
        progress_multiplier = 0
        one_20th = int(self.tot_pixels/20)
        self.parent.ui.progress_ProgressBar.setValue(0)


        color_counter = 0
        for color in self.img_colors:
            self.is_skip_color = False
            self.parent.ui.log_TextEdit.append("(" + str((color_counter+1)) + "/" + str((len(self.img_colors))) + ") Current color: " + str(color))
            QApplication.processEvents()
            color_counter += 1

            if color in colors_to_skip: continue

            first_point = (0, 0)
            is_first_point_of_row = True
            is_last_point_of_row = False
            is_prev_color = False
            is_line = False
            pixels_in_line = 0


            # Choose opacity
            time.sleep(self.ctrl_area_delay)
            if use_hidden_colors:
                if   color >= 0  and color < 64: self.click_pixel(self.ctrl_opacity[5])
                elif color >= 64 and color < 128: self.click_pixel(self.ctrl_opacity[4])
                elif color >= 128 and color < 192: self.click_pixel(self.ctrl_opacity[3])
                elif color >= 192 and color < 256: self.click_pixel(self.ctrl_opacity[2])
            else:
                if   color >= 0  and color < 20: self.click_pixel(self.ctrl_opacity[5])
                elif color >= 20 and color < 40: self.click_pixel(self.ctrl_opacity[4])
                elif color >= 40 and color < 60: self.click_pixel(self.ctrl_opacity[3])
                elif color >= 60 and color < 80: self.click_pixel(self.ctrl_opacity[2])
            time.sleep(self.ctrl_area_delay)

            # Choose color
            if use_hidden_colors:
                self.click_pixel(self.ctrl_color[color%64])
            else:
                self.click_pixel(self.ctrl_color[color%20])
            time.sleep(self.ctrl_area_delay)


            for y in range(self.canvas_h):
                if self.is_skip_color: break

                progress_multiplier = int(pixel_progress/one_20th)
                if progress_multiplier != prev_progress_multiplier:
                    prev_progress_multiplier = progress_multiplier
                    self.parent.ui.progress_ProgressBar.setValue(5 * progress_multiplier)

                is_first_point_of_row = True
                is_last_point_of_row = False
                is_prev_color = False
                is_line = False
                pixels_in_line = 0

                for x in range(self.canvas_w):

                    while self.is_paused: None
                    if self.is_skip_color: break
                    if self.is_abort:
                        listener.stop()
                        elapsed_time = int(time.time() - start_time)
                        self.parent.ui.log_TextEdit.append("Elapsed time: " + str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))
                        self.parent.ui.log_TextEdit.append("Aborted...")
                        QApplication.processEvents()
                        self.hotkey_label.hide()

                        if bool(self.settings.value("window_topmost", default_settings["window_topmost"])):
                            self.parent.setWindowFlags(self.parent.windowFlags() & ~Qt.WindowStaysOnTopHint)
                            self.parent.show()
                        self.parent.activateWindow()
                        return

                    if x == (self.canvas_w - 1):
                        is_last_point_of_row = True

                    if is_first_point_of_row and self.prefer_lines:
                        is_first_point_of_row = False
                        if pixel_arr[x, y] == color:
                            first_point = (self.canvas_x + x, self.canvas_y + y)
                            is_prev_color = True
                            pixels_in_line = 1
                        continue

                    if pixel_arr[x, y] == color:
                        if not self.prefer_lines:
                            self.click_pixel(self.canvas_x + x, self.canvas_y + y)
                            pixel_progress += 1
                            continue
                        if is_prev_color:
                            if is_last_point_of_row:
                                if pixels_in_line >= minimum_line_width:
                                    self.draw_line(first_point, (self.canvas_x + x, self.canvas_y + y))
                                    pixel_progress += pixels_in_line
                                else:
                                    for index in range(pixels_in_line):
                                        self.click_pixel(first_point[0] + index, self.canvas_y + y)
                                    self.click_pixel(self.canvas_x + x, self.canvas_y + y)
                                    pixel_progress += pixels_in_line + 1
                            else:
                                is_line = True
                                pixels_in_line += 1
                        else:
                            if is_last_point_of_row:
                                self.click_pixel(self.canvas_x + x, self.canvas_y + y)
                                pixel_progress += 1
                            else:
                                first_point = (self.canvas_x + x, self.canvas_y + y)
                                is_prev_color = True
                                pixels_in_line = 1
                    else:
                        if not self.prefer_lines: continue
                        if is_prev_color:
                            if is_line:
                                is_line = False
                        
                                if is_last_point_of_row:
                                    if pixels_in_line >= minimum_line_width:
                                        self.draw_line(first_point, (self.canvas_x + (x-1), self.canvas_y + y))
                                        pixel_progress += pixels_in_line
                                    else:
                                        for index in range(pixels_in_line):
                                            self.click_pixel(first_point[0] + index, self.canvas_y + y)
                                        pixel_progress += pixels_in_line
                                    continue
    
                                if pixels_in_line >= minimum_line_width:
                                    self.draw_line(first_point, (self.canvas_x + (x-1), self.canvas_y + y))
                                    pixel_progress += pixels_in_line
                                else:
                                    for index in range(pixels_in_line):
                                        self.click_pixel(first_point[0] + index, self.canvas_y + y)
                                    pixel_progress += pixels_in_line
                                pixels_in_line = 0
    
                            else:
                                self.click_pixel(self.canvas_x + (x-1), self.canvas_y + y)
                                pixel_progress += 1
                            is_prev_color = False
                        else:
                            is_line = False
                            pixels_in_line = 0
    
            if update_canvas:
                self.click_pixel(self.ctrl_update)
    
        if update_canvas_end:
            self.click_pixel(self.ctrl_update)
    
        listener.stop()
        self.parent.ui.progress_ProgressBar.setValue(100)
        elapsed_time = int(time.time() - start_time)

        self.parent.ui.log_TextEdit.append("Elapsed time: " + str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))
        QApplication.processEvents()
        self.hotkey_label.hide()
        
        if bool(self.settings.value("window_topmost", default_settings["window_topmost"])):
            self.parent.setWindowFlags(self.parent.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.parent.show()
        self.parent.activateWindow()

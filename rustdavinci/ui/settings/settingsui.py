# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsUI(object):
    def setupUi(self, SettingsUI):
        SettingsUI.setObjectName("SettingsUI")
        SettingsUI.resize(391, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsUI.sizePolicy().hasHeightForWidth())
        SettingsUI.setSizePolicy(sizePolicy)
        SettingsUI.setMinimumSize(QtCore.QSize(391, 510))
        SettingsUI.setMaximumSize(QtCore.QSize(391, 510))
        self.tabWidget = QtWidgets.QTabWidget(SettingsUI)
        self.tabWidget.setGeometry(QtCore.QRect(6, 9, 381, 461))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.generalTab = QtWidgets.QWidget()
        self.generalTab.setObjectName("generalTab")
        self.line_1 = QtWidgets.QFrame(self.generalTab)
        self.line_1.setGeometry(QtCore.QRect(10, 70, 351, 20))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.quality_ComboBox = QtWidgets.QComboBox(self.generalTab)
        self.quality_ComboBox.setGeometry(QtCore.QRect(180, 40, 171, 22))
        self.quality_ComboBox.setObjectName("quality_ComboBox")
        self.quality_ComboBox.addItem("")
        self.quality_ComboBox.addItem("")
        self.label_1 = QtWidgets.QLabel(self.generalTab)
        self.label_1.setGeometry(QtCore.QRect(20, 40, 161, 21))
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(self.generalTab)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 161, 20))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.generalTab)
        self.label_7.setGeometry(QtCore.QRect(300, 110, 51, 20))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.generalTab)
        self.label_9.setGeometry(QtCore.QRect(300, 150, 51, 20))
        self.label_9.setObjectName("label_9")
        self.ctrl_y_LineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.ctrl_y_LineEdit.setGeometry(QtCore.QRect(180, 110, 101, 20))
        self.ctrl_y_LineEdit.setObjectName("ctrl_y_LineEdit")
        self.clear_coords_PushButton = QtWidgets.QPushButton(self.generalTab)
        self.clear_coords_PushButton.setGeometry(QtCore.QRect(130, 180, 101, 23))
        self.clear_coords_PushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.clear_coords_PushButton.setDefault(False)
        self.clear_coords_PushButton.setObjectName("clear_coords_PushButton")
        self.ctrl_h_LineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.ctrl_h_LineEdit.setGeometry(QtCore.QRect(180, 150, 101, 20))
        self.ctrl_h_LineEdit.setObjectName("ctrl_h_LineEdit")
        self.ctrl_w_LineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.ctrl_w_LineEdit.setGeometry(QtCore.QRect(180, 130, 101, 20))
        self.ctrl_w_LineEdit.setObjectName("ctrl_w_LineEdit")
        self.label_2 = QtWidgets.QLabel(self.generalTab)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 161, 20))
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.generalTab)
        self.label_8.setGeometry(QtCore.QRect(300, 130, 51, 20))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.generalTab)
        self.label_6.setGeometry(QtCore.QRect(300, 90, 51, 20))
        self.label_6.setObjectName("label_6")
        self.ctrl_x_LineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.ctrl_x_LineEdit.setGeometry(QtCore.QRect(180, 90, 101, 20))
        self.ctrl_x_LineEdit.setObjectName("ctrl_x_LineEdit")
        self.label_5 = QtWidgets.QLabel(self.generalTab)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 161, 20))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.generalTab)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 161, 20))
        self.label_3.setObjectName("label_3")
        self.topmost_CheckBox = QtWidgets.QCheckBox(self.generalTab)
        self.topmost_CheckBox.setGeometry(QtCore.QRect(20, 20, 341, 17))
        self.topmost_CheckBox.setChecked(True)
        self.topmost_CheckBox.setObjectName("topmost_CheckBox")
        self.line_7 = QtWidgets.QFrame(self.generalTab)
        self.line_7.setGeometry(QtCore.QRect(10, 200, 351, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.skip_background_CheckBox = QtWidgets.QCheckBox(self.generalTab)
        self.skip_background_CheckBox.setGeometry(QtCore.QRect(20, 230, 341, 17))
        self.skip_background_CheckBox.setChecked(True)
        self.skip_background_CheckBox.setObjectName("skip_background_CheckBox")
        self.label_13 = QtWidgets.QLabel(self.generalTab)
        self.label_13.setGeometry(QtCore.QRect(20, 250, 161, 21))
        self.label_13.setObjectName("label_13")
        self.color_picker_PushButton = QtWidgets.QPushButton(self.generalTab)
        self.color_picker_PushButton.setGeometry(QtCore.QRect(320, 250, 31, 20))
        self.color_picker_PushButton.setObjectName("color_picker_PushButton")
        self.background_LineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.background_LineEdit.setGeometry(QtCore.QRect(180, 250, 131, 20))
        self.background_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.background_LineEdit.setReadOnly(True)
        self.background_LineEdit.setObjectName("background_LineEdit")
        self.skip_colors_ListWidget = QtWidgets.QListWidget(self.generalTab)
        self.skip_colors_ListWidget.setGeometry(QtCore.QRect(20, 310, 241, 111))
        self.skip_colors_ListWidget.setObjectName("skip_colors_ListWidget")
        self.add_skip_color_PushButton = QtWidgets.QPushButton(self.generalTab)
        self.add_skip_color_PushButton.setGeometry(QtCore.QRect(270, 310, 81, 23))
        self.add_skip_color_PushButton.setObjectName("add_skip_color_PushButton")
        self.remove_skip_color_PushButton = QtWidgets.QPushButton(self.generalTab)
        self.remove_skip_color_PushButton.setGeometry(QtCore.QRect(270, 340, 81, 23))
        self.remove_skip_color_PushButton.setObjectName("remove_skip_color_PushButton")
        self.label_48 = QtWidgets.QLabel(self.generalTab)
        self.label_48.setGeometry(QtCore.QRect(20, 290, 331, 21))
        self.label_48.setObjectName("label_48")
        self.show_ctrl_PushButton = QtWidgets.QPushButton(self.generalTab)
        self.show_ctrl_PushButton.setGeometry(QtCore.QRect(240, 180, 101, 23))
        self.show_ctrl_PushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.show_ctrl_PushButton.setDefault(False)
        self.show_ctrl_PushButton.setObjectName("show_ctrl_PushButton")
        self.available_colors_PushButton = QtWidgets.QPushButton(self.generalTab)
        self.available_colors_PushButton.setGeometry(QtCore.QRect(270, 370, 81, 51))
        self.available_colors_PushButton.setObjectName("available_colors_PushButton")
        self.tabWidget.addTab(self.generalTab, "")
        self.paintingTab = QtWidgets.QWidget()
        self.paintingTab.setObjectName("paintingTab")
        self.pause_key_LineEdit = QtWidgets.QLineEdit(self.paintingTab)
        self.pause_key_LineEdit.setGeometry(QtCore.QRect(180, 20, 171, 20))
        self.pause_key_LineEdit.setObjectName("pause_key_LineEdit")
        self.label_10 = QtWidgets.QLabel(self.paintingTab)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.paintingTab)
        self.label_11.setGeometry(QtCore.QRect(20, 50, 161, 21))
        self.label_11.setObjectName("label_11")
        self.skip_key_LineEdit = QtWidgets.QLineEdit(self.paintingTab)
        self.skip_key_LineEdit.setGeometry(QtCore.QRect(180, 50, 171, 20))
        self.skip_key_LineEdit.setObjectName("skip_key_LineEdit")
        self.label_12 = QtWidgets.QLabel(self.paintingTab)
        self.label_12.setGeometry(QtCore.QRect(20, 80, 161, 21))
        self.label_12.setObjectName("label_12")
        self.abort_key_LineEdit = QtWidgets.QLineEdit(self.paintingTab)
        self.abort_key_LineEdit.setGeometry(QtCore.QRect(180, 80, 171, 20))
        self.abort_key_LineEdit.setObjectName("abort_key_LineEdit")
        self.line_2 = QtWidgets.QFrame(self.paintingTab)
        self.line_2.setGeometry(QtCore.QRect(10, 110, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.update_canvas_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.update_canvas_CheckBox.setGeometry(QtCore.QRect(20, 140, 341, 17))
        self.update_canvas_CheckBox.setChecked(True)
        self.update_canvas_CheckBox.setObjectName("update_canvas_CheckBox")
        self.update_canvas_end_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.update_canvas_end_CheckBox.setGeometry(QtCore.QRect(20, 160, 341, 17))
        self.update_canvas_end_CheckBox.setChecked(True)
        self.update_canvas_end_CheckBox.setObjectName("update_canvas_end_CheckBox")
        self.opacities_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.opacities_CheckBox.setGeometry(QtCore.QRect(20, 340, 341, 17))
        self.opacities_CheckBox.setChecked(True)
        self.opacities_CheckBox.setObjectName("opacities_CheckBox")
        self.draw_lines_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.draw_lines_CheckBox.setGeometry(QtCore.QRect(20, 180, 341, 17))
        self.draw_lines_CheckBox.setChecked(True)
        self.draw_lines_CheckBox.setObjectName("draw_lines_CheckBox")
        self.line_4 = QtWidgets.QFrame(self.paintingTab)
        self.line_4.setGeometry(QtCore.QRect(10, 310, 351, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_24 = QtWidgets.QLabel(self.paintingTab)
        self.label_24.setGeometry(QtCore.QRect(40, 370, 321, 41))
        self.label_24.setObjectName("label_24")
        self.hidden_colors_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.hidden_colors_CheckBox.setGeometry(QtCore.QRect(20, 360, 341, 16))
        self.hidden_colors_CheckBox.setObjectName("hidden_colors_CheckBox")
        self.show_info_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.show_info_CheckBox.setGeometry(QtCore.QRect(20, 200, 341, 17))
        self.show_info_CheckBox.setChecked(True)
        self.show_info_CheckBox.setObjectName("show_info_CheckBox")
        self.show_preview_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.show_preview_CheckBox.setGeometry(QtCore.QRect(20, 220, 341, 31))
        self.show_preview_CheckBox.setChecked(True)
        self.show_preview_CheckBox.setObjectName("show_preview_CheckBox")
        self.hide_preview_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.hide_preview_CheckBox.setGeometry(QtCore.QRect(20, 260, 341, 16))
        self.hide_preview_CheckBox.setChecked(True)
        self.hide_preview_CheckBox.setObjectName("hide_preview_CheckBox")
        self.paint_background_CheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.paint_background_CheckBox.setGeometry(QtCore.QRect(20, 280, 341, 16))
        self.paint_background_CheckBox.setObjectName("paint_background_CheckBox")
        self.tabWidget.addTab(self.paintingTab, "")
        self.experimentalTab = QtWidgets.QWidget()
        self.experimentalTab.setObjectName("experimentalTab")
        self.label_15 = QtWidgets.QLabel(self.experimentalTab)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 161, 20))
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(self.experimentalTab)
        self.label_19.setGeometry(QtCore.QRect(280, 20, 81, 20))
        self.label_19.setObjectName("label_19")
        self.click_delay_LineEdit = QtWidgets.QLineEdit(self.experimentalTab)
        self.click_delay_LineEdit.setGeometry(QtCore.QRect(180, 20, 91, 20))
        self.click_delay_LineEdit.setObjectName("click_delay_LineEdit")
        self.label_20 = QtWidgets.QLabel(self.experimentalTab)
        self.label_20.setGeometry(QtCore.QRect(280, 80, 81, 20))
        self.label_20.setObjectName("label_20")
        self.label_16 = QtWidgets.QLabel(self.experimentalTab)
        self.label_16.setGeometry(QtCore.QRect(20, 80, 161, 20))
        self.label_16.setObjectName("label_16")
        self.line_delay_LineEdit = QtWidgets.QLineEdit(self.experimentalTab)
        self.line_delay_LineEdit.setGeometry(QtCore.QRect(180, 80, 91, 20))
        self.line_delay_LineEdit.setObjectName("line_delay_LineEdit")
        self.label_21 = QtWidgets.QLabel(self.experimentalTab)
        self.label_21.setGeometry(QtCore.QRect(280, 50, 81, 20))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.experimentalTab)
        self.label_22.setGeometry(QtCore.QRect(280, 110, 81, 20))
        self.label_22.setObjectName("label_22")
        self.label_17 = QtWidgets.QLabel(self.experimentalTab)
        self.label_17.setGeometry(QtCore.QRect(20, 50, 161, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.experimentalTab)
        self.label_18.setGeometry(QtCore.QRect(20, 110, 161, 20))
        self.label_18.setObjectName("label_18")
        self.min_line_width_LineEdit = QtWidgets.QLineEdit(self.experimentalTab)
        self.min_line_width_LineEdit.setGeometry(QtCore.QRect(180, 110, 91, 20))
        self.min_line_width_LineEdit.setObjectName("min_line_width_LineEdit")
        self.ctrl_delay_LineEdit = QtWidgets.QLineEdit(self.experimentalTab)
        self.ctrl_delay_LineEdit.setGeometry(QtCore.QRect(180, 50, 91, 20))
        self.ctrl_delay_LineEdit.setObjectName("ctrl_delay_LineEdit")
        self.line_5 = QtWidgets.QFrame(self.experimentalTab)
        self.line_5.setGeometry(QtCore.QRect(10, 140, 351, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.brush_type_ComboBox = QtWidgets.QComboBox(self.experimentalTab)
        self.brush_type_ComboBox.setGeometry(QtCore.QRect(180, 170, 141, 22))
        self.brush_type_ComboBox.setObjectName("brush_type_ComboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/brushes/light_round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brush_type_ComboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/brushes/heavy_round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brush_type_ComboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/brushes/medium_round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brush_type_ComboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/brushes/heavy_square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brush_type_ComboBox.addItem(icon3, "")
        self.label_23 = QtWidgets.QLabel(self.experimentalTab)
        self.label_23.setGeometry(QtCore.QRect(20, 170, 161, 21))
        self.label_23.setObjectName("label_23")
        self.line_6 = QtWidgets.QFrame(self.experimentalTab)
        self.line_6.setGeometry(QtCore.QRect(10, 200, 351, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.double_click_CheckBox = QtWidgets.QCheckBox(self.experimentalTab)
        self.double_click_CheckBox.setGeometry(QtCore.QRect(20, 230, 341, 17))
        self.double_click_CheckBox.setObjectName("double_click_CheckBox")
        self.click_color_PushButton = QtWidgets.QPushButton(self.experimentalTab)
        self.click_color_PushButton.setGeometry(QtCore.QRect(220, 390, 141, 31))
        self.click_color_PushButton.setObjectName("click_color_PushButton")
        self.tabWidget.addTab(self.experimentalTab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.gitRepoLinkLabel = QtWidgets.QLabel(self.aboutTab)
        self.gitRepoLinkLabel.setGeometry(QtCore.QRect(20, 340, 221, 16))
        self.gitRepoLinkLabel.setTextFormat(QtCore.Qt.RichText)
        self.gitRepoLinkLabel.setScaledContents(False)
        self.gitRepoLinkLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gitRepoLinkLabel.setOpenExternalLinks(True)
        self.gitRepoLinkLabel.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.gitRepoLinkLabel.setObjectName("gitRepoLinkLabel")
        self.logo1Label = QtWidgets.QLabel(self.aboutTab)
        self.logo1Label.setGeometry(QtCore.QRect(10, 30, 351, 71))
        self.logo1Label.setText("")
        self.logo1Label.setPixmap(QtGui.QPixmap(":/icons/RustDaVinci-logo-2.png"))
        self.logo1Label.setScaledContents(True)
        self.logo1Label.setObjectName("logo1Label")
        self.aboutLabel = QtWidgets.QLabel(self.aboutTab)
        self.aboutLabel.setGeometry(QtCore.QRect(20, 160, 331, 101))
        self.aboutLabel.setWordWrap(True)
        self.aboutLabel.setObjectName("aboutLabel")
        self.versionLabel = QtWidgets.QLabel(self.aboutTab)
        self.versionLabel.setGeometry(QtCore.QRect(20, 110, 161, 20))
        self.versionLabel.setObjectName("versionLabel")
        self.versionLabel_2 = QtWidgets.QLabel(self.aboutTab)
        self.versionLabel_2.setGeometry(QtCore.QRect(20, 130, 161, 20))
        self.versionLabel_2.setObjectName("versionLabel_2")
        self.licenseLabel = QtWidgets.QLabel(self.aboutTab)
        self.licenseLabel.setGeometry(QtCore.QRect(20, 270, 311, 31))
        self.licenseLabel.setWordWrap(True)
        self.licenseLabel.setObjectName("licenseLabel")
        self.line = QtWidgets.QFrame(self.aboutTab)
        self.line.setGeometry(QtCore.QRect(10, 310, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.logo2Label = QtWidgets.QLabel(self.aboutTab)
        self.logo2Label.setGeometry(QtCore.QRect(250, 340, 81, 81))
        self.logo2Label.setText("")
        self.logo2Label.setPixmap(QtGui.QPixmap(":/icons/RustDaVinci-logo-1.png"))
        self.logo2Label.setScaledContents(True)
        self.logo2Label.setObjectName("logo2Label")
        self.faqLinkLabel_2 = QtWidgets.QLabel(self.aboutTab)
        self.faqLinkLabel_2.setGeometry(QtCore.QRect(20, 360, 221, 16))
        self.faqLinkLabel_2.setTextFormat(QtCore.Qt.RichText)
        self.faqLinkLabel_2.setScaledContents(False)
        self.faqLinkLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.faqLinkLabel_2.setOpenExternalLinks(True)
        self.faqLinkLabel_2.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.faqLinkLabel_2.setObjectName("faqLinkLabel_2")
        self.tabWidget.addTab(self.aboutTab, "")
        self.default_PushButton = QtWidgets.QPushButton(SettingsUI)
        self.default_PushButton.setGeometry(QtCore.QRect(10, 480, 75, 23))
        self.default_PushButton.setObjectName("default_PushButton")
        self.ok_PushButton = QtWidgets.QPushButton(SettingsUI)
        self.ok_PushButton.setGeometry(QtCore.QRect(150, 480, 75, 23))
        self.ok_PushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ok_PushButton.setDefault(True)
        self.ok_PushButton.setObjectName("ok_PushButton")
        self.cancel_PushButton = QtWidgets.QPushButton(SettingsUI)
        self.cancel_PushButton.setGeometry(QtCore.QRect(230, 480, 75, 23))
        self.cancel_PushButton.setObjectName("cancel_PushButton")
        self.apply_PushButton = QtWidgets.QPushButton(SettingsUI)
        self.apply_PushButton.setEnabled(False)
        self.apply_PushButton.setGeometry(QtCore.QRect(310, 480, 75, 23))
        self.apply_PushButton.setObjectName("apply_PushButton")

        self.retranslateUi(SettingsUI)
        self.tabWidget.setCurrentIndex(0)
        self.quality_ComboBox.setCurrentIndex(0)
        self.brush_type_ComboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SettingsUI)

    def retranslateUi(self, SettingsUI):
        _translate = QtCore.QCoreApplication.translate
        SettingsUI.setWindowTitle(_translate("SettingsUI", "RustDaVinci Settings"))
        self.quality_ComboBox.setToolTip(_translate("SettingsUI", "The painting quality"))
        self.quality_ComboBox.setCurrentText(_translate("SettingsUI", "Normal"))
        self.quality_ComboBox.setItemText(0, _translate("SettingsUI", "Normal"))
        self.quality_ComboBox.setItemText(1, _translate("SettingsUI", "High"))
        self.label_1.setText(_translate("SettingsUI", "Painting Quality:"))
        self.label_4.setText(_translate("SettingsUI", "Control area width:"))
        self.label_7.setText(_translate("SettingsUI", "(in pixels)"))
        self.label_9.setText(_translate("SettingsUI", "(in pixels)"))
        self.ctrl_y_LineEdit.setToolTip(_translate("SettingsUI", "The y-coordinate for the topleft corner of the painting control area"))
        self.ctrl_y_LineEdit.setText(_translate("SettingsUI", "0"))
        self.clear_coords_PushButton.setToolTip(_translate("SettingsUI", "Clear the painting controls area coordinates & ratio"))
        self.clear_coords_PushButton.setText(_translate("SettingsUI", "Clear Coordinates"))
        self.ctrl_h_LineEdit.setToolTip(_translate("SettingsUI", "The height of the painting control area"))
        self.ctrl_h_LineEdit.setText(_translate("SettingsUI", "0"))
        self.ctrl_w_LineEdit.setToolTip(_translate("SettingsUI", "The width of the painting control area"))
        self.ctrl_w_LineEdit.setText(_translate("SettingsUI", "0"))
        self.label_2.setText(_translate("SettingsUI", "Control area x-coordinate:"))
        self.label_8.setText(_translate("SettingsUI", "(in pixels)"))
        self.label_6.setText(_translate("SettingsUI", "(in pixels)"))
        self.ctrl_x_LineEdit.setToolTip(_translate("SettingsUI", "The x-coordinate for the topleft corner of the painting control area"))
        self.ctrl_x_LineEdit.setText(_translate("SettingsUI", "0"))
        self.label_5.setText(_translate("SettingsUI", "Control area height:"))
        self.label_3.setText(_translate("SettingsUI", "Control area y-coordinate:"))
        self.topmost_CheckBox.setToolTip(_translate("SettingsUI", "This will set RustDaVinci app topmost property to true and will appear above all windows while painting"))
        self.topmost_CheckBox.setText(_translate("SettingsUI", "Set the RustDaVinci window on topmost while painting"))
        self.skip_background_CheckBox.setToolTip(_translate("SettingsUI", "This will ignore painting the set default background color"))
        self.skip_background_CheckBox.setText(_translate("SettingsUI", "Skip painting the default background color"))
        self.label_13.setText(_translate("SettingsUI", "Default background color:"))
        self.color_picker_PushButton.setToolTip(_translate("SettingsUI", "Use the color finder"))
        self.color_picker_PushButton.setText(_translate("SettingsUI", "..."))
        self.background_LineEdit.setToolTip(_translate("SettingsUI", "This is the set default background HEX color"))
        self.background_LineEdit.setText(_translate("SettingsUI", "#ECF0F1"))
        self.skip_colors_ListWidget.setToolTip(_translate("SettingsUI", "A list full of the colors that will be ignored when painting"))
        self.add_skip_color_PushButton.setToolTip(_translate("SettingsUI", "Add colors to the list of colors to ignore when painting"))
        self.add_skip_color_PushButton.setText(_translate("SettingsUI", "Add"))
        self.remove_skip_color_PushButton.setToolTip(_translate("SettingsUI", "Remove selected color from the colors to ignore when painting"))
        self.remove_skip_color_PushButton.setText(_translate("SettingsUI", "Remove"))
        self.label_48.setText(_translate("SettingsUI", "Skip painting these colors:"))
        self.show_ctrl_PushButton.setToolTip(_translate("SettingsUI", "Show where on the screen the painting controls area is located according to the coordinates & ratio"))
        self.show_ctrl_PushButton.setText(_translate("SettingsUI", "Show Controls"))
        self.available_colors_PushButton.setToolTip(_translate("SettingsUI", "Opens a dialog window showing all the possible colors in RustDaVinci"))
        self.available_colors_PushButton.setText(_translate("SettingsUI", "Available\n"
"Colors"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab), _translate("SettingsUI", "General"))
        self.pause_key_LineEdit.setToolTip(_translate("SettingsUI", "This is the hotkey for pausing and resumeing the painting process"))
        self.pause_key_LineEdit.setText(_translate("SettingsUI", "f10"))
        self.label_10.setText(_translate("SettingsUI", "Pause Hotkey:"))
        self.label_11.setText(_translate("SettingsUI", "Skip Color Hotkey:"))
        self.skip_key_LineEdit.setToolTip(_translate("SettingsUI", "This is the hotkey for skipping the current color being painted"))
        self.skip_key_LineEdit.setText(_translate("SettingsUI", "f11"))
        self.label_12.setText(_translate("SettingsUI", "Abort Hotkey:"))
        self.abort_key_LineEdit.setToolTip(_translate("SettingsUI", "This is the hotkey for aborting the painting process"))
        self.abort_key_LineEdit.setText(_translate("SettingsUI", "esc"))
        self.update_canvas_CheckBox.setToolTip(_translate("SettingsUI", "This will automatically update the canvas when switching a color while painting"))
        self.update_canvas_CheckBox.setText(_translate("SettingsUI", "Automatically update the canvas while painting"))
        self.update_canvas_end_CheckBox.setToolTip(_translate("SettingsUI", "This will automatically update the canvas when the painting process is completed"))
        self.update_canvas_end_CheckBox.setText(_translate("SettingsUI", "Automatically save the painting when completed"))
        self.opacities_CheckBox.setToolTip(_translate("SettingsUI", "This will improve paintings by utilizing different brush opacities"))
        self.opacities_CheckBox.setText(_translate("SettingsUI", "Improve paintings by utilizing different brush opacities"))
        self.draw_lines_CheckBox.setToolTip(_translate("SettingsUI", "This causes grouped pixels to be drawn as a line instead of painting each pixel (speeds up painting)"))
        self.draw_lines_CheckBox.setText(_translate("SettingsUI", "Draw lines if calculated to be faster"))
        self.label_24.setText(_translate("SettingsUI", "(Only recommended if 1920x1080 resolution in-game and \n"
"the paint control area is automatically found)"))
        self.hidden_colors_CheckBox.setToolTip(_translate("SettingsUI", "This will improve paintings by utilizing hidden colors (colors hidden between the visible color circles)"))
        self.hidden_colors_CheckBox.setText(_translate("SettingsUI", "Use the hidden color palette"))
        self.show_info_CheckBox.setToolTip(_translate("SettingsUI", "This will display painting information such as colors, total pixels and lines before the painting process starts"))
        self.show_info_CheckBox.setText(_translate("SettingsUI", "Show painting information before starting the painting"))
        self.show_preview_CheckBox.setToolTip(_translate("SettingsUI", "This will automatically show the preview based on the quality setting when loading a new image"))
        self.show_preview_CheckBox.setText(_translate("SettingsUI", "Automatically show painting preview based on the quality setting\n"
"when loading new image"))
        self.hide_preview_CheckBox.setToolTip(_translate("SettingsUI", "This will automatically hide the preview when the painting process starts"))
        self.hide_preview_CheckBox.setText(_translate("SettingsUI", "Automatically hide painting preview before painting starts"))
        self.paint_background_CheckBox.setToolTip(_translate("SettingsUI", "This will automatically paint the background with the set background color before the painting process begins"))
        self.paint_background_CheckBox.setText(_translate("SettingsUI", "Automatically paint the background at start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.paintingTab), _translate("SettingsUI", "Painting"))
        self.label_15.setText(_translate("SettingsUI", "Mouse-click delay:"))
        self.label_19.setText(_translate("SettingsUI", "(in milliseconds)"))
        self.click_delay_LineEdit.setToolTip(_translate("SettingsUI", "This is the delay when releasing the mouse button during a click event. Increasing this improves painting accuracy at the cost of speed."))
        self.click_delay_LineEdit.setText(_translate("SettingsUI", "15"))
        self.label_20.setText(_translate("SettingsUI", "(in milliseconds)"))
        self.label_16.setText(_translate("SettingsUI", "Line-draw delay:"))
        self.line_delay_LineEdit.setToolTip(_translate("SettingsUI", "This is the delay when painting a line. Increasing this improves painting accuracy at the cost of speed."))
        self.line_delay_LineEdit.setText(_translate("SettingsUI", "25"))
        self.label_21.setText(_translate("SettingsUI", "(in milliseconds)"))
        self.label_22.setText(_translate("SettingsUI", "(in pixels)"))
        self.label_17.setText(_translate("SettingsUI", "Control area delay:"))
        self.label_18.setText(_translate("SettingsUI", "Minimum line width:"))
        self.min_line_width_LineEdit.setToolTip(_translate("SettingsUI", "This is the minimum of grouped pixels requred before drawing a line. Changing this may affect the overall painting time."))
        self.min_line_width_LineEdit.setText(_translate("SettingsUI", "10"))
        self.ctrl_delay_LineEdit.setToolTip(_translate("SettingsUI", "This is the delay between the clicks on different painting controls"))
        self.ctrl_delay_LineEdit.setText(_translate("SettingsUI", "150"))
        self.brush_type_ComboBox.setToolTip(_translate("SettingsUI", "The default brush type used for painting"))
        self.brush_type_ComboBox.setCurrentText(_translate("SettingsUI", "Heavy Round"))
        self.brush_type_ComboBox.setItemText(0, _translate("SettingsUI", "Light Round"))
        self.brush_type_ComboBox.setItemText(1, _translate("SettingsUI", "Heavy Round"))
        self.brush_type_ComboBox.setItemText(2, _translate("SettingsUI", "Medium Round"))
        self.brush_type_ComboBox.setItemText(3, _translate("SettingsUI", "Heavy Square"))
        self.label_23.setText(_translate("SettingsUI", "Painting brush type:"))
        self.double_click_CheckBox.setToolTip(_translate("SettingsUI", "This will automatically click the mouse button twice during the painting process eliminating any dead pixels"))
        self.double_click_CheckBox.setText(_translate("SettingsUI", "Double-click the mouse for improved painting accuracy"))
        self.click_color_PushButton.setToolTip(_translate("SettingsUI", "Opens a dialog where you can select a color that the application will click in the in-game palette"))
        self.click_color_PushButton.setText(_translate("SettingsUI", "Click Color"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.experimentalTab), _translate("SettingsUI", "Experimental"))
        self.gitRepoLinkLabel.setToolTip(_translate("SettingsUI", "https://github.com/alexemanuelol/RustDaVinci"))
        self.gitRepoLinkLabel.setText(_translate("SettingsUI", "<html><head/><body><p><a href=\"https://github.com/alexemanuelol/RustDaVinci\"><span style=\" font-weight:600; text-decoration: underline; color:#000000;\">The GitHub Repository</span></a></p></body></html>"))
        self.aboutLabel.setText(_translate("SettingsUI", "RustDaVinci is an automatic sign painter for the game Rust by Facepunch. The application is completely free and open-source. For those who would like to contribute to the application please visit the GitHub page in the link below. For those who just want to use the application as it is, it is strongly recommended to only use the released version of the application to avoid trouble with EAC/ Facepunch. The latest releases can be found on the Github page."))
        self.versionLabel.setText(_translate("SettingsUI", "v0.4.0"))
        self.versionLabel_2.setText(_translate("SettingsUI", "March 6, 2020"))
        self.licenseLabel.setText(_translate("SettingsUI", "RustDaVinci is licensed under GNU GPL3\n"
"Developed by AlexEmanuelol"))
        self.faqLinkLabel_2.setToolTip(_translate("SettingsUI", "https://github.com/alexemanuelol/RustDaVinci/blob/master/docs/FAQ.md"))
        self.faqLinkLabel_2.setText(_translate("SettingsUI", "<html><head/><body><p><a href=\"https://github.com/alexemanuelol/RustDaVinci/blob/master/docs/FAQ.md\"><span style=\" font-weight:600; text-decoration: underline; color:#000000;\">Frequently Asked Questions</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("SettingsUI", "About"))
        self.default_PushButton.setToolTip(_translate("SettingsUI", "Revert all settings to their default value"))
        self.default_PushButton.setText(_translate("SettingsUI", "Defaults"))
        self.ok_PushButton.setText(_translate("SettingsUI", "OK"))
        self.cancel_PushButton.setText(_translate("SettingsUI", "Cancel"))
        self.apply_PushButton.setText(_translate("SettingsUI", "Apply"))
import ui.resources.icons_rc

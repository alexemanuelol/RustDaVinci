# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsUI(object):
    def setupUi(self, SettingsUI):
        SettingsUI.setObjectName("SettingsUI")
        SettingsUI.resize(391, 510)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsUI.sizePolicy().hasHeightForWidth())
        SettingsUI.setSizePolicy(sizePolicy)
        self.tabWidget = QtWidgets.QTabWidget(SettingsUI)
        self.tabWidget.setGeometry(QtCore.QRect(6, 9, 381, 461))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.generalTab = QtWidgets.QWidget()
        self.generalTab.setObjectName("generalTab")
        self.line_1 = QtWidgets.QFrame(self.generalTab)
        self.line_1.setGeometry(QtCore.QRect(10, 50, 351, 20))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.faqLinkLabel = QtWidgets.QLabel(self.generalTab)
        self.faqLinkLabel.setGeometry(QtCore.QRect(160, 390, 181, 21))
        self.faqLinkLabel.setTextFormat(QtCore.Qt.RichText)
        self.faqLinkLabel.setScaledContents(False)
        self.faqLinkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.faqLinkLabel.setOpenExternalLinks(True)
        self.faqLinkLabel.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.faqLinkLabel.setObjectName("faqLinkLabel")
        self.paintingQualityComboBox = QtWidgets.QComboBox(self.generalTab)
        self.paintingQualityComboBox.setGeometry(QtCore.QRect(180, 20, 171, 22))
        self.paintingQualityComboBox.setObjectName("paintingQualityComboBox")
        self.paintingQualityComboBox.addItem("")
        self.paintingQualityComboBox.addItem("")
        self.label_1 = QtWidgets.QLabel(self.generalTab)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(self.generalTab)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 161, 20))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.generalTab)
        self.label_7.setGeometry(QtCore.QRect(300, 140, 51, 20))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.generalTab)
        self.label_9.setGeometry(QtCore.QRect(300, 180, 51, 20))
        self.label_9.setObjectName("label_9")
        self.controlAreaYLineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.controlAreaYLineEdit.setGeometry(QtCore.QRect(180, 140, 101, 20))
        self.controlAreaYLineEdit.setObjectName("controlAreaYLineEdit")
        self.clearCoordinatesPushButton = QtWidgets.QPushButton(self.generalTab)
        self.clearCoordinatesPushButton.setGeometry(QtCore.QRect(180, 200, 101, 23))
        self.clearCoordinatesPushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.clearCoordinatesPushButton.setDefault(True)
        self.clearCoordinatesPushButton.setObjectName("clearCoordinatesPushButton")
        self.controlAreaHeightLineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.controlAreaHeightLineEdit.setGeometry(QtCore.QRect(180, 180, 101, 20))
        self.controlAreaHeightLineEdit.setObjectName("controlAreaHeightLineEdit")
        self.controlAreaWidthLineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.controlAreaWidthLineEdit.setGeometry(QtCore.QRect(180, 160, 101, 20))
        self.controlAreaWidthLineEdit.setObjectName("controlAreaWidthLineEdit")
        self.label_2 = QtWidgets.QLabel(self.generalTab)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 161, 20))
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.generalTab)
        self.label_8.setGeometry(QtCore.QRect(300, 160, 51, 20))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.generalTab)
        self.label_6.setGeometry(QtCore.QRect(300, 120, 51, 20))
        self.label_6.setObjectName("label_6")
        self.rememberControlAreaCoordinatesCheckBox = QtWidgets.QCheckBox(self.generalTab)
        self.rememberControlAreaCoordinatesCheckBox.setEnabled(True)
        self.rememberControlAreaCoordinatesCheckBox.setGeometry(QtCore.QRect(20, 100, 341, 17))
        self.rememberControlAreaCoordinatesCheckBox.setChecked(False)
        self.rememberControlAreaCoordinatesCheckBox.setObjectName("rememberControlAreaCoordinatesCheckBox")
        self.controlAreaXLineEdit = QtWidgets.QLineEdit(self.generalTab)
        self.controlAreaXLineEdit.setGeometry(QtCore.QRect(180, 120, 101, 20))
        self.controlAreaXLineEdit.setObjectName("controlAreaXLineEdit")
        self.label_5 = QtWidgets.QLabel(self.generalTab)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 161, 20))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.generalTab)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 161, 20))
        self.label_3.setObjectName("label_3")
        self.useSavedControlAreaCoordinatesCheckBox = QtWidgets.QCheckBox(self.generalTab)
        self.useSavedControlAreaCoordinatesCheckBox.setGeometry(QtCore.QRect(20, 80, 331, 17))
        self.useSavedControlAreaCoordinatesCheckBox.setChecked(False)
        self.useSavedControlAreaCoordinatesCheckBox.setObjectName("useSavedControlAreaCoordinatesCheckBox")
        self.tabWidget.addTab(self.generalTab, "")
        self.paintingTab = QtWidgets.QWidget()
        self.paintingTab.setObjectName("paintingTab")
        self.pauseKeyLineEdit = QtWidgets.QLineEdit(self.paintingTab)
        self.pauseKeyLineEdit.setGeometry(QtCore.QRect(180, 20, 171, 20))
        self.pauseKeyLineEdit.setObjectName("pauseKeyLineEdit")
        self.label_10 = QtWidgets.QLabel(self.paintingTab)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.paintingTab)
        self.label_11.setGeometry(QtCore.QRect(20, 50, 161, 21))
        self.label_11.setObjectName("label_11")
        self.skipColorKeyLineEdit = QtWidgets.QLineEdit(self.paintingTab)
        self.skipColorKeyLineEdit.setGeometry(QtCore.QRect(180, 50, 171, 20))
        self.skipColorKeyLineEdit.setObjectName("skipColorKeyLineEdit")
        self.label_12 = QtWidgets.QLabel(self.paintingTab)
        self.label_12.setGeometry(QtCore.QRect(20, 80, 161, 21))
        self.label_12.setObjectName("label_12")
        self.cancelKeyLineEdit = QtWidgets.QLineEdit(self.paintingTab)
        self.cancelKeyLineEdit.setGeometry(QtCore.QRect(180, 80, 171, 20))
        self.cancelKeyLineEdit.setObjectName("cancelKeyLineEdit")
        self.line_2 = QtWidgets.QFrame(self.paintingTab)
        self.line_2.setGeometry(QtCore.QRect(10, 110, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.skipDefaultColorCheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.skipDefaultColorCheckBox.setGeometry(QtCore.QRect(20, 200, 341, 17))
        self.skipDefaultColorCheckBox.setChecked(True)
        self.skipDefaultColorCheckBox.setObjectName("skipDefaultColorCheckBox")
        self.autoUpdateCanvasCheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.autoUpdateCanvasCheckBox.setGeometry(QtCore.QRect(20, 260, 341, 17))
        self.autoUpdateCanvasCheckBox.setChecked(True)
        self.autoUpdateCanvasCheckBox.setObjectName("autoUpdateCanvasCheckBox")
        self.autoUpdateCanvasWhenCompletedCheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.autoUpdateCanvasWhenCompletedCheckBox.setGeometry(QtCore.QRect(20, 280, 341, 17))
        self.autoUpdateCanvasWhenCompletedCheckBox.setChecked(True)
        self.autoUpdateCanvasWhenCompletedCheckBox.setObjectName("autoUpdateCanvasWhenCompletedCheckBox")
        self.useBrushOpacitiesCheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.useBrushOpacitiesCheckBox.setGeometry(QtCore.QRect(20, 340, 341, 17))
        self.useBrushOpacitiesCheckBox.setChecked(True)
        self.useBrushOpacitiesCheckBox.setObjectName("useBrushOpacitiesCheckBox")
        self.drawLinesCheckBox = QtWidgets.QCheckBox(self.paintingTab)
        self.drawLinesCheckBox.setGeometry(QtCore.QRect(20, 360, 341, 17))
        self.drawLinesCheckBox.setChecked(True)
        self.drawLinesCheckBox.setObjectName("drawLinesCheckBox")
        self.label_13 = QtWidgets.QLabel(self.paintingTab)
        self.label_13.setGeometry(QtCore.QRect(20, 140, 161, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.paintingTab)
        self.label_14.setGeometry(QtCore.QRect(20, 170, 161, 21))
        self.label_14.setObjectName("label_14")
        self.backgroundColorLineEdit = QtWidgets.QLineEdit(self.paintingTab)
        self.backgroundColorLineEdit.setGeometry(QtCore.QRect(180, 140, 171, 20))
        self.backgroundColorLineEdit.setObjectName("backgroundColorLineEdit")
        self.skipColorsLineEdit = QtWidgets.QLineEdit(self.paintingTab)
        self.skipColorsLineEdit.setGeometry(QtCore.QRect(180, 170, 171, 20))
        self.skipColorsLineEdit.setObjectName("skipColorsLineEdit")
        self.line_3 = QtWidgets.QFrame(self.paintingTab)
        self.line_3.setGeometry(QtCore.QRect(10, 230, 351, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.paintingTab)
        self.line_4.setGeometry(QtCore.QRect(10, 310, 351, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tabWidget.addTab(self.paintingTab, "")
        self.experimentalTab = QtWidgets.QWidget()
        self.experimentalTab.setObjectName("experimentalTab")
        self.label_15 = QtWidgets.QLabel(self.experimentalTab)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 161, 20))
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(self.experimentalTab)
        self.label_19.setGeometry(QtCore.QRect(280, 20, 81, 20))
        self.label_19.setObjectName("label_19")
        self.mouseClickDelayLineEdit = QtWidgets.QLineEdit(self.experimentalTab)
        self.mouseClickDelayLineEdit.setGeometry(QtCore.QRect(180, 20, 91, 20))
        self.mouseClickDelayLineEdit.setObjectName("mouseClickDelayLineEdit")
        self.label_20 = QtWidgets.QLabel(self.experimentalTab)
        self.label_20.setGeometry(QtCore.QRect(280, 40, 81, 20))
        self.label_20.setObjectName("label_20")
        self.label_16 = QtWidgets.QLabel(self.experimentalTab)
        self.label_16.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.label_16.setObjectName("label_16")
        self.lineDrawingDelayLineEdit = QtWidgets.QLineEdit(self.experimentalTab)
        self.lineDrawingDelayLineEdit.setGeometry(QtCore.QRect(180, 40, 91, 20))
        self.lineDrawingDelayLineEdit.setObjectName("lineDrawingDelayLineEdit")
        self.label_21 = QtWidgets.QLabel(self.experimentalTab)
        self.label_21.setGeometry(QtCore.QRect(280, 60, 81, 20))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.experimentalTab)
        self.label_22.setGeometry(QtCore.QRect(280, 80, 81, 20))
        self.label_22.setObjectName("label_22")
        self.label_17 = QtWidgets.QLabel(self.experimentalTab)
        self.label_17.setGeometry(QtCore.QRect(20, 60, 161, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.experimentalTab)
        self.label_18.setGeometry(QtCore.QRect(20, 80, 161, 20))
        self.label_18.setObjectName("label_18")
        self.minimumLineWidthLineEdit = QtWidgets.QLineEdit(self.experimentalTab)
        self.minimumLineWidthLineEdit.setGeometry(QtCore.QRect(180, 80, 91, 20))
        self.minimumLineWidthLineEdit.setObjectName("minimumLineWidthLineEdit")
        self.controlAreaDelayLineEdit = QtWidgets.QLineEdit(self.experimentalTab)
        self.controlAreaDelayLineEdit.setGeometry(QtCore.QRect(180, 60, 91, 20))
        self.controlAreaDelayLineEdit.setObjectName("controlAreaDelayLineEdit")
        self.line_5 = QtWidgets.QFrame(self.experimentalTab)
        self.line_5.setGeometry(QtCore.QRect(10, 110, 351, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.paintingBrushTypeComboBox = QtWidgets.QComboBox(self.experimentalTab)
        self.paintingBrushTypeComboBox.setGeometry(QtCore.QRect(180, 140, 111, 22))
        self.paintingBrushTypeComboBox.setObjectName("paintingBrushTypeComboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/brushes/light_round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paintingBrushTypeComboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/brushes/heavy_round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paintingBrushTypeComboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/brushes/medium_round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paintingBrushTypeComboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/brushes/heavy_square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paintingBrushTypeComboBox.addItem(icon3, "")
        self.label_23 = QtWidgets.QLabel(self.experimentalTab)
        self.label_23.setGeometry(QtCore.QRect(20, 140, 141, 21))
        self.label_23.setObjectName("label_23")
        self.doubleClickCheckBox = QtWidgets.QCheckBox(self.experimentalTab)
        self.doubleClickCheckBox.setGeometry(QtCore.QRect(20, 210, 341, 17))
        self.doubleClickCheckBox.setObjectName("doubleClickCheckBox")
        self.label_24 = QtWidgets.QLabel(self.experimentalTab)
        self.label_24.setGeometry(QtCore.QRect(40, 240, 321, 41))
        self.label_24.setObjectName("label_24")
        self.useHiddenColorsCheckBox = QtWidgets.QCheckBox(self.experimentalTab)
        self.useHiddenColorsCheckBox.setGeometry(QtCore.QRect(20, 230, 341, 16))
        self.useHiddenColorsCheckBox.setObjectName("useHiddenColorsCheckBox")
        self.line_6 = QtWidgets.QFrame(self.experimentalTab)
        self.line_6.setGeometry(QtCore.QRect(10, 180, 351, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.tabWidget.addTab(self.experimentalTab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.gitRepoLinkLabel = QtWidgets.QLabel(self.aboutTab)
        self.gitRepoLinkLabel.setGeometry(QtCore.QRect(10, 330, 351, 51))
        self.gitRepoLinkLabel.setTextFormat(QtCore.Qt.RichText)
        self.gitRepoLinkLabel.setScaledContents(False)
        self.gitRepoLinkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gitRepoLinkLabel.setOpenExternalLinks(True)
        self.gitRepoLinkLabel.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.gitRepoLinkLabel.setObjectName("gitRepoLinkLabel")
        self.tabWidget.addTab(self.aboutTab, "")
        self.defaultPushButton = QtWidgets.QPushButton(SettingsUI)
        self.defaultPushButton.setGeometry(QtCore.QRect(10, 480, 75, 23))
        self.defaultPushButton.setObjectName("defaultPushButton")
        self.okPushButton = QtWidgets.QPushButton(SettingsUI)
        self.okPushButton.setGeometry(QtCore.QRect(150, 480, 75, 23))
        self.okPushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.okPushButton.setDefault(True)
        self.okPushButton.setObjectName("okPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(SettingsUI)
        self.cancelPushButton.setGeometry(QtCore.QRect(230, 480, 75, 23))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.applyPushButton = QtWidgets.QPushButton(SettingsUI)
        self.applyPushButton.setEnabled(False)
        self.applyPushButton.setGeometry(QtCore.QRect(310, 480, 75, 23))
        self.applyPushButton.setObjectName("applyPushButton")

        self.retranslateUi(SettingsUI)
        self.tabWidget.setCurrentIndex(0)
        self.paintingQualityComboBox.setCurrentIndex(1)
        self.paintingBrushTypeComboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SettingsUI)

    def retranslateUi(self, SettingsUI):
        _translate = QtCore.QCoreApplication.translate
        SettingsUI.setWindowTitle(_translate("SettingsUI", "RustDaVinci Settings"))
        self.faqLinkLabel.setText(_translate("SettingsUI", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/alexemanuelol/RustDaVinci/blob/master/docs/FAQ.md\"><span style=\" font-family:\'Arial Black\'; font-weight:600; text-decoration: underline; color:#000000;\">Frequently Asked Questions</span></a></pre></body></html>"))
        self.paintingQualityComboBox.setCurrentText(_translate("SettingsUI", "High"))
        self.paintingQualityComboBox.setItemText(0, _translate("SettingsUI", "Normal"))
        self.paintingQualityComboBox.setItemText(1, _translate("SettingsUI", "High"))
        self.label_1.setText(_translate("SettingsUI", "Painting Quality:"))
        self.label_4.setText(_translate("SettingsUI", "Control area width:"))
        self.label_7.setText(_translate("SettingsUI", "(in pixels)"))
        self.label_9.setText(_translate("SettingsUI", "(in pixels)"))
        self.controlAreaYLineEdit.setText(_translate("SettingsUI", "0"))
        self.clearCoordinatesPushButton.setText(_translate("SettingsUI", "Clear Coordinates"))
        self.controlAreaHeightLineEdit.setText(_translate("SettingsUI", "0"))
        self.controlAreaWidthLineEdit.setText(_translate("SettingsUI", "0"))
        self.label_2.setText(_translate("SettingsUI", "Control area x-coordinate:"))
        self.label_8.setText(_translate("SettingsUI", "(in pixels)"))
        self.label_6.setText(_translate("SettingsUI", "(in pixels)"))
        self.rememberControlAreaCoordinatesCheckBox.setText(_translate("SettingsUI", "Always remember the paint controls area coordinates"))
        self.controlAreaXLineEdit.setText(_translate("SettingsUI", "0"))
        self.label_5.setText(_translate("SettingsUI", "Control area height:"))
        self.label_3.setText(_translate("SettingsUI", "Control area y-coordinate:"))
        self.useSavedControlAreaCoordinatesCheckBox.setText(_translate("SettingsUI", "Always use the saved paint controls area coordinates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab), _translate("SettingsUI", "General"))
        self.pauseKeyLineEdit.setText(_translate("SettingsUI", "F10"))
        self.label_10.setText(_translate("SettingsUI", "Pause Hotkey:"))
        self.label_11.setText(_translate("SettingsUI", "Skip Color Hotkey:"))
        self.skipColorKeyLineEdit.setText(_translate("SettingsUI", "F11"))
        self.label_12.setText(_translate("SettingsUI", "Cancel Hotkey:"))
        self.cancelKeyLineEdit.setText(_translate("SettingsUI", "Escape"))
        self.skipDefaultColorCheckBox.setText(_translate("SettingsUI", "Skip painting the default background color"))
        self.autoUpdateCanvasCheckBox.setText(_translate("SettingsUI", "Automatically update the canvas while painting"))
        self.autoUpdateCanvasWhenCompletedCheckBox.setText(_translate("SettingsUI", "Automatically save the painting when completed"))
        self.useBrushOpacitiesCheckBox.setText(_translate("SettingsUI", "Improve paintings by utilizing different brush opacities"))
        self.drawLinesCheckBox.setText(_translate("SettingsUI", "Draw lines if calculated to be faster"))
        self.label_13.setText(_translate("SettingsUI", "Default background color:"))
        self.label_14.setText(_translate("SettingsUI", "Skip these colors:"))
        self.backgroundColorLineEdit.setText(_translate("SettingsUI", "16"))
        self.skipColorsLineEdit.setText(_translate("SettingsUI", "36, 56, 76"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.paintingTab), _translate("SettingsUI", "Painting"))
        self.label_15.setText(_translate("SettingsUI", "Mouse-click delay:"))
        self.label_19.setText(_translate("SettingsUI", "(in milliseconds)"))
        self.mouseClickDelayLineEdit.setText(_translate("SettingsUI", "5"))
        self.label_20.setText(_translate("SettingsUI", "(in milliseconds)"))
        self.label_16.setText(_translate("SettingsUI", "Line-draw delay:"))
        self.lineDrawingDelayLineEdit.setText(_translate("SettingsUI", "25"))
        self.label_21.setText(_translate("SettingsUI", "(in milliseconds)"))
        self.label_22.setText(_translate("SettingsUI", "(in pixels)"))
        self.label_17.setText(_translate("SettingsUI", "Control area delay:"))
        self.label_18.setText(_translate("SettingsUI", "Minimum line width:"))
        self.minimumLineWidthLineEdit.setText(_translate("SettingsUI", "10"))
        self.controlAreaDelayLineEdit.setText(_translate("SettingsUI", "100"))
        self.paintingBrushTypeComboBox.setCurrentText(_translate("SettingsUI", "Heavy Round"))
        self.paintingBrushTypeComboBox.setItemText(0, _translate("SettingsUI", "Light Round"))
        self.paintingBrushTypeComboBox.setItemText(1, _translate("SettingsUI", "Heavy Round"))
        self.paintingBrushTypeComboBox.setItemText(2, _translate("SettingsUI", "Medium Round"))
        self.paintingBrushTypeComboBox.setItemText(3, _translate("SettingsUI", "Heavy Square"))
        self.label_23.setText(_translate("SettingsUI", "Painting brush type:"))
        self.doubleClickCheckBox.setText(_translate("SettingsUI", "Double-click the mouse for improved painting accuracy"))
        self.label_24.setText(_translate("SettingsUI", "(Only recommended if 1920x1080 resolution in-game and \n"
"automatically find the paint control area coordinates is selected)"))
        self.useHiddenColorsCheckBox.setText(_translate("SettingsUI", "Use the hidden color palette"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.experimentalTab), _translate("SettingsUI", "Experimental"))
        self.gitRepoLinkLabel.setText(_translate("SettingsUI", "<html><head/><body><p><a href=\"https://github.com/alexemanuelol/RustDaVinci\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#000000;\">The GitHub Repository</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("SettingsUI", "About"))
        self.defaultPushButton.setText(_translate("SettingsUI", "Defaults"))
        self.okPushButton.setText(_translate("SettingsUI", "OK"))
        self.cancelPushButton.setText(_translate("SettingsUI", "Cancel"))
        self.applyPushButton.setText(_translate("SettingsUI", "Apply"))
import ui.resources.icons_rc

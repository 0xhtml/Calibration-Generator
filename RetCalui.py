# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\pythonstuff\RetCalui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 667)
        MainWindow.setMinimumSize(QtCore.QSize(810, 667))
        MainWindow.setMaximumSize(QtCore.QSize(810, 667))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.genGcode = QtWidgets.QPushButton(self.centralwidget)
        self.genGcode.setGeometry(QtCore.QRect(30, 560, 251, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.genGcode.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.genGcode.setFont(font)
        self.genGcode.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.genGcode.setObjectName("genGcode")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(323, 0, 657, 831))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setMaximumSize(QtCore.QSize(480, 16777215))
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setLineWidth(1)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setIndent(-1)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_15.setLineWidth(1)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 10, 151, 423))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.nozzleDiameter = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.nozzleDiameter.setObjectName("nozzleDiameter")
        self.verticalLayout_2.addWidget(self.nozzleDiameter)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.layerHeight = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.layerHeight.setObjectName("layerHeight")
        self.verticalLayout_2.addWidget(self.layerHeight)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.filamentDiameter = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.filamentDiameter.setObjectName("filamentDiameter")
        self.verticalLayout_2.addWidget(self.filamentDiameter)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.extrusionMultiplier = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.extrusionMultiplier.setObjectName("extrusionMultiplier")
        self.verticalLayout_2.addWidget(self.extrusionMultiplier)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.speedTravel = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.speedTravel.setObjectName("speedTravel")
        self.verticalLayout_2.addWidget(self.speedTravel)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.customGcode = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.customGcode.setObjectName("customGcode")
        self.verticalLayout_2.addWidget(self.customGcode)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.layersTest = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.layersTest.setObjectName("layersTest")
        self.verticalLayout_2.addWidget(self.layersTest)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.NumTests = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.NumTests.setObjectName("NumTests")
        self.verticalLayout_2.addWidget(self.NumTests)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 137, 536))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.incrementRetractiondistance = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.incrementRetractiondistance.setObjectName("incrementRetractiondistance")
        self.gridLayout.addWidget(self.incrementRetractiondistance, 8, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.printSpeed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.printSpeed.setObjectName("printSpeed")
        self.gridLayout.addWidget(self.printSpeed, 14, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 17, 0, 1, 1)
        self.tempBed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tempBed.setObjectName("tempBed")
        self.gridLayout.addWidget(self.tempBed, 20, 0, 1, 1)
        self.startRetractiondistance = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.startRetractiondistance.setObjectName("startRetractiondistance")
        self.gridLayout.addWidget(self.startRetractiondistance, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.incrementRetractionspeed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.incrementRetractionspeed.setObjectName("incrementRetractionspeed")
        self.gridLayout.addWidget(self.incrementRetractionspeed, 12, 0, 1, 1)
        self.tempStarthotend = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tempStarthotend.setObjectName("tempStarthotend")
        self.gridLayout.addWidget(self.tempStarthotend, 16, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.tempIncrementhotend = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tempIncrementhotend.setObjectName("tempIncrementhotend")
        self.gridLayout.addWidget(self.tempIncrementhotend, 18, 0, 1, 1)
        self.dimensionX = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dimensionX.setToolTipDuration(-1)
        self.dimensionX.setObjectName("dimensionX")
        self.gridLayout.addWidget(self.dimensionX, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 15, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 21, 0, 1, 1)
        self.speedFanIncrement = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.speedFanIncrement.setObjectName("speedFanIncrement")
        self.gridLayout.addWidget(self.speedFanIncrement, 24, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 19, 0, 1, 1)
        self.startRetractionspeed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.startRetractionspeed.setObjectName("startRetractionspeed")
        self.gridLayout.addWidget(self.startRetractionspeed, 10, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 23, 0, 1, 1)
        self.speedFan = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.speedFan.setObjectName("speedFan")
        self.gridLayout.addWidget(self.speedFan, 22, 0, 1, 1)
        self.dimensionY = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dimensionY.setToolTipDuration(-1)
        self.dimensionY.setObjectName("dimensionY")
        self.gridLayout.addWidget(self.dimensionY, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dimensionX, self.dimensionY)
        MainWindow.setTabOrder(self.dimensionY, self.startRetractiondistance)
        MainWindow.setTabOrder(self.startRetractiondistance, self.incrementRetractiondistance)
        MainWindow.setTabOrder(self.incrementRetractiondistance, self.startRetractionspeed)
        MainWindow.setTabOrder(self.startRetractionspeed, self.incrementRetractionspeed)
        MainWindow.setTabOrder(self.incrementRetractionspeed, self.printSpeed)
        MainWindow.setTabOrder(self.printSpeed, self.tempStarthotend)
        MainWindow.setTabOrder(self.tempStarthotend, self.tempIncrementhotend)
        MainWindow.setTabOrder(self.tempIncrementhotend, self.tempBed)
        MainWindow.setTabOrder(self.tempBed, self.speedFan)
        MainWindow.setTabOrder(self.speedFan, self.speedFanIncrement)
        MainWindow.setTabOrder(self.speedFanIncrement, self.nozzleDiameter)
        MainWindow.setTabOrder(self.nozzleDiameter, self.layerHeight)
        MainWindow.setTabOrder(self.layerHeight, self.filamentDiameter)
        MainWindow.setTabOrder(self.filamentDiameter, self.extrusionMultiplier)
        MainWindow.setTabOrder(self.extrusionMultiplier, self.genGcode)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calibration Generator 1.3.1"))
        self.genGcode.setText(_translate("MainWindow", "Generate Gcode"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/Capture.JPG\"/></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Default settings should work with bowden tube. First try with defaults. Then adjust temps fan etc.\n"
"Notes:\n"
"For delta set bed size to 0 for x and y\n"
"For direct drive start with 1 starting retraction and .1 incriment\n"
"For short bowden start with .5 starting retraction and .5 incriment\n"
"To dial in further you can change starting retraction and increments."))
        self.label_15.setText(_translate("MainWindow", "Big Thanks to Qwerer,  Ed, and Gene for your contributions."))
        self.label_16.setText(_translate("MainWindow", "Nozzle Diameter"))
        self.nozzleDiameter.setText(_translate("MainWindow", ".4"))
        self.label_17.setText(_translate("MainWindow", "Layer Height"))
        self.layerHeight.setText(_translate("MainWindow", ".2"))
        self.label_18.setText(_translate("MainWindow", "Filament Diameter"))
        self.filamentDiameter.setText(_translate("MainWindow", "1.75"))
        self.label_19.setText(_translate("MainWindow", "Extrusion Multiplier"))
        self.extrusionMultiplier.setText(_translate("MainWindow", "1"))
        self.label_20.setText(_translate("MainWindow", "Travel Speed"))
        self.speedTravel.setText(_translate("MainWindow", "100"))
        self.label_21.setText(_translate("MainWindow", "Custom Gcode"))
        self.customGcode.setPlainText(_translate("MainWindow", ";Enter auto leveling here"))
        self.label_22.setText(_translate("MainWindow", "Layers per Test"))
        self.layersTest.setText(_translate("MainWindow", "25"))
        self.label_23.setText(_translate("MainWindow", "Number of Tests"))
        self.NumTests.setText(_translate("MainWindow", "15"))
        self.incrementRetractiondistance.setText(_translate("MainWindow", ".5"))
        self.label_3.setText(_translate("MainWindow", "Starting Retraction Distance"))
        self.printSpeed.setText(_translate("MainWindow", "40"))
        self.label_4.setText(_translate("MainWindow", "Increment Retraction"))
        self.label_9.setText(_translate("MainWindow", "Increment Temp"))
        self.tempBed.setText(_translate("MainWindow", "50"))
        self.startRetractiondistance.setText(_translate("MainWindow", ".5"))
        self.label_2.setText(_translate("MainWindow", "y Dimension"))
        self.incrementRetractionspeed.setText(_translate("MainWindow", "10"))
        self.tempStarthotend.setText(_translate("MainWindow", "210"))
        self.label_5.setText(_translate("MainWindow", "Start Retraction Speed"))
        self.tempIncrementhotend.setToolTip(_translate("MainWindow", "Temp increases every 25 layers by this amount. Remember to only test one variable at a time."))
        self.tempIncrementhotend.setText(_translate("MainWindow", "0"))
        self.dimensionX.setToolTip(_translate("MainWindow", "For Delta set bed size 0"))
        self.dimensionX.setText(_translate("MainWindow", "220"))
        self.label_6.setText(_translate("MainWindow", "Retraction Speed Increment"))
        self.label_8.setText(_translate("MainWindow", "Starting Temp"))
        self.label_11.setText(_translate("MainWindow", "Fan Speed %"))
        self.speedFanIncrement.setToolTip(_translate("MainWindow", "Fan speed increases every 25 layers by this amount. Remember to only test one variable at a time."))
        self.speedFanIncrement.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Bed Temp"))
        self.startRetractionspeed.setText(_translate("MainWindow", "10"))
        self.label_7.setText(_translate("MainWindow", "Print Speed"))
        self.label.setText(_translate("MainWindow", "X Dimension"))
        self.label_12.setText(_translate("MainWindow", "Fan Speed Increment"))
        self.speedFan.setText(_translate("MainWindow", "40"))
        self.dimensionY.setToolTip(_translate("MainWindow", "For Delta set bed size 0"))
        self.dimensionY.setText(_translate("MainWindow", "220"))
import RetCalResource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
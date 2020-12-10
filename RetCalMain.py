# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\pythonstuff\retraction.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from RetCalui import Ui_MainWindow
import RetCalGenGcode


ui=None

#Start Raft
#def raft (file,xpos,ypos,ps,eValueresult,lh):
#    return file,xpos,ypos




#Start Gcode
 
def gengcode ():
    global ui
    

    name = QtWidgets.QFileDialog.getSaveFileName(ui.centralwidget, 'Save Gcode', filter="(*.gcode)")
    if len(name[0])>0:
        srd = float(ui.startRetractiondistance.text())
        ird = float(ui.incrementRetractiondistance.text())
        srs = float(ui.startRetractionspeed.text())
        irs = float(ui.incrementRetractionspeed.text())
        tsh = float(ui.tempStarthotend.text())
        tih = float(ui.tempIncrementhotend.text())
        fs = float(ui.speedFan.text())
        fsi = float(ui.speedFanIncrement.text())
        lh = float(ui.layerHeight.text())
        ts = float(ui.speedTravel.text())
        lt = float(ui.layersTest.text())
        nt = float(ui.NumTests.text())
        dx = float(ui.dimensionX.text())
        dy = float(ui.dimensionY.text())
        ps = float(ui.printSpeed.text())
        nd = float(ui.nozzleDiameter.text())
        fd = float(ui.filamentDiameter.text())
        em = float(ui.extrusionMultiplier.text())
        tb = float(ui.tempBed.text())
        sgcode = str(ui.customGcode.toPlainText())
        RetCalGenGcode.genGcode(name[0], srd, ird, srs, irs, tsh, tih, fs, fsi, lh, ts, lt, nt, dx, dy, ps, nd, fd, em, tb, sgcode)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.genGcode.clicked.connect(gengcode)
    MainWindow.show()
    sys.exit(app.exec_())

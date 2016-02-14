# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created: Sun Feb 14 14:25:58 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(848, 675)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow\n"
"{\n"
"background-color: blue;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #555;\n"
"background: rgb(217, 217, 217);\n"
"height: 20px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"background: black;\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"height: 20px;\n"
"font: bold 12pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white;\n"
"background-color: blue;\n"
"border: 1px solid white;\n"
"height: 20px;\n"
"font: bold 10pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:disabled{    \n"
"color: black;\n"
"background-color: white;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: black;\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Date = QtGui.QLabel(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(750, 0, 71, 31))
        self.Date.setObjectName(_fromUtf8("Date"))
        self.BTN_1 = QtGui.QPushButton(self.centralwidget)
        self.BTN_1.setGeometry(QtCore.QRect(623, 50, 201, 16))
        self.BTN_1.setObjectName(_fromUtf8("BTN_1"))
        self.BTN_3 = QtGui.QPushButton(self.centralwidget)
        self.BTN_3.setGeometry(QtCore.QRect(723, 98, 101, 16))
        self.BTN_3.setObjectName(_fromUtf8("BTN_3"))
        self.BTN_2 = QtGui.QPushButton(self.centralwidget)
        self.BTN_2.setGeometry(QtCore.QRect(673, 74, 151, 16))
        self.BTN_2.setObjectName(_fromUtf8("BTN_2"))
        self.TimeTableRoom2 = QtGui.QTableWidget(self.centralwidget)
        self.TimeTableRoom2.setGeometry(QtCore.QRect(50, 150, 751, 451))
        self.TimeTableRoom2.setRowCount(0)
        self.TimeTableRoom2.setColumnCount(5)
        self.TimeTableRoom2.setObjectName(_fromUtf8("TimeTableRoom2"))
        self.TimeTableRoom2.horizontalHeader().setVisible(False)
        self.TimeTableRoom2.horizontalHeader().setCascadingSectionResizes(False)
        self.TimeTableRoom2.horizontalHeader().setDefaultSectionSize(135)
        self.TimeTableRoom2.horizontalHeader().setMinimumSectionSize(15)
        self.imagewidget = ImageWidget(self.centralwidget)
        self.imagewidget.setGeometry(QtCore.QRect(250, 0, 400, 51))
        self.imagewidget.setOrientation(QtCore.Qt.Vertical)
        self.imagewidget.setObjectName(_fromUtf8("imagewidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MKA Aamla Assistant", None))
        self.Date.setText(_translate("MainWindow", "TextLabel", None))
        self.BTN_1.setText(_translate("MainWindow", "1", None))
        self.BTN_3.setText(_translate("MainWindow", "3", None))
        self.BTN_2.setText(_translate("MainWindow", "2", None))

from guiqwt.plot import ImageWidget

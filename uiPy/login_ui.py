# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Login.ui'
#
# Created: Mon Feb 22 18:31:17 2016
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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.setWindowModality(QtCore.Qt.WindowModal)
        Login.resize(176, 122)
        Login.setStyleSheet(_fromUtf8("QDialog\n"
"{\n"
"background-color: rgb(0, 0, 255);\n"
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
        self.gridLayout = QtGui.QGridLayout(Login)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Language_LBL = QtGui.QLabel(Login)
        self.Language_LBL.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Language_LBL.setObjectName(_fromUtf8("Language_LBL"))
        self.gridLayout.addWidget(self.Language_LBL, 0, 0, 1, 1)
        self.Language_CBOX = QtGui.QComboBox(Login)
        self.Language_CBOX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Language_CBOX.setObjectName(_fromUtf8("Language_CBOX"))
        self.Language_CBOX.addItem(_fromUtf8(""))
        self.Language_CBOX.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.Language_CBOX, 0, 1, 1, 1)
        self.Username_LBL = QtGui.QLabel(Login)
        self.Username_LBL.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Username_LBL.setObjectName(_fromUtf8("Username_LBL"))
        self.gridLayout.addWidget(self.Username_LBL, 1, 0, 1, 1)
        self.Username_LINE = QtGui.QLineEdit(Login)
        self.Username_LINE.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Username_LINE.setObjectName(_fromUtf8("Username_LINE"))
        self.gridLayout.addWidget(self.Username_LINE, 1, 1, 1, 1)
        self.Password_LBL = QtGui.QLabel(Login)
        self.Password_LBL.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Password_LBL.setObjectName(_fromUtf8("Password_LBL"))
        self.gridLayout.addWidget(self.Password_LBL, 2, 0, 1, 1)
        self.Password_LINE = QtGui.QLineEdit(Login)
        self.Password_LINE.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Password_LINE.setStyleSheet(_fromUtf8(""))
        self.Password_LINE.setEchoMode(QtGui.QLineEdit.Password)
        self.Password_LINE.setObjectName(_fromUtf8("Password_LINE"))
        self.gridLayout.addWidget(self.Password_LINE, 2, 1, 1, 1)
        self.Login_BTN = QtGui.QPushButton(Login)
        self.Login_BTN.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Login_BTN.setStyleSheet(_fromUtf8(""))
        self.Login_BTN.setObjectName(_fromUtf8("Login_BTN"))
        self.gridLayout.addWidget(self.Login_BTN, 3, 1, 1, 1)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Dialog", None))
        self.Language_LBL.setText(_translate("Login", "Language", None))
        self.Language_CBOX.setItemText(0, _translate("Login", "English", None))
        self.Language_CBOX.setItemText(1, _translate("Login", "German", None))
        self.Username_LBL.setText(_translate("Login", "Username:", None))
        self.Password_LBL.setText(_translate("Login", "Password:", None))
        self.Login_BTN.setText(_translate("Login", "Login", None))


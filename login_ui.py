# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Sun Feb 14 14:25:57 2016
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
        Login.resize(204, 122)
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
        self.layoutWidget = QtGui.QWidget(Login)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 161, 97))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Username = QtGui.QLineEdit(self.layoutWidget)
        self.Username.setObjectName(_fromUtf8("Username"))
        self.gridLayout.addWidget(self.Username, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Password = QtGui.QLineEdit(self.layoutWidget)
        self.Password.setStyleSheet(_fromUtf8(""))
        self.Password.setEchoMode(QtGui.QLineEdit.Password)
        self.Password.setObjectName(_fromUtf8("Password"))
        self.gridLayout.addWidget(self.Password, 1, 1, 1, 1)
        self.LoginBtn = QtGui.QPushButton(self.layoutWidget)
        self.LoginBtn.setStyleSheet(_fromUtf8(""))
        self.LoginBtn.setObjectName(_fromUtf8("LoginBtn"))
        self.gridLayout.addWidget(self.LoginBtn, 2, 1, 1, 1)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Dialog", None))
        self.label.setText(_translate("Login", "Username:", None))
        self.label_2.setText(_translate("Login", "Password:", None))
        self.LoginBtn.setText(_translate("Login", "Login", None))


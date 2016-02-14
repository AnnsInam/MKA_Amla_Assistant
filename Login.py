from PyQt4 import QtCore, QtGui
from login_ui import Ui_Login

class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.Password.setEnabled(False)
        self.ui.LoginBtn.setEnabled(False)

        self.ui.Username.returnPressed.connect(self.VerifyUsername)
        self.ui.Password.returnPressed.connect(self.EnableLoginBtn)
        self.ui.LoginBtn.clicked.connect(self.DoLogin)

    def VerifyUsername(self):
        from QSQL_Retriever import QSQL_Retriever
        Obj = QSQL_Retriever()
        List_of_Usernames = Obj.getUsernames_from_DB()

        if self.ui.Username.text() in List_of_Usernames:
            self.ui.Password.setEnabled(True)
            self.index = List_of_Usernames.index(self.ui.Username.text())
        else:
            self.ui.Password.setEnabled(False)
            self.ui.LoginBtn.setEnabled(False)
            QtGui.QMessageBox.about(self, "Error", "The Username could not be found in our database")


    def EnableLoginBtn(self):
        self.ui.LoginBtn.setEnabled(True)

    def DoLogin(self):
        from QSQL_Retriever import QSQL_Retriever
        Obj = QSQL_Retriever()
        Password = Obj.getPasswords_from_DB(self.index)

        if self.ui.Password.text() in Password:
            print("Login successful")
            self.accept()
        else:
            QtGui.QMessageBox.about(self, "Error", "The Username and Password you entered don't match")
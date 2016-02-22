from PyQt4 import QtGui

from Settings import LoadSettings, WriteSettings
from uiPy.login_ui import Ui_Login

# from QSQL_Retriever import QSQL_Retriever
import Labels

class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.Password_LINE.setEnabled(False)
        self.ui.Login_BTN.setEnabled(False)

        self.ui.Username_LINE.returnPressed.connect(self.VerifyUsername)
        self.ui.Password_LINE.returnPressed.connect(self.EnableLoginBtn)
        self.ui.Login_BTN.clicked.connect(self.DoLogin)

        self.settings = LoadSettings()
        self.langInd = self.settings[0]
        self.ui.Language_CBOX.setCurrentIndex(self.langInd)
        self.SetLanguage()
        self.ui.Language_CBOX.currentIndexChanged.connect(self.SetLanguage)

    def SetLanguage(self):
        self.langInd = self.ui.Language_CBOX.currentIndex()
        print 'Setting Language to ' + self.ui.Language_CBOX.currentText()
        print self.langInd
        self.ui.Language_LBL.setText(Labels.Language[self.langInd])
        self.ui.Username_LBL.setText(Labels.Username[self.langInd])
        self.ui.Password_LBL.setText(Labels.Password[self.langInd])
        self.ui.Login_BTN.setText(Labels.LoginBtn[self.langInd])
        WriteSettings(0, self.ui.Language_CBOX.currentText())

    def VerifyUsername(self):
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
        Obj = QSQL_Retriever()
        Password = Obj.getPasswords_from_DB(self.index)

        if self.ui.Password.text() in Password:
            print("Login successful")
            self.accept()
        else:
            QtGui.QMessageBox.about(self, "Error", "The Username and Password you entered don't match")
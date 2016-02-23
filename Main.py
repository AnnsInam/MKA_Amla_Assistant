import time
import Labels

from PyQt4 import QtCore, QtGui

from Login import Login


class MainGUI(QtGui.QMainWindow):
    send_data = QtCore.pyqtSignal(str)

    def __init__(self, Username, langInd):
        from uiPy.Main_ui import Ui_MainWindow
        QtGui.QMainWindow.__init__(self)
        self.established = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Date.setText(time.strftime("%d/%m/%y"))
        self.Username = Username
        self.ui.Bismillah_LBL.setText(Labels.Bismillah[langInd])

    def Create_Settings(self):
        pass

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()
    # if login.exec_() == QtGui.QDialog.Accepted:
    #     main = MainGUI(login.ui.Username.text(), login.langInd)
    main = MainGUI('AInam', login.langInd)
    main.show()

    sys.exit(app.exec_())


from PyQt4 import QtCore, QtGui
from Login import Login
import time

class MainGUI(QtGui.QMainWindow):
    send_data = QtCore.pyqtSignal(str)

    def __init__(self, Username, langInd):
        from Main_ui import Ui_MainWindow
        QtGui.QMainWindow.__init__(self)
        self.established = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Date.setText(time.strftime("%d/%m/%y"))
        self.Username = Username

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()
    # if login.exec_() == QtGui.QDialog.Accepted:
    #     main = MainGUI(login.ui.Username.text(), login.langInd)
    main = MainGUI('AInam', login.langInd)
    main.show()

    sys.exit(app.exec_())


from PyQt4 import QtCore, QtGui
from Login import Login
import time

class MainGUI(QtGui.QMainWindow):
    send_data = QtCore.pyqtSignal(str)

    def __init__(self, Username):
        from Main_ui import Ui_MainWindow
        QtGui.QMainWindow.__init__(self)
        self.established = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Date.setText(time.strftime("%d/%m/%y"))
        self.Username = Username
        self.Create_TimeTable()
        self.ui.Book_TR.clicked.connect(self.Book_TR)
        self.ui.Update_Tables.clicked.connect(self.Create_TimeTable)

    def Create_TimeTable(self):
        from QSQL_Retriever import QSQL_Retriever
        Obj = QSQL_Retriever()
        Obj.FillTable_from_DB(self.ui.TimeTableRoom1)
        Obj.FillTable_from_DB(self.ui.TimeTableRoom2)
        Obj.FillTable_from_DB(self.ui.TimeTableRoom3)

    def Book_TR(self):
        for item in self.ui.TimeTableRoom1.selectedIndexes():
            self.ui.TimeTableRoom1.setItem(item.row(), item.column(), QtGui.QTableWidgetItem(self.Username))

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtGui.QDialog.Accepted:
        main = MainGUI(login.ui.Username.text())
    # main = MainGUI('MDamon')
    main.show()

    sys.exit(app.exec_())


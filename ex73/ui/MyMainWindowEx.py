from ex73.libs.mymodule import tinh_pt_bac_2
from ex73.ui.MyMainWindow import Ui_MainWindow


class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.calculation)
    def calculation(self):
        a=float(self.heSoALineEdit.text())
        b=float(self.heSoBLineEdit.text())
        c=float(self.heSoCLineEdit.text())
        ketqua= tinh_pt_bac_2(a,b,c)
        self.ketQuaLineEdit.setText(str(ketqua))



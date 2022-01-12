import sys, os
from qt_core import *

from gui.ui_main_window import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.userinterface=UI_MainWindow()
        self.userinterface.setup_ui(self)
        self.show()


if __name__ =="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())
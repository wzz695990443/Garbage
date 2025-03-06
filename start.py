import sys
from win.view import my_DatabaseChose
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_DatabaseChose = my_DatabaseChose()
    my_DatabaseChose.show()
    sys.exit(app.exec())

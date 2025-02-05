import sys
from PySide6.QtWidgets import QApplication, QWidget,QFileDialog,QMessageBox
from PySide6.scripts.project import QMLDIR_FILE

from QTdesign.DatabaseChose import Ui_importFunction
from template.ConfigProcess import ConfigProcess
from template.DBtestconnect import DBtestconnect

class my_DatabaseChose(QWidget, Ui_importFunction):
    def __init__(self):
        super().__init__()
        self.file_type = None
        self.file_path = None
        self.setupUi(self)

        self.pmsChose.addItems(ConfigProcess().get_conn_name("pms"))
        self.memberChose.addItems(ConfigProcess().get_conn_name("member"))
        self.groupChose.addItems(ConfigProcess().get_conn_name("group"))

        self.bind()


    def bind(self):
        self.companyImportrb.clicked.connect(self.companyImportrb_clicked)
        self.checkBt.clicked.connect(self.checkBt_clicked)
        self.choseFile.clicked.connect(self.choseFile_clicked)

    def companyImportrb_clicked(self):
        self.pmsChose.setDisabled(True)
        self.pmsChose.setCurrentText("")
        self.memberChose.setDisabled(True)
        self.memberChose.setCurrentText("")

    def checkBt_clicked(self):
        if self.pmsChose.isEnabled():
            print(self.pmsChose.currentText())
        elif self.memberChose.isEnabled():
            print(self.memberChose.currentText())
        elif self.groupChose.isEnabled():
            print(self.groupChose.currentText())

    def choseFile_clicked(self):
        self.file_path, self.file_type = QFileDialog.getOpenFileName(self, "选取文件", ".", "All Files (*.xlsx);")
        if self.file_path:
            self.filePath.setText(self.file_path)

    def checkBt_clicked(self):
        dt = DBtestconnect()
        flag = False
        if self.pmsChose.isEnabled():
            flag = dt.test_connect(self.pmsChose.currentText())
        if self.memberChose.isEnabled():
            flag = dt.test_connect(self.memberChose.currentText())
        if self.groupChose.isEnabled():
            flag = dt.test_connect(self.groupChose.currentText())
        if flag:
            reply = QMessageBox.information(self, '连接成功', '连接成功')
        else:
            reply = QMessageBox.information(self, '连接失败', '连接失败')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_DatabaseChose = my_DatabaseChose()
    my_DatabaseChose.show()
    sys.exit(app.exec())
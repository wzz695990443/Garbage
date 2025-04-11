import sys
from PySide6.QtWidgets import QApplication, QWidget,QFileDialog,QMessageBox
from PySide6.scripts.project import QMLDIR_FILE

from win.QTdesign.DatabaseChose_ui import Ui_importFunction
from template.ConfigProcess import ConfigProcess
from template.DBtestconnect import DBtestconnect
from win.ExcelTable import ExcelTable

from template.ORM.Connect import Connect
from template.ORM.CompanyBase import CompanyBase, Base
from template.CompanyImport import insert_company_base, insert_company_type

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
        self.editPreview.clicked.connect(self.editPreview_clicked)
        self.import_2.clicked.connect(self.import_2_clicked)

    def companyImportrb_clicked(self):
        # self.pmsChose.setDisabled(True)
        # self.pmsChose.setCurrentText("")
        self.memberChose.setDisabled(True)
        self.memberChose.setCurrentText("")

    def choseFile_clicked(self):
        self.file_path, self.file_type = QFileDialog.getOpenFileName(
            self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)"
        )
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

    def editPreview_clicked(self):
        if self.file_path:
            self.excel_table = ExcelTable()  # 创建 ExcelTable 实例
            self.excel_table.dataframe_ready.connect(
                self.receive_dataframe
            )  # 连接信号和槽
            self.excel_table.load_excel(self.file_path)  # 加载文件
            self.excel_table.show()  # 显示 ExcelTable 窗口
        else:
            QMessageBox.warning(self, "Warning", "No file selected.")

    def receive_dataframe(self, dataframe):
        # 在这里处理接收到的 dataframe
        print("Received dataframe:", dataframe)
        # 你可以在这里将 dataframe 保存到类的属性中，或者进行其他操作
        self.dataframe = dataframe

    def import_2_clicked(self):
        print(self.dataframe)
        try:
            if self.pmsChose.isEnabled() and self.groupChose.isEnabled():
                conn_pms = Connect(**ConfigProcess().get_conn_info(self.pmsChose.currentText()))
                conn_grp = Connect(**ConfigProcess().get_conn_info(self.groupChose.currentText()))
                session_pms = conn_pms.connect()
                session_grp = conn_grp.connect()
                print("Connect Success")

                self.dataframe = self.dataframe.fillna(value="")
                for round in self.dataframe.index:
                    company_id = insert_company_base(
                        self.dataframe, session_grp, round, 2, 9
                    )
                    print(company_id)
                    print(
                        insert_company_base(
                            self.dataframe, session_pms, round, 2, 9, company_id
                        )
                    )
                    print(
                        insert_company_type(
                            self.dataframe, session_grp, round, 2, 9, company_id
                        )
                    )
                    print(
                        insert_company_type(
                            self.dataframe, session_pms, round, 2, 9, company_id
                        )
                    )
                    print(
                        insert_company_type(
                            self.dataframe, session_grp, round, 2, 0, company_id
                        )
                    )
                    print(
                        insert_company_type(
                            self.dataframe, session_pms, round, 2, 0, company_id
                        )
                    )
        except Exception as e:
            print(e)
        finally:    
            session_pms.close()
            session_grp.close()
            conn_pms.close()
            conn_grp.close()
            print("Connect Closed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_DatabaseChose = my_DatabaseChose()
    my_DatabaseChose.show()
    sys.exit(app.exec())

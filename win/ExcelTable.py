import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PySide6.QtCore import Qt

class ExcelTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excel Table Viewer")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)
        
        self.load_button = QPushButton("Load Excel File")
        self.load_button.clicked.connect(self.load_excel)
        self.layout.addWidget(self.load_button)
        
        self.dataframe = None

    def load_excel(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.dataframe = pd.read_excel(file_path)
            self.update_table()

    def update_table(self):
        if self.dataframe is not None:
            self.table_widget.setRowCount(self.dataframe.shape[0])
            self.table_widget.setColumnCount(self.dataframe.shape[1])
            self.table_widget.setHorizontalHeaderLabels(self.dataframe.columns)
            
            for row in range(self.dataframe.shape[0]):
                for col in range(self.dataframe.shape[1]):
                    item = QTableWidgetItem(str(self.dataframe.iat[row, col]))
                    item.setFlags(item.flags() | Qt.ItemIsEditable)
                    self.table_widget.setItem(row, col, item)
                    
            self.table_widget.cellChanged.connect(self.update_dataframe)

    def update_dataframe(self, row, col):
        if self.dataframe is not None:
            new_value = self.table_widget.item(row, col).text()
            self.dataframe.iat[row, col] = new_value

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelTable()
    window.show()
    sys.exit(app.exec_())
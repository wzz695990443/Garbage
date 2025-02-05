import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog, QAbstractItemView
from PySide6.QtCore import Qt, QMimeData, QRect
from PySide6.QtGui import QDrag, QCursor

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
        self.table_widget.setDragEnabled(True)
        self.table_widget.setAcceptDrops(True)
        self.table_widget.setDragDropOverwriteMode(False)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setDropIndicatorShown(True)
        self.table_widget.setDragDropMode(QAbstractItemView.InternalMove)
        self.table_widget.cellChanged.connect(self.update_dataframe)
        self.table_widget.mousePressEvent = self.mouse_press_event
        self.table_widget.mouseMoveEvent = self.mouse_move_event
        self.table_widget.dropEvent = self.drop_event
        self.layout.addWidget(self.table_widget)
        
        self.load_button = QPushButton("Load Excel File")
        self.load_button.clicked.connect(self.load_excel)
        self.layout.addWidget(self.load_button)
        
        self.print_button = QPushButton("Print Excel File")
        self.print_button.clicked.connect(self.print_excel)
        self.layout.addWidget(self.print_button)
        
        self.dataframe = None
        self.dragged_rows = []

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

    def update_dataframe(self, row, col):
        if self.dataframe is not None:
            new_value = self.table_widget.item(row, col).text()
            self.dataframe.iat[row, col] = new_value

    def print_excel(self):
        print(self.dataframe)

    def mouse_press_event(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.position().toPoint()
            self.dragged_rows = [index.row() for index in self.table_widget.selectedIndexes() if index.column() == 0]
        QTableWidget.mousePressEvent(self.table_widget, event)

    def mouse_move_event(self, event):
        if event.buttons() & Qt.LeftButton and (event.position().toPoint() - self.drag_start_position).manhattanLength() > QApplication.startDragDistance():
            if self.dragged_rows:
                drag = QDrag(self.table_widget)
                mime_data = QMimeData()
                mime_data.setText(f"Rows {self.dragged_rows}")
                drag.setMimeData(mime_data)
                drag.exec(Qt.MoveAction)
        QTableWidget.mouseMoveEvent(self.table_widget, event)

    def drop_event(self, event):
        if event.source() == self.table_widget:
            target_row = self.table_widget.rowAt(event.position().y())
            if target_row == -1:
                target_row = self.table_widget.rowCount()
            else:
                # Calculate the middle line of the target row
                target_row_rect = self.table_widget.visualRect(self.table_widget.model().index(target_row, 0))
                target_row_middle = target_row_rect.y() + target_row_rect.height() / 2
                if event.position().y() < target_row_middle:
                    target_row -= 1
            self.move_rows(self.dragged_rows, target_row)
            event.accept()
        else:
            event.ignore()
        QTableWidget.dropEvent(self.table_widget, event)

    def move_rows(self, from_rows, to_row):
        if not from_rows:
            return
        
        # Extract the rows to be moved
        rows_data = [self.dataframe.iloc[row].copy() for row in from_rows]
        
        # Remove the rows from the dataframe
        for row in sorted(from_rows, reverse=True):
            self.dataframe = pd.concat([self.dataframe.iloc[:row], self.dataframe.iloc[row+1:]], ignore_index=True)
        
        # Insert the rows at the target position
        for i, row_data in enumerate(rows_data):
            self.dataframe = pd.concat([self.dataframe.iloc[:to_row + i], pd.DataFrame([row_data]), self.dataframe.iloc[to_row + i:]], ignore_index=True)
        
        self.update_table()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelTable()
    window.show()
    sys.exit(app.exec())
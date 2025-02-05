import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog, QAbstractItemView, QMessageBox
from PySide6.QtCore import Qt, QMimeData, QRect
from PySide6.QtGui import QDrag, QCursor
import template.tool as tool

class ExcelTable(QMainWindow):
    def __init__(self):
        """初始化主窗口"""
        super().__init__()
        self.setWindowTitle("Excel Table Viewer")  # 设置窗口标题
        self.setGeometry(100, 100, 800, 600)  # 设置窗口初始位置和大小
        
        self.central_widget = QWidget()  # 创建中心部件
        self.setCentralWidget(self.central_widget)  # 将中心部件设置为主窗口的中央部件
        
        self.layout = QVBoxLayout()  # 创建垂直布局
        self.central_widget.setLayout(self.layout)  # 将布局设置为中心部件的布局
        
        self.table_widget = QTableWidget()  # 创建表格部件
        self.table_widget.setDragEnabled(True)  # 启用拖拽功能
        self.table_widget.setAcceptDrops(True)  # 允许接收拖拽数据
        self.table_widget.setDragDropOverwriteMode(False)  # 禁用覆盖模式
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择行为为整行选择
        self.table_widget.setDropIndicatorShown(True)  # 显示下拉指示器
        self.table_widget.setDragDropMode(QAbstractItemView.InternalMove)  # 设置拖拽模式为内部移动
        self.layout.addWidget(self.table_widget)  # 将表格部件添加到布局中
        
        self.load_button = QPushButton("Load Excel File")  # 创建加载文件按钮
        self.layout.addWidget(self.load_button)  # 将按钮添加到布局中
        
        self.print_button = QPushButton("Print Excel File")  # 创建打印文件按钮
        self.layout.addWidget(self.print_button)  # 将按钮添加到布局中
        
        self.dataframe = None  # 初始化 DataFrame 为空
        self.dragged_rows = []  # 初始化拖拽行列表为空

        self.bind()  # 绑定信号和槽

    def bind(self):
        """绑定信号和槽"""
        self.table_widget.cellChanged.connect(self.update_dataframe)  # 绑定单元格更改事件到更新函数
        self.load_button.clicked.connect(self.load_excel)  # 绑定按钮点击事件到加载函数
        self.print_button.clicked.connect(self.print_excel)  # 绑定按钮点击事件到打印函数

    def load_excel(self):
        """加载 Excel 文件并更新表格"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")  # 打开文件对话框选择文件
        if not file_path:
            QMessageBox.warning(self, "Warning", "No file selected.")
            return
        
        try:
            self.dataframe = pd.read_excel(file_path)  # 读取 Excel 文件到 DataFrame
            self.update_table()  # 更新表格显示
        except Exception as e:
            print(f"Error loading file: {e}")  # 打印错误信息
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")  # 弹出错误消息框

    def update_table(self):
        """根据 DataFrame 更新表格内容"""
        if self.dataframe is not None:
            self.table_widget.blockSignals(True)  # 阻止信号以提高性能
            self.table_widget.setRowCount(self.dataframe.shape[0])  # 设置表格行数
            self.table_widget.setColumnCount(self.dataframe.shape[1])  # 设置表格列数
            self.table_widget.setHorizontalHeaderLabels(self.dataframe.columns)  # 设置表头
            
            for row in range(self.dataframe.shape[0]):
                for col in range(self.dataframe.shape[1]):
                    item = QTableWidgetItem(str(self.dataframe.iat[row, col]))  # 创建表格项
                    item.setFlags(item.flags() | Qt.ItemIsEditable)  # 设置表格项可编辑
                    self.table_widget.setItem(row, col, item)
            self.table_widget.blockSignals(False)  # 恢复信号

    def update_dataframe(self, row, col):
        """将表格中的更改同步到 DataFrame"""
        if self.dataframe is not None:
            item = self.table_widget.item(row, col)  # 获取表格项
            if item is not None:
                new_value = item.text()  # 获取表格项的新值
                self.dataframe.iat[row, col] = new_value  # 更新 DataFrame 中对应位置的值
                self.update_table()

    def print_excel(self):
        """打印当前 DataFrame 内容"""
        print(self.dataframe)

    def dragEnterEvent(self, event):
        # 禁止放置项目
        event.ignore()

    def dropEvent(self, event):
        # 禁止放置项目
        event.ignore()

    def drop_event(self, event):
        """自定义下拉事件，用于处理行移动"""
        
        if event.source() == self.table_widget:
            target_row = self.table_widget.rowAt(event.position().y())  # 获取目标行索引
            if target_row == -1:
                target_row = self.table_widget.rowCount()  # 如果超出范围，则放置在最后一行
            
            mime_data = event.mimeData()
            if mime_data.hasText():
                dragged_rows_str = mime_data.text()
                if dragged_rows_str.startswith("Rows "):
                    try:
                        dragged_rows = list(map(int, dragged_rows_str[5:].split()))
                        if all(0 <= row < self.table_widget.rowCount() for row in dragged_rows):
                            self.move_rows(dragged_rows, target_row)  # 移动选中的行到目标位置
                            event.accept()  # 接受下拉事件
                        else:
                            event.ignore()  # 忽略无效的拖拽行
                    except ValueError:
                        event.ignore()  # 忽略无效的拖拽行
                else:
                    event.ignore()  # 忽略其他来源的下拉事件
            else:
                event.ignore()  # 忽略其他来源的下拉事件
        else:
            event.ignore()  # 忽略其他来源的下拉事件
        QTableWidget.dropEvent(self.table_widget, event)  # 调用默认的下拉事件

    def move_rows(self, from_rows, to_row):
        """移动指定行到目标位置"""
        if not from_rows or to_row < 0 or to_row >= self.table_widget.rowCount():
            return  # 如果没有要移动的行或目标行超出范围，则直接返回
        
        # 调整目标行索引
        unique_from_rows = sorted(set(from_rows))
        for row in unique_from_rows:
            if row < to_row:
                to_row -= 1
        
        # 提取要移动的行数据
        rows_data = self.dataframe.iloc[unique_from_rows].copy()
        
        # 在目标位置插入新行
        self.dataframe = tool.insert_row_at_index(self.dataframe, rows_data, to_row)
        
        # 删除原行
        self.dataframe = self.dataframe.drop(unique_from_rows).reset_index(drop=True)
        
        self.update_table()  # 更新表格显示

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序实例
    window = ExcelTable()  # 创建主窗口实例
    window.show()  # 显示主窗口
    sys.exit(app.exec())  # 进入应用程序主循环
import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog, QAbstractItemView, QMessageBox, QTableWidgetSelectionRange
from PySide6.QtCore import Qt, QTimer, Signal
import logging

logging.basicConfig(level=logging.INFO)

class ExcelTable(QMainWindow):
    dataframe_ready = Signal(pd.DataFrame)

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
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择行为为整行选择
        self.layout.addWidget(self.table_widget)  # 将表格部件添加到布局中

        # self.load_button = QPushButton("Load Excel File")  # 创建加载文件按钮
        # self.layout.addWidget(self.load_button)  # 将按钮添加到布局中

        self.print_button = QPushButton("Print Excel File")  # 创建打印文件按钮
        self.layout.addWidget(self.print_button)  # 将按钮添加到布局中

        self.move_up_button = QPushButton("Move Up")  # 创建向上移动按钮
        self.layout.addWidget(self.move_up_button)  # 将按钮添加到布局中

        self.move_down_button = QPushButton("Move Down")  # 创建向下移动按钮
        self.layout.addWidget(self.move_down_button)  # 将按钮添加到布局中

        self.confirm_button = QPushButton("Confirm")  # 创建确认按钮
        self.layout.addWidget(self.confirm_button)  # 将按钮添加到布局中

        self.dataframe = None  # 初始化 DataFrame 为空

        self.bind()  # 绑定信号和槽

        # 初始化批量更新相关的变量
        self._pending_updates = []
        self.UPDATE_THRESHOLD = 10  # 根据实际情况调整阈值
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.flush_pending_updates)
        self.update_timer.start(500)  # 每500毫秒检查一次

    def bind(self):
        """绑定信号和槽"""
        self.table_widget.cellChanged.connect(self.update_dataframe)  # 绑定单元格更改事件到更新函数
        # self.load_button.clicked.connect(self.load_excel)  # 绑定按钮点击事件到加载函数
        self.print_button.clicked.connect(self.print_excel)  # 绑定按钮点击事件到打印函数
        self.move_up_button.clicked.connect(self.move_selected_rows_up)  # 绑定向上移动按钮点击事件
        self.move_down_button.clicked.connect(self.move_selected_rows_down)  # 绑定向下移动按钮点击事件
        self.confirm_button.clicked.connect(
            self.confirm_clicked
        )  # 绑定 confirm 按钮点击事件

    def load_excel(self,file_path):
        """加载 Excel 文件并更新表格"""
        try:
            # file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")  # 打开文件对话框选择文件
            if not file_path:
                QMessageBox.warning(self, "Warning", "No file selected.")
                return

            # 验证文件是否为有效的 Excel 文件
            if not file_path.endswith(('.xlsx', '.xls')):
                raise ValueError("Invalid file format")

            self.dataframe = pd.read_excel(file_path,dtype='str')  # 读取 Excel 文件到 DataFrame
            self.update_table()  # 更新表格显示
        except Exception as e:
            logging.error(f"Error loading file: {e}")  # 记录错误日志
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
        if self.dataframe is None or self.table_widget is None:
            return

        try:
            # 获取表格项
            item = self.table_widget.item(row, col)
            if item is None:
                return

            # 获取表格项的新值并尝试转换为目标列的数据类型
            new_value = item.text()
            target_dtype = self.dataframe.dtypes[col]
            try:
                new_value = target_dtype.type(new_value)
            except (ValueError, TypeError):
                logging.warning(f"无法将值 '{new_value}' 转换为列 {col} 的数据类型 {target_dtype}")
                QMessageBox.warning(self, "Warning", f"无法将值 '{new_value}' 转换为列 {col} 的数据类型 {target_dtype}")
                return

            # 确保 row 和 col 在有效范围内
            if row < 0 or row >= len(self.dataframe) or col < 0 or col >= len(self.dataframe.columns):
                logging.warning(f"行 {row} 或列 {col} 超出 DataFrame 范围")
                return

            # 更新 DataFrame 中对应位置的值
            self.dataframe.iat[row, col] = new_value

            # 批量更新后统一调用一次 update_table
            self._pending_updates.append((row, col))
            if len(self._pending_updates) >= self.UPDATE_THRESHOLD:
                self.flush_pending_updates()

        except IndexError as e:
            logging.error(f"索引超出范围: {e}")
        except AttributeError as e:
            logging.error(f"属性错误: {e}")

    def flush_pending_updates(self):
        """刷新待处理的更新"""
        if self._pending_updates:
            self.update_table()
            self._pending_updates.clear()

    def print_excel(self):
        """打印当前 DataFrame 内容"""
        print(self.dataframe)

    def move_selected_rows_up(self):
        """将选中的行向上移动"""
        selected_rows = self.get_selected_rows()
        if not selected_rows:
            return

        if min(selected_rows) == 0:
            QMessageBox.warning(self, "Warning", "Cannot move top row up.")
            return

        # 移动所有选中的行作为一个整体
        self.move_rows(selected_rows, -1)

    def move_selected_rows_down(self):
        """将选中的行向下移动"""
        selected_rows = self.get_selected_rows()
        if not selected_rows:
            return

        if max(selected_rows) == self.table_widget.rowCount() - 1:
            QMessageBox.warning(self, "Warning", "Cannot move bottom row down.")
            return

        # 移动所有选中的行作为一个整体
        self.move_rows(selected_rows, 1)

    def move_rows(self, rows, offset):
        """移动指定行到目标位置"""
        if not rows:
            return

        # 确保行在有效范围内
        if offset < 0 and min(rows) + offset < 0:
            QMessageBox.warning(self, "Warning", "Cannot move top row up.")
            return
        if offset > 0 and max(rows) + offset >= self.table_widget.rowCount():
            QMessageBox.warning(self, "Warning", "Cannot move bottom row down.")
            return

        # 获取选中的行数据
        rows_data = self.dataframe.iloc[rows].copy()

        # 删除原行
        self.dataframe.drop(rows, inplace=True)

        # 插入新行
        target_row = min(rows) + offset
        self.dataframe = pd.concat([self.dataframe.iloc[:target_row], rows_data, self.dataframe.iloc[target_row:]]).reset_index(drop=True)

        # 更新表格显示
        self.update_table()

        # 重新选择移动后的行
        if rows:
            start_row = target_row
            end_row = target_row + len(rows) - 1
            selection_range = QTableWidgetSelectionRange(start_row, 0, end_row, self.table_widget.columnCount() - 1)
            if offset < 0:
                disselection_range = QTableWidgetSelectionRange(max(rows), 0, max(rows), self.table_widget.columnCount() - 1)
            elif offset > 0:
                disselection_range = QTableWidgetSelectionRange(min(rows), 0, min(rows), self.table_widget.columnCount() - 1)
            self.table_widget.setRangeSelected(selection_range, True)
            self.table_widget.setRangeSelected(disselection_range, False)

    def get_selected_rows(self):
        """获取选中的行索引"""
        selected_items = self.table_widget.selectedItems()
        if not selected_items:
            return []

        selected_rows = set()
        for item in selected_items:
            selected_rows.add(item.row())

        return sorted(list(selected_rows))

    def confirm_clicked(self):
        if self.dataframe is not None:
            self.dataframe_ready.emit(self.dataframe)  # 发送 dataframe
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序实例
    window = ExcelTable()  # 创建主窗口实例
    window.show()  # 显示主窗口
    sys.exit(app.exec())  # 进入应用程序主循环

import sys
from PySide6.QtWidgets import QApplication, QWidget
from QTdesign.calculator import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.result = ''
        self.pb_0.clicked.connect(lambda :self.addElement('0'))
        self.pb_1.clicked.connect(lambda :self.addElement('1'))
        self.pb_2.clicked.connect(lambda :self.addElement('2'))
        self.pb_3.clicked.connect(lambda :self.addElement('3'))
        self.pb_4.clicked.connect(lambda :self.addElement('4'))
        self.pb_5.clicked.connect(lambda :self.addElement('5'))
        self.pb_6.clicked.connect(lambda :self.addElement('6'))
        self.pb_7.clicked.connect(lambda :self.addElement('7'))
        self.pb_8.clicked.connect(lambda :self.addElement('8'))
        self.pb_9.clicked.connect(lambda :self.addElement('9'))
        self.pb_point.clicked.connect(lambda :self.addElement('.'))
        self.pb_add.clicked.connect(lambda :self.addElement('+'))
        self.pb_sub.clicked.connect(lambda :self.addElement('-'))
        self.pb_mul.clicked.connect(lambda :self.addElement('*'))
        self.pb_div.clicked.connect(lambda :self.addElement('/'))
        self.pb_equal.clicked.connect(lambda :self.addElement('='))

    def addElement(self, element):
        a = ['1','2','3','4','5','6','7','8','9','0','.','+','-','*','/']
        if element in a:
            self.lcdNumber.display(element)
            self.result += element
        elif element == '=':
            self.lcdNumber.display(eval(self.result))
            self.result = ''
        print(self.result)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()

    # 结束QApplication
    sys.exit(app.exec())
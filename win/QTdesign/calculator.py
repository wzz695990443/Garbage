# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLCDNumber, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(341, 407)
        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 10, 321, 121))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 140, 321, 261))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pb_1 = QPushButton(self.widget)
        self.pb_1.setObjectName(u"pb_1")
        self.pb_1.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_1, 0, 0, 1, 1)

        self.pb_2 = QPushButton(self.widget)
        self.pb_2.setObjectName(u"pb_2")
        self.pb_2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_2, 0, 1, 1, 1)

        self.pb_3 = QPushButton(self.widget)
        self.pb_3.setObjectName(u"pb_3")
        self.pb_3.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_3, 0, 2, 1, 1)

        self.pb_4 = QPushButton(self.widget)
        self.pb_4.setObjectName(u"pb_4")
        self.pb_4.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_4, 1, 0, 1, 1)

        self.pb_5 = QPushButton(self.widget)
        self.pb_5.setObjectName(u"pb_5")
        self.pb_5.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_5, 1, 1, 1, 1)

        self.pb_6 = QPushButton(self.widget)
        self.pb_6.setObjectName(u"pb_6")
        self.pb_6.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_6, 1, 2, 1, 1)

        self.pb_7 = QPushButton(self.widget)
        self.pb_7.setObjectName(u"pb_7")
        self.pb_7.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_7, 2, 0, 1, 1)

        self.pb_8 = QPushButton(self.widget)
        self.pb_8.setObjectName(u"pb_8")
        self.pb_8.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_8, 2, 1, 1, 1)

        self.pb_9 = QPushButton(self.widget)
        self.pb_9.setObjectName(u"pb_9")
        self.pb_9.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_9, 2, 2, 1, 1)

        self.pb_0 = QPushButton(self.widget)
        self.pb_0.setObjectName(u"pb_0")
        self.pb_0.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_0, 3, 1, 1, 1)

        self.pb_add = QPushButton(self.widget)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_add, 0, 3, 1, 1)

        self.pb_sub = QPushButton(self.widget)
        self.pb_sub.setObjectName(u"pb_sub")
        self.pb_sub.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_sub, 1, 3, 1, 1)

        self.pb_mul = QPushButton(self.widget)
        self.pb_mul.setObjectName(u"pb_mul")
        self.pb_mul.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_mul, 2, 3, 1, 1)

        self.pb_equal = QPushButton(self.widget)
        self.pb_equal.setObjectName(u"pb_equal")
        self.pb_equal.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_equal, 3, 2, 1, 1)

        self.pb_div = QPushButton(self.widget)
        self.pb_div.setObjectName(u"pb_div")
        self.pb_div.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_div, 3, 3, 1, 1)

        self.pb_point = QPushButton(self.widget)
        self.pb_point.setObjectName(u"pb_point")
        self.pb_point.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pb_point, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pb_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pb_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pb_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pb_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pb_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pb_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pb_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pb_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pb_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pb_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pb_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.pb_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pb_mul.setText(QCoreApplication.translate("Form", u"*", None))
        self.pb_equal.setText(QCoreApplication.translate("Form", u"=", None))
        self.pb_div.setText(QCoreApplication.translate("Form", u"\u00f7", None))
        self.pb_point.setText(QCoreApplication.translate("Form", u".", None))
    # retranslateUi


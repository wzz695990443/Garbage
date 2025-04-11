# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatabaseChose.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_importFunction(object):
    def setupUi(self, importFunction):
        if not importFunction.objectName():
            importFunction.setObjectName(u"importFunction")
        importFunction.resize(800, 500)
        self.verticalLayout = QVBoxLayout(importFunction)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.functionChose = QGroupBox(importFunction)
        self.functionChose.setObjectName(u"functionChose")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.functionChose.sizePolicy().hasHeightForWidth())
        self.functionChose.setSizePolicy(sizePolicy)
        self.functionChose.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.functionChose)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.companyImportrb = QRadioButton(self.functionChose)
        self.companyImportrb.setObjectName(u"companyImportrb")

        self.horizontalLayout_3.addWidget(self.companyImportrb)

        self.memberImportrb = QRadioButton(self.functionChose)
        self.memberImportrb.setObjectName(u"memberImportrb")

        self.horizontalLayout_3.addWidget(self.memberImportrb)


        self.verticalLayout.addWidget(self.functionChose)

        self.databaseChosebox = QGroupBox(importFunction)
        self.databaseChosebox.setObjectName(u"databaseChosebox")
        self.databaseChosebox.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_2 = QVBoxLayout(self.databaseChosebox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pms = QLabel(self.databaseChosebox)
        self.pms.setObjectName(u"pms")
        self.pms.setMinimumSize(QSize(50, 0))
        self.pms.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.pms)

        self.pmsChose = QComboBox(self.databaseChosebox)
        self.pmsChose.setObjectName(u"pmsChose")
        self.pmsChose.setMinimumSize(QSize(160, 0))
        self.pmsChose.setEditable(True)

        self.horizontalLayout.addWidget(self.pmsChose)

        self.member = QLabel(self.databaseChosebox)
        self.member.setObjectName(u"member")
        self.member.setMinimumSize(QSize(50, 0))
        self.member.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.member)

        self.memberChose = QComboBox(self.databaseChosebox)
        self.memberChose.setObjectName(u"memberChose")
        self.memberChose.setMinimumSize(QSize(160, 0))
        self.memberChose.setEditable(True)

        self.horizontalLayout.addWidget(self.memberChose)

        self.group = QLabel(self.databaseChosebox)
        self.group.setObjectName(u"group")
        self.group.setMinimumSize(QSize(50, 0))
        self.group.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.group)

        self.groupChose = QComboBox(self.databaseChosebox)
        self.groupChose.setObjectName(u"groupChose")
        self.groupChose.setMinimumSize(QSize(160, 0))
        self.groupChose.setEditable(True)

        self.horizontalLayout.addWidget(self.groupChose)

        self.checkBt = QPushButton(self.databaseChosebox)
        self.checkBt.setObjectName(u"checkBt")
        self.checkBt.setMinimumSize(QSize(75, 25))
        self.checkBt.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.checkBt)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.databaseChosebox)

        self.groupBox = QGroupBox(importFunction)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filePath = QTextBrowser(self.groupBox)
        self.filePath.setObjectName(u"filePath")
        self.filePath.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.filePath)

        self.choseFile = QPushButton(self.groupBox)
        self.choseFile.setObjectName(u"choseFile")
        self.choseFile.setMinimumSize(QSize(75, 25))
        self.choseFile.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.choseFile)

        self.editPreview = QPushButton(self.groupBox)
        self.editPreview.setObjectName(u"editPreview")
        self.editPreview.setMinimumSize(QSize(75, 25))
        self.editPreview.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.editPreview)


        self.verticalLayout.addWidget(self.groupBox)

        self.import_2 = QPushButton(importFunction)
        self.import_2.setObjectName(u"import_2")

        self.verticalLayout.addWidget(self.import_2)


        self.retranslateUi(importFunction)

        QMetaObject.connectSlotsByName(importFunction)
    # setupUi

    def retranslateUi(self, importFunction):
        importFunction.setWindowTitle(QCoreApplication.translate("importFunction", u"Form", None))
        self.functionChose.setTitle(QCoreApplication.translate("importFunction", u"\u529f\u80fd\u9009\u62e9", None))
        self.companyImportrb.setText(QCoreApplication.translate("importFunction", u"\u534f\u8bae\u5355\u4f4d\u5bfc\u5165", None))
        self.memberImportrb.setText(QCoreApplication.translate("importFunction", u"\u4f1a\u5458\u5bfc\u5165", None))
        self.databaseChosebox.setTitle(QCoreApplication.translate("importFunction", u"\u6570\u636e\u5e93\u9009\u62e9", None))
        self.pms.setText(QCoreApplication.translate("importFunction", u"\u95e8\u5e97\u5e93\uff1a", None))
        self.member.setText(QCoreApplication.translate("importFunction", u"\u4f1a\u5458\u5e93\uff1a", None))
        self.group.setText(QCoreApplication.translate("importFunction", u"\u96c6\u56e2\u5e93\uff1a", None))
        self.checkBt.setText(QCoreApplication.translate("importFunction", u"\u68c0\u67e5\u8fde\u63a5", None))
        self.groupBox.setTitle(QCoreApplication.translate("importFunction", u"\u6587\u4ef6\u9009\u62e9", None))
        self.choseFile.setText(QCoreApplication.translate("importFunction", u"\u9009\u62e9\u6587\u4ef6", None))
        self.editPreview.setText(QCoreApplication.translate("importFunction", u"\u7f16\u8f91\u9884\u89c8", None))
        self.import_2.setText(QCoreApplication.translate("importFunction", u"\u5bfc\u5165", None))
    # retranslateUi


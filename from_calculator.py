# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'from_calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(257, 192)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_C = QPushButton(Form)
        self.pushButton_C.setObjectName(u"pushButton_C")

        self.horizontalLayout.addWidget(self.pushButton_C)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.multiplication = QPushButton(Form)
        self.multiplication.setObjectName(u"multiplication")

        self.horizontalLayout_2.addWidget(self.multiplication)

        self.division = QPushButton(Form)
        self.division.setObjectName(u"division")

        self.horizontalLayout_2.addWidget(self.division)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.answer = QPushButton(Form)
        self.answer.setObjectName(u"answer")

        self.verticalLayout.addWidget(self.answer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_C.setText(QCoreApplication.translate("Form", u"C", None))
        self.multiplication.setText(QCoreApplication.translate("Form", u"*", None))
        self.division.setText(QCoreApplication.translate("Form", u"/", None))
        self.answer.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'from_a.ui'
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
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(435, 305)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditInput = QLineEdit(Form)
        self.lineEditInput.setObjectName(u"lineEditInput")

        self.horizontalLayout.addWidget(self.lineEditInput)

        self.lineEditMirror = QLineEdit(Form)
        self.lineEditMirror.setObjectName(u"lineEditMirror")

        self.horizontalLayout.addWidget(self.lineEditMirror)

        self.lineEdit3 = QLineEdit(Form)
        self.lineEdit3.setObjectName(u"lineEdit3")

        self.horizontalLayout.addWidget(self.lineEdit3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.pushButtonMirror = QPushButton(Form)
        self.pushButtonMirror.setObjectName(u"pushButtonMirror")

        self.verticalLayout_2.addWidget(self.pushButtonMirror)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEditInput.setText("")
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.pushButtonMirror.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0436\u043c\u0438 \u043c\u0435\u043d\u044f", None))
    # retranslateUi


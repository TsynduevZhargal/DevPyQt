
from PySide6 import QtWidgets
from from_calculator import Ui_Form  #Импортируем класс формы

class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        self.pushButton_2.clicked.connect(lambda: self.mirror("2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.mirror("3"))
        self.ui.multiplication.clicked.connect(lambda: self.mirror("*"))
        self.ui.division.clicked.connect(lambda: self.mirror("/"))
        self.ui.answer.clicked.connect(lambda: self.mirror("="))
        self.ui.pushButton_C.clicked.connect(self.mirror)

    def mirror(self, number):
        self.lineEdit.setText(self.ui.pushButton_2.text()+number)

    def mirror(self, number):
        self.ui.lineEdit.setText(self.ui.pushButton_3.text() + number)

    def mirror(self, number):
        self.ui.lineEdit.setText(self.ui.multiplication.text() + number)

    def mirror(self, number):
        self.ui.lineEdit.setText(self.ui.division.text() + number)



        #





if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
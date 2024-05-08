
from PySide6 import QtWidgets
from from_calculator import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        self.ui.pushButton_2.clicked.connect(self.mirror)
        self.ui.pushButton_3.clicked.connect(self.mirror)
        self.ui.multiplication.clicked.connect(self.mirror)
        self.ui.division.clicked.connect(self.mirror)

        self.ui.pushButton_C.clicked.connect(self.mirror)
        self.ui.answer.clicked.connect(self.mirror)


    def mirror(self):
        text_2 = self.ui.pushButton_2.text()
        text_3 = self.ui.pushButton_3.text()
        text_multiplication = self.ui.multiplication.text()
        text_division = self.ui.division.text()
        self.ui.lineEdit.setText(text_2, text_3, text_multiplication, text_division)

        text_C = (self.ui.pushButton_2.text("2"))
        text_answer = (self.ui.pushButton_2.text("2"))




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
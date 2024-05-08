
from PySide6 import QtWidgets
from from_calculator import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        self.ui.pushButton_2.clicked.connect(lambda: self.mirror("2"))
        # self.ui.pushButton_3.clicked.connect(self.mirror)

    def mirror(self, number):
        self.ui.lineEdit.setText(self.ui.pushButton_2.text()+number)




        # self.ui.multiplication.clicked.connect(self.mirror) + number
        # self.ui.division.clicked.connect(self.mirror)
        #
        # self.ui.pushButton_C.clicked.connect(self.mirror)
        # self.ui.answer.clicked.connect(self.mirror)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
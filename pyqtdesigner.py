import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QLabel

from webscanner import *

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn1 = QPushButton("Button 1", self)
        self.btn1.move(30, 50)

        self.btn2 = QPushButton("Button 2", self)
        self.btn2.move(150, 50)

        self.btn1.clicked.connect(self.buttonClicked)
        self.btn2.clicked.connect(self.buttonClicked)

        self.text = QLabel(self)
        self.text.move(85, 150)

        self.enterwebsite = QLineEdit

        self.setGeometry(600, 600, 580, 300)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        self.text.setText(str(getwebcount('http://zetcode.com/gui/pyqt5/dialogs/')))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
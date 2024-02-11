import unittest
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from functions import *
from tests.test_functions import TestAddressFunctions
from io import StringIO

class MyInterface(QWidget):
    def __init__(self):
        super().__init__()

        font = QFont()
        fontTest = QFont()
        font.setPointSize(16)
        fontTest.setPointSize(8)

        self.setFixedSize(800, 600)

        self.label = QLabel("Digite o endereço:")
        self.label.setFont(font)
        self.console_output = QPlainTextEdit(self)
        self.console_output.setReadOnly(True)
        self.console_output.setFont(fontTest)
        self.entry = QLineEdit()
        self.button = QPushButton("Separar")
        self.buttonTest = QPushButton("Testar")
        self.button.setStyleSheet('background-color: #FFA500;')
        self.buttonTest.setStyleSheet('background-color: #FFA500;')
        self.setStyleSheet('background-color: #ffffff;')

        self.groupBox = QGroupBox("Resposta")
        self.groupBox.setFont(font)
        self.labelAddress = QLabel("")
        self.labelAddress.setFont(font)
        groupBoxLayout = QVBoxLayout()
        groupBoxLayout.addWidget(self.labelAddress)
        self.groupBox.setLayout(groupBoxLayout)

        self.button.clicked.connect(self.on_button_click)
        self.buttonTest.clicked.connect(self.on_button_test_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        layout.addWidget(self.buttonTest)
        layout.addWidget(self.groupBox)
        layout.addWidget(self.console_output)

        self.setLayout(layout)
        self.setWindowTitle("Desafio_Codigo")

        self.setWindowIcon(QIcon('img/address.ico'))

    def on_button_click(self):
        address = self.entry.text()
        self.labelAddress.setText(address_redirector(address))

    def on_button_test_click(self):
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestAddressFunctions)
        test_runner = unittest.TextTestRunner(stream=StringIO(), verbosity=2)
        result = test_runner.run(test_suite)

        output_text = result.stream.getvalue()
        self.console_output.setPlainText(output_text)

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("img/address.ico"))
    interface = MyInterface()
    interface.show()
    app.exec_()

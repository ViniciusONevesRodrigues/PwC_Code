from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from functions import *

class MinhaInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 400)

        self.label = QLabel("Digite o endereço:")
        self.entry = QLineEdit()
        self.button = QPushButton("Clique-me")
        self.labelAddress = QLabel("")
        self.button.clicked.connect(self.on_button_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        layout.addWidget(self.labelAddress)

        self.setLayout(layout)

    def on_button_click(self):
        address = self.entry.text()
        self.labelAddress.setText(address_redirector(address))

# Iniciar a aplicação
app = QApplication([])
interface = MinhaInterface()
interface.show()
app.exec_()

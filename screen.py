from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from functions import *

class MinhaInterface(QWidget):
    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPointSize(16)
        self.setFixedSize(600, 400)

        self.label = QLabel("Digite o endereço:")
        self.label.setFont(font)
        self.entry = QLineEdit()
        self.button = QPushButton("Separar")
        self.button.setStyleSheet('background-color: #FFA500;')
        self.setStyleSheet('background-color: #ffffff;')

        self.groupBox = QGroupBox("Resposta")
        self.groupBox.setFont(font)
        
        self.labelAddress = QLabel("")
        self.labelAddress.setFont(font)
        
        groupBoxLayout = QVBoxLayout()
        groupBoxLayout.addWidget(self.labelAddress)
        self.groupBox.setLayout(groupBoxLayout)

        self.button.clicked.connect(self.on_button_click)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        layout.addWidget(self.groupBox) 

        self.setLayout(layout)

        self.setWindowTitle("Desafio_Codigo")

    def on_button_click(self):
        address = self.entry.text()
        self.labelAddress.setText(address_redirector(address))
    

app = QApplication([])
interface = MinhaInterface()
interface.show()
app.exec_()

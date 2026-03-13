from PySide6.QtWidgets import (QWidget, QLabel, QPushButton,
                               QVBoxLayout, QHBoxLayout, QLineEdit)
from PySide6.QtCore import Qt

from .model import Notebook


class SchoolPage(QWidget):
    def __init__(self):
        super().__init__()

        self.notebook = Notebook("Exam preparation", 30)

        layout = QVBoxLayout(self)

        layout.addLayout(self.create_subject_block('Maths'))

        layout.addLayout(self.create_subject_block('Informatics'))

        layout.addLayout(self.create_subject_block('Russian'))

        layout.addLayout(self.create_subject_block('German'))

    def create_subject_block(self, name):
        label = QLabel(name)
    
        input_field = QLineEdit()
        input_field.setPlaceholderText("Write here")

        button = QPushButton("+")
        button.setFixedWidth(40)

        lower_layout = QHBoxLayout()
        lower_layout.addWidget(input_field)
        lower_layout.addWidget(button)

        block_layout = QVBoxLayout()
        block_layout.addWidget(label)
        block_layout.addLayout(lower_layout)

        return block_layout

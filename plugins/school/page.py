from PySide6.QtWidgets import (QWidget, QLabel, QPushButton,
                               QVBoxLayout, QHBoxLayout, QLineEdit)
from PySide6.QtCore import Qt

from .model import Notebook


class SchoolPage(QWidget):
    def __init__(self):
        super().__init__()

        self.notebook = Notebook("Exam preparation", 30)
        
        # Maths
        self.maths_label = QLabel('Mathematics')

        maths_lower_layout = QHBoxLayout()

        self.maths_input = QLineEdit()
        self.maths_input.setPlaceholderText('Write here')
        self.maths_button = QPushButton('+')

        maths_lower_layout.addWidget(self.maths_input)
        maths_lower_layout.addWidget(self.maths_button)

        # Informatics
        self.informatics_label = QLabel('Informatics')

        informatics_lower_layout = QHBoxLayout()

        self.informatics_input = QLineEdit()
        self.informatics_input.setPlaceholderText('Write here')
        self.informatics_button = QPushButton('+')

        informatics_lower_layout.addWidget(self.informatics_input)
        informatics_lower_layout.addWidget(self.informatics_button)

        # Russian language
        self.russian_label = QLabel('Russian')

        russian_lower_layout = QHBoxLayout()

        self.russian_input = QLineEdit()
        self.russian_input.setPlaceholderText('Write here')
        self.russian_button = QPushButton('+')

        russian_lower_layout.addWidget(self.russian_input)
        russian_lower_layout.addWidget(self.russian_button)

        # German language
        self.german_label = QLabel('German')

        german_lower_layout = QHBoxLayout()

        self.german_input = QLineEdit()
        self.german_input.setPlaceholderText('Write here')
        self.german_button = QPushButton('+')

        german_lower_layout.addWidget(self.german_input)
        german_lower_layout.addWidget(self.german_button)


        layout = QVBoxLayout(self)

        layout.addWidget(self.maths_label)
        layout.addLayout(maths_lower_layout)

        layout.addWidget(self.informatics_label)
        layout.addLayout(informatics_lower_layout)

        layout.addWidget(self.russian_label)
        layout.addLayout(russian_lower_layout)

        layout.addWidget(self.german_label)
        layout.addLayout(german_lower_layout)

    # def add_hours(self, h):
    #     self.notebook.add_hours(h)
    #     self.update_label()

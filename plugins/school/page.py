from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

from .model import Notebook


class SchoolPage(QWidget):
    def __init__(self):
        super().__init__()

        self.notebook = Notebook("Exam preparation", 30)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn1 = QPushButton("+1 hour")
        self.btn2 = QPushButton("+2 hours")

        self.btn1.clicked.connect(lambda: self.add_hours(1))
        self.btn2.clicked.connect(lambda: self.add_hours(2))

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)

        self.update_label()

    def add_hours(self, h):
        self.notebook.add_hours(h)
        self.update_label()

    def update_label(self):
        percent = self.notebook.progress()
        self.label.setText(
            f"{self.notebook.current_hours}/{self.notebook.target_hours}\n"
            f"{percent:.1f}%"
        )
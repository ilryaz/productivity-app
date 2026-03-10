import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QPushButton, QVBoxLayout, QWidget,
                               QHBoxLayout, QListWidget, QStackedWidget,
                               QScrollArea)

class Notebook:
    def __init__(self, name, target_hours):
        self.name = name
        self.target_hours = target_hours
        self.current_hours = 0

    def add_hours(self, hours):
        self.current_hours += hours
        print(f"Added {hours} hours. Total hours: {self.current_hours}/{self.target_hours}")

    def progress(self):
        if self.target_hours == 0:
            return 100
        return (self.current_hours / self.target_hours) * 100
    
class NotebookPage(QWidget):
    def __init__(self):
        super().__init__()

        self.notebook = Notebook("Exam preparation", 30)

        # Label
        self.progress_bar = QLabel()
        font = self.progress_bar.font()
        font.setPointSize(30)
        self.progress_bar.setFont(font)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Buttons
        self.progress_button_1 = QPushButton("+1 hour")
        self.progress_button_2 = QPushButton("+2 hours")

        # Signals
        self.progress_button_1.clicked.connect(lambda: self.add_hours(1))
        self.progress_button_2.clicked.connect(lambda: self.add_hours(2))

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.progress_button_1)
        layout.addWidget(self.progress_button_2)

        for i in range(30):
            layout.addWidget(QLabel(f"Дополнительная строка {i}"))

        self.setLayout(layout)
        self.update_label()

    def update_label(self):
        percent = self.notebook.progress()
        self.progress_bar.setText(
            f"{self.notebook.current_hours}/{self.notebook.target_hours}\n"
            f"{percent:.1f}%"
        )

    def add_hours(self, hours):
        self.notebook.add_hours(hours)
        self.update_label()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Productivity App")

        central_widget = QWidget()
        main_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.addItem("School")
        self.sidebar.setMaximumWidth(300)

        # Stack
        self.stack = QStackedWidget()

        # Page and scroll
        notebook_page = NotebookPage()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(notebook_page)

        self.stack.addWidget(scroll)

        self.sidebar.currentRowChanged.connect(self.stack.setCurrentIndex)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stack, 1)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    
app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.resize(900, 600)
window.show()
app.exec()

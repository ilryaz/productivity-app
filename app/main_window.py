import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QPushButton, QVBoxLayout, QWidget,
                               QHBoxLayout, QListWidget, QStackedWidget,
                               QScrollArea)
from plugins.school.plugin import SchoolPlugin
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Productivity App")

        central_widget = QWidget()
        main_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.setMaximumWidth(300)

        # Stack
        self.stack = QStackedWidget()

        plugin = SchoolPlugin()

        page = plugin.create_page()

        self.sidebar.addItem(plugin.name)
        self.stack.addWidget(page)

        self.sidebar.currentRowChanged.connect(self.stack.setCurrentIndex)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stack, 1)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

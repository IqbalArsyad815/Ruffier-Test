# Step 17 | Import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

# Step 18 | Create Final class from QWidget as third screen
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    # Step 19 | Create set_appear method to set window title, size, and position
    #           Same as first and second screen
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    # Step 20 | Create initUI method to set the interface of the third screen
    def initUI(self):
        # Step 20A | Create widget for final screen interface
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)

        # Step 20B | Create vertical layout, and put every widget into it
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)

        # Step 20C | Set layout_line as main layout
        self.setLayout(self.layout_line)
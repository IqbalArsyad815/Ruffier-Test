# Step 1 | Import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)

# Step 3 | Import module instr.py
from instr import *
# Step 6 | Import second_win.py
from second_win import *

# Step 2 | Create MainWin class from QWidget as first screen
class MainWin(QWidget):
    # Step 2A | Constructor for MainWin class, calling every other methods
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    # # Step 2B | Other methods for MainWin class
    # #           Set everyting as pass for now, remove pass when you put something inside it
    # def set_appear():
    #     pass

    # def initUI():
    #     pass

    # def connects():
    #     pass

    # Step 4 | Create set_appear method to set window title, size, and position
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    # Step 5 | Create initUI method to set the interface of the first screen
    def initUI(self):
        # Step 5A | Create widget for first screen interface
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)

        # Step 5B | Create vertical layout, and put every widget into it
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.button, alignment = Qt.AlignCenter)

        # Step 5C | Set layout_line as main layout
        self.setLayout(self.layout_line)

    # Step 7 | Create next_click method to hide current screen
    #          Create object using TestWin class from second_win.py for second screen
    def next_click(self):
        self.hide()
        self.tw = TestWin()

    # Step 8 | Create connects method to set the trigger for button when it clicked
    def connects(self):
        self.button.clicked.connect(self.next_click)

# Step 9 | Create app object using MainWin class
app = QApplication([])
mw = MainWin()
app.exec_()

# Step 10 | Import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
# Step 14 | Import final_win.py
from final_win import *

# Step 11 | Create TestWin class from QWidget as second screen
class TestWin(QWidget):
    # Step 11A | Constructor for TestWin class, calling every other methods
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    # # Step 11B | Other methods for TestWin class
    # #            Set everyting as pass for now, remove pass when you put something inside it
    # def set_appear():
    #     pass

    # def initUI():
    #     pass

    # def connects():
    #     pass

    # Step 12 | Create set_appear method to set window title, size, and position
    #           Same as first screen
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    # Step 13 | Create initUI method to set the interface of the second screen
    def initUI(self):
        # Step 13A | Create widget for second screen interface
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)

        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.btn_next = QPushButton(txt_sendresults, self)

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        # Step 13B | Create left and right vertical, also horizontal layout, and put every widget into vertical
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        # Step 13C | Create vertical and horizontal layout, and put every widget into vertical
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)

        # Step 13C | Add l_line and r_line to h_line
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        # Step 13D | Set h_line as main layout
        self.setLayout(self.h_line)

    # Step 15 | Create next_click method to set the screen to go to third window
    #           We also create the object of the third window using FinalWin class
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

    # Step 16 | Create connects method to set the trigger for button when it clicked
    def connects(self): 
        self.btn_next.clicked.connect(self.next_click)

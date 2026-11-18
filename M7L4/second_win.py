from PyQt5.QtCore import Qt, QTimer, QTime      # Step 1 | Import QTimer and QTime
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSpinBox,
    QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def initUI(self):
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

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

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

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    # Step 2 | Create timer_test and timer1Event method
    def timer_test(self):
        global time                                                 # Set variable time as global
        time = QTime(0, 0, 15)                                      # Set the time 15s
        self.timer = QTimer()                                       # Create timer object using QTimer class
        self.timer.timeout.connect(self.timer1Event)                # Handler function for timer
        self.timer.start(1000)                                      # Call handler every 1000 ms (1s)

    def timer1Event(self):
        global time                                                 # Set variable time as global
        time = time.addSecs(-1)                                     # Reduce the second in time by 1
        self.text_timer.setText(time.toString("hh:mm:ss"))          # Upadate text_timer text
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))     # Set text_timer font
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")          # Set text_timer color to black
        if time.toString("hh:mm:ss") == "00:00:00":                 # Stop the timer when the second in time reach 0
            self.timer.stop()
    
    # Step 4 | Create timer_sits and timer2Event method
    def timer_sits(self):
        global time                                                 # Set variable time as global
        time = QTime(0, 0, 30)                                      # Set the time 30s
        self.timer = QTimer()                                       # Create timer object using QTimer class
        self.timer.timeout.connect(self.timer2Event)                # Handler function for timer
        self.timer.start(1500)                                      # Call handler every 1500 ms (1.5s)

    def timer2Event(self):
        global time                                                 # Set variable time as global
        time = time.addSecs(-1)                                     # Reduce the second in time by 1
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])     # Upadate text_timer text
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))     # Set text_timer font
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")          # Set text_timer color to black
        if time.toString("hh:mm:ss") == "00:00:00":                 # Stop the timer when the second in time reach 0
            self.timer.stop()

    # Step 6 | Create timer_final and timer3Event method
    def timer_final(self):
        global time                                                 # Set variable time as global
        time = QTime(0, 1, 0)                                       # Set the time 1m
        self.timer = QTimer()                                       # Create timer object using QTimer class
        self.timer.timeout.connect(self.timer3Event)                # Handler function for timer
        self.timer.start(1000)                                      # Call handler every 1000 ms (1s)

    def timer3Event(self):
        global time                                                 # Set variable time as global
        time = time.addSecs(-1)                                     # Reduce the second in time by 1
        self.text_timer.setText(time.toString("hh:mm:ss"))          # Upadate text_timer text
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))     # Set text_timer font

        if int(time.toString("hh:mm:ss")[6:8]) >= 45:               # Set text_timer color to green when second in time > 45
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:             # Set text_timer color to green when second in time < 15
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:                                                       # Set text_timer color to black for the rest
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")

        if time.toString("hh:mm:ss") == "00:00:00":                 # Stop the timer when the second in time reach 0
            self.timer.stop()
    
    def connects(self):
        # Step 3 | Coneect btn_test1 to timer_test method when clicked
        self.btn_test1.clicked.connect(self.timer_test)
        # Step 5 | Coneect btn_test2 to timer_sits method when clicked
        self.btn_test2.clicked.connect(self.timer_sits)
        # Step 7 | Coneect btn_test2 to timer_sits method when clicked
        self.btn_test3.clicked.connect(self.timer_final)
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        # Step 9 | Create a new object using Experiment class
        self.exp = Experiment(
            self.line_age.text(),
            self.line_test1.text(),
            self.line_test2.text(),
            self.line_test3.text()
        )
        self.fw = FinalWin(self.exp)        # Step 10 | Send the object as argument when createing fw object using FinalWin class

# Step 8 | Create Experiment class to store the data of the test data
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.t1 = int(test1)
        self.t2 = int(test2)
        self.t3 = int(test3)

# Step 11-17 | On final_win.py
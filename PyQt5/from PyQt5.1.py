from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton)


#creating an application object
app = QApplication([])
# creating the main window object
main_win = QWidget()
# creating the name of the main window
main_win.setWindowTitle('Quiz')


question = QLabel('What year was Algorithmics founded in?')
btn_answer1 = QRadioButton('2013')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2016')
btn_answer4 = QRadioButton('2019')
btn_answer5 = QRadioButton('2023')
btn_answer6 = QRadioButton('2026')


layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layoutH4.addWidget(btn_answer5, alignment = Qt.AlignCenter)
layoutH4.addWidget(btn_answer6, alignment = Qt.AlignCenter)
layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addLayout(layoutH4)
main_win.setLayout(layout_main)

def show_win():
    win = QMessageBox()
    win.setText('Right! \n You did it!')
    win.exec_()
    
def show_lose():
    lose = QMessageBox()
    lose.setText('False! \n Try again!')
    lose.exec_()
    

btn_answer3.clicked.connect(show_win)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)
btn_answer5.clicked.connect(show_lose)
btn_answer6.clicked.connect(show_lose)

main_win.show()
app.exec_()
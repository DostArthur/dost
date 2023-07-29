from PyQt5.QtCore import Qt
#connecting the required widgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox, QRadioButton)
import random

#creating an application object
app = QApplication([])
# creating the main window object
main_win = QWidget()
# creating the name of the main window
main_win.setWindowTitle('Winner\'s determiner')
# creating a button object and setting a label on it
but = QPushButton('Generate')
# creating a text object
text = QLabel('Click to find out the winner')
# creating a text object
winner = QLabel('?')

# creating a Vertical layout
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)
       
#Creating an event handler function
def show_winner():
    x = random.randint(1,100)
    winner.setText(str(x))
    
# linking a button press to a function call
but.clicked.connect(show_winner)
   
# giving the window the command to show up
main_win.show()
#Leaves the app open until the exit button is pressed
app.exec_()
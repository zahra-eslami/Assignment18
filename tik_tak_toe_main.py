import sys
from functools import partial

from PySide6.QtWidgets import QApplication, QLabel,QDialog,QVBoxLayout,QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QMovie
from PySide6.QtCore import QSize, Qt


# -------------------------------------------------------------------------------------------#

def show_custom_message_box(title, text, gif_path, width=200, height=200):
    dialog = QDialog()
    dialog.setWindowTitle(title)
    dialog_layout = QVBoxLayout(dialog)

    label = QLabel(dialog)
    movie = QMovie(gif_path)
    scaled_size = QSize(width - 40, height - 50)
    movie.setScaledSize(scaled_size)
    label.setMovie(movie)
    movie.start()

    label.setAlignment(Qt.AlignCenter)

    text_html = f'<div style="font-size: 32pt; font-weight: bold; color: green; text-align: center; display: flex; justify-content: center; align-items: center;">{text}</div>'
    label_text = QLabel(text_html, dialog)
    dialog_layout.addWidget(label)
    dialog_layout.addWidget(label_text)

    dialog.setMinimumSize(width, height)
    dialog.exec()

# -------------------------------------------------------------------------------------------#

def check(player):
    is_tie=True
    # Check rows
    for i in range(3):
        if buttons[i][0].text == buttons[i][1].text == buttons[i][2].text and buttons[i][0].text != '':
            show_custom_message_box('Tik Tak Toe', f'Player {player} wins!', 'Assignment18/win.gif')
            return

    # Check columns
    for j in range(3):
        if buttons[0][j].text == buttons[1][j].text == buttons[2][j].text and buttons[0][j].text != '':
            show_custom_message_box('Tik Tak Toe', f'Player {player} wins!', 'Assignment18/win.gif')
            return

    # Check diagonals
    if buttons[0][0].text == buttons[1][1].text == buttons[2][2].text and buttons[0][0].text != '':
        show_custom_message_box('Tik Tak Toe', f'Player {player} wins!', 'Assignment18/win.gif')
        return
    if buttons[0][2].text == buttons[1][1].text == buttons[2][0].text and buttons[0][2].text != '':
        show_custom_message_box('Tik Tak Toe', f'Player {player} wins!', 'Assignment18/win.gif')
        return

    for i in range (3):
        for j in range(3):
            if buttons[i][j].text != 'x' and buttons[i][j].text != 'o':
                is_tie=False

    if is_tie:
        show_custom_message_box('Tik Tak Toe', 'It''s a Tie!', 'Assignment18/lost.gif')
        return
# -------------------------------------------------------------------------------------------# 
    
def play(row,col):
    global player
    
    if buttons[row][col].text in ['x', 'o']:
        QMessageBox.warning(None, 'Invalid Move', 'Please select an empty cell.')
        return

    button_size = buttons[row][col].size()
    icon_size = QSize(button_size.width() - 20, button_size.height() - 20)
    buttons[row][col].setIconSize(icon_size) 

    if player == 1:
        buttons[row][col].setIcon(QIcon("Assignment18/x.png")) 
        buttons[row][col].text='x'
        check(player)
        player = 2

    elif player == 2:
        buttons[row][col].setIcon(QIcon("Assignment18/o.png")) 
        buttons[row][col].text='o'
        check(player)
        player = 1
    

# -------------------------------------------------------------------------------------------#


loader = QUiLoader()
my_app = QApplication(sys.argv)

player=1

my_window = loader.load("Assignment18/tik_tak_toe_window.ui")
my_window.show()

button_size = my_window.btn_reset.size()
icon_size = QSize(button_size.width() - 20, button_size.height() - 20)
my_window.btn_reset.setIconSize(icon_size) 
my_window.btn_reset.setIcon(QIcon("Assignment18/refresh-icon"))

buttons=[[my_window.btn1, my_window.btn2, my_window.btn3],
       [my_window.btn4, my_window.btn5, my_window.btn6],
       [my_window.btn7, my_window.btn8, my_window.btn9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play,i,j))

my_app.exec()
# sys.exit(my_app.exec())

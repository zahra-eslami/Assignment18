import sys
from functools import partial
import random

from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QMessageBox,QLabel
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

winx = 0
wino = 0
tie = 0

def check(player):
    global game_over, winx, wino, tie
    is_tie = True
    # Check rows
    for i in range(3):
        if buttons[i][0].text == buttons[i][1].text == buttons[i][2].text and buttons[i][0].text != '':
            show_custom_message_box('Tik Tak Toe', f'Player {player} wins!', 'Assignment18/win.gif')
            game_over = True
            if player == 1:
                winx += 1
                my_window.btn_x.setText(f"X (YOU):{winx}")
            else:
                wino += 1
                my_window.btn_o.setText(f"O (CPU):{wino}")
            return

    # Check columns
    for j in range(3):
        if buttons[0][j].text == buttons[1][j].text == buttons[2][j].text and buttons[0][j].text != '':
            show_custom_message_box('Tik Tak Toe', f'Player {player} wins!', 'Assignment18/win.gif')
            game_over = True
            if player == 1:
                winx += 1
                my_window.btn_x.setText(f"X (YOU):{winx}")
            else:
                wino += 1
                my_window.btn_o.setText(f"O (CPU):{wino}")
            return

    # Check diagonals
    if buttons[0][0].text == buttons[1][1].text == buttons[2][2].text and buttons[0][0].text != '':
        show_custom_message_box('Tik Tak Toe', f'Player {player} wins!', 'Assignment18/win.gif')
        game_over = True
        if player == 1:
            winx += 1
            my_window.btn_x.setText(f"X (YOU):{winx}")
        else:
            wino += 1
        return
    if buttons[0][2].text == buttons[1][1].text == buttons[2][0].text and buttons[0][2].text != '':
        show_custom_message_box('Tik Tak Toe', f'Player {player} wins!', 'Assignment18/win.gif')
        game_over = True
        if player == 1:
            winx += 1
            my_window.btn_x.setText(f"X (YOU):{winx}")
        else:
            wino += 1
            my_window.btn_o.setText(f"O (CPU):{wino}")
        return

    for i in range(3):
        for j in range(3):
            if buttons[i][j].text != 'x' and buttons[i][j].text != 'o':
                is_tie = False

    if is_tie:
        show_custom_message_box('Tik Tak Toe', 'It''s a Tie!', 'Assignment18/lost.gif')
        game_over = True
        tie += 1
        my_window.btn_tie.setText(f"TIES:{tie}")
        return

# -------------------------------------------------------------------------------------------#

def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j].text not in ['x', 'o']]
    if empty_cells:
        row, col = random.choice(empty_cells)

    return row, col

def play(row, col):
    global player, selected_value, game_over

    if game_over:
        return

    if buttons[row][col].text in ['x', 'o']:
        QMessageBox.warning(None, 'Invalid Move', 'Please select an empty cell.')
        return

    button_size = buttons[row][col].size()
    icon_size = QSize(button_size.width() - 20, button_size.height() - 20)
    buttons[row][col].setIconSize(icon_size)

    if selected_value == 1:
        if player == 1:
            buttons[row][col].setIcon(QIcon("Assignment18/x.png"))
            buttons[row][col].text = 'x'
            check(player)
            player = 2
            my_window.btn_turn.setText("O Turn")

        elif player == 2:
            buttons[row][col].setIcon(QIcon("Assignment18/o.png"))
            buttons[row][col].text = 'o'
            check(player)
            player = 1
            my_window.btn_turn.setText("X Turn")

    elif selected_value == 2:
        if player == 1: 
            buttons[row][col].setIcon(QIcon("Assignment18/x.png"))
            buttons[row][col].text = 'x'
            check(player)
            player = 2
            my_window.btn_turn.setText("O Turn")

            if game_over:
                return
            else:
                row, col = computer_move()
                button_size = buttons[row][col].size()
                icon_size = QSize(button_size.width() - 20, button_size.height() - 20)
                buttons[row][col].setIconSize(icon_size)
                buttons[row][col].setIcon(QIcon("Assignment18/o.png"))
                buttons[row][col].text = 'o'
                check(player)
                player = 1
                my_window.btn_turn.setText("X Turn")

    elif selected_value == 2 and player == 2 and not game_over:
        row, col = computer_move()
        button_size = buttons[row][col].size()
        icon_size = QSize(button_size.width() - 20, button_size.height() - 20)
        buttons[row][col].setIconSize(icon_size)
        buttons[row][col].setIcon(QIcon("Assignment18/o.png"))
        buttons[row][col].text = 'o'
        check(player)
        player = 1
        my_window.btn_turn.setText("X Turn")

def reset_game():
    for i in range(3):
        for j in range(3):
            buttons[i][j].text = ''
            buttons[i][j].setIcon(QIcon())
    global player, game_over
    player = 1
    game_over = False

def set_variable_value():
    global selected_value
    selected_value = 1
    if new_game_window.r_btn_1.isChecked():
        selected_value = 1
    elif new_game_window.r_btn_2.isChecked():
        selected_value = 2
    reset_game()

    new_game_window.close()

# -------------------------------------------------------------------------------------------#

def new_game():
    new_game_window.r_btn_2.setChecked(True)
    new_game_window.show()

def cancel():
    new_game_window.close()
# -------------------------------------------------------------------------------------------#

loader = QUiLoader()
my_app = QApplication(sys.argv)

player = 1
selected_value = 1
game_over = False
winx= wino =tie =0

my_window = loader.load("Assignment18/tik_tak_toe_window.ui")
new_game_window = loader.load("Assignment18/new_game.ui")
my_window.setWindowTitle("Tik Tak Toe")
my_window.show()

new_game_window.btn_ok.clicked.connect(partial(set_variable_value))
new_game_window.btn_cancel.clicked.connect(partial(cancel))


button_size = my_window.btn_reset.size()
icon_size = QSize(button_size.width() - 20, button_size.height() - 20)

my_window.btn_reset.setIconSize(icon_size)
my_window.btn_reset.setIcon(QIcon("Assignment18/refresh-icon.png"))
my_window.btn_reset.clicked.connect(partial(new_game))

my_window.btn_xo.setIconSize(icon_size)
my_window.btn_xo.setIcon(QIcon("Assignment18/x-o.png"))

my_window.btn_turn.setText("X Turn")
my_window.btn_x.setText(f"X (YOU):{winx}")
my_window.btn_o.setText(f"O (CPU):{wino}")
my_window.btn_tie.setText(f"TIES:{tie}")

buttons = [[my_window.btn1, my_window.btn2, my_window.btn3],
           [my_window.btn4, my_window.btn5, my_window.btn6],
           [my_window.btn7, my_window.btn8, my_window.btn9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

my_app.exec()

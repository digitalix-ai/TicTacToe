import turtle
import random
import os

turtle_pen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(850, 700)
turtle_pen.hideturtle()
is_users_turn = True
can_user_go = False
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
section_1_midpoint = (-200, 100)
section_2_midpoint = (0, 100)
section_3_midpoint = (200, 100)
section_4_midpoint = (-200, -100)
section_5_midpoint = (0, -100)
section_6_midpoint = (200, -100)
section_7_midpoint = (-200, -300)
section_8_midpoint = (0, -300)
section_9_midpoint = (200, -300)
is_popup_showing = False


def setup_board():
    """Set up the tic tac toe board"""
    screen.bgcolor("yellow")
    turtle_pen.width(20)
    turtle_pen.color("purple")
    draw_line(-300, -200)
    draw_line(-300, 0)
    turtle_pen.up()
    turtle_pen.rt(90)
    draw_line(-100, 200)
    draw_line(100, 200)
    turtle_pen.rt(-90)
    turtle_pen.up()


def draw_line(x, y):
    """Draws a line from the starting point (x,y)"""
    turtle_pen.up()
    turtle_pen.goto(x, y)
    turtle_pen.down()
    turtle_pen.forward(600)


def write_message(message, color):
    """Write a message to the screen in a specified color"""
    global  can_user_go
    turtle_pen.goto(-190, 300)
    turtle_pen.down()
    turtle_pen.width(5)
    turtle_pen.color(color)
    turtle_pen.write(message, False, "left", ("Arial", 60, "normal"))
    if is_users_turn:
        can_user_go = True


def start_game():
    """Starts the game"""
    write_message("Your turn!", "red")


def draw_part_of_x(degrees):
    """Draws one part of the x symbol"""
    turtle_pen.rt(degrees)
    turtle_pen.down()
    turtle_pen.forward(100)
    turtle_pen.up()
    turtle_pen.back(100)


def draw_x(midpoint):
    """Draws an X in the midpoint of a square"""
    global  is_users_turn
    turtle_pen.color("red")
    turtle_pen.up()
    turtle_pen.goto(midpoint[0], midpoint[1])
    turtle_pen.width(15)
    draw_part_of_x(45)
    draw_part_of_x(90)
    draw_part_of_x(90)
    draw_part_of_x(90)
    turtle_pen.setheading(0)
    is_users_turn = False


def draw_symbol(midpoint):
    """Used to draw a symbol into a space"""
    global is_users_turn
    if is_users_turn:
        draw_x(midpoint)
        erase_text()
        if not check_for_win("x") and not is_popup_showing:
            write_message("CPU's turn", "blue")
            cpu_ai_logic()
            is_users_turn = True
    else:
        draw_o(midpoint)
        erase_text()
        if not is_popup_showing:
            write_message("Your turn!", "pink")
            is_users_turn = False


def check_for_win(symbol):
    """Checks the board to see if there is a win"""
    global is_popup_showing

    row_1_win = (board[0][0] == symbol) and (board[0][1] == symbol) and (board[0][2] == symbol)
    row_2_win = (board[1][0] == symbol) and (board[1][1] == symbol) and (board[1][2] == symbol)
    row_3_win = (board[2][0] == symbol) and (board[2][1] == symbol) and (board[2][2] == symbol)

    column_1_win = (board[0][0] == symbol) and (board[1][0] == symbol) and (board[2][0] == symbol)
    column_2_win = (board[0][1] == symbol) and (board[1][1] == symbol) and (board[2][1] == symbol)
    column_3_win = (board[0][2] == symbol) and (board[1][2] == symbol) and (board[2][2] == symbol)

    diagnol_1_win = (board[0][0] == symbol) and (board[1][1] == symbol) and (board[2][2] == symbol)
    diagnol_2_win = (board[0][2] == symbol) and (board[1][1] == symbol) and (board[2][0] == symbol)

    has_someone_won = row_1_win or row_2_win or row_3_win or column_1_win or column_2_win or column_3_win or diagnol_1_win or diagnol_2_win

    if has_someone_won:
        show_popup(symbol)
        return True
    else:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != "-":
                    count += 1
        if count == 9:
            is_popup_showing = True
            screen.clear()
            screen.bgcolor("yellow")
            t = turtle.Turtle()
            t.hideturtle()
            t.down()
            write_message("Tie", "green")
            draw_replay_and_quit_buttons(t)
        return False


def show_popup(symbol):
    """Displays you win or game over popup"""
    global is_popup_showing
    is_popup_showing = True
    screen.clear()
    screen.bgcolor("yellow")
    t = turtle.Turtle()
    t.hideturtle()
    t.down()
    if symbol == "x":
        write_message("You win!", "cyan")
    else:
        write_message("Game over!", "red")
    draw_replay_and_quit_buttons(t)


def draw_replay_and_quit_buttons(t):
    """Draws replay and quit buttons"""
    replay_button = turtle.Turtle()
    replay_button.onclick(replay)
    replay_button.hideturtle()
    replay_button.shape("square")
    replay_button.turtlesize(5, 25)
    replay_button.color("cyan")
    replay_button.speed("fastest")
    replay_button.up()
    replay_button.goto(t.pos() + (0, -100))
    replay_button.showturtle()

    replay_button_text = turtle.Turtle()
    replay_button_text.hideturtle()
    replay_button_text.color("white")
    replay_button_text.pensize(10)
    replay_button_text.up()
    replay_button_text.goto(replay_button.pos() + (-120, -40))
    replay_button_text.down()
    replay_button_text.write("Replay", False, "left", ("Arial", 60, "normal"))

    quit_button = turtle.Turtle()
    quit_button.onclick(quit_game)
    quit_button.hideturtle()
    quit_button.shape("square")
    quit_button.turtlesize(5, 25)
    quit_button.color("pink")
    quit_button.speed("fastest")
    quit_button.up()
    quit_button.goto(t.pos() + (0, -250))
    quit_button.showturtle()

    quit_button_text = turtle.Turtle()
    quit_button_text.hideturtle()
    quit_button_text.color("brown")
    quit_button_text.pensize(10)
    quit_button_text.up()
    quit_button_text.goto(quit_button.pos() + (-95, -40))
    quit_button_text.down()
    quit_button_text.write("Quit", False, "left", ("Arial", 60, "normal"))


def replay(x, y):
    """Restarts the script if the user clicks the replay button"""
    screen.bye()
    os.system("TicTacToeExample.py")


def quit_game(x, y):
    """Closes the program if the user clicks the quit button"""
    screen.bye()


def let_user_place_symbol(x_pos, y_pos):
    """Lets the user place an X"""
    global can_user_go
    can_user_go = False
    in_first_section = -300 <= x_pos <= -100 and 0 <= y_pos <= 200 and is_section_empty(0, 0)
    in_second_section = -100 <= x_pos <= 100 and 0 <= y_pos <= 200 and is_section_empty(0, 1)
    in_third_section = 100 <= x_pos <= 300 and 0 <= y_pos <= 200 and is_section_empty(0, 2)
    in_fourth_section = -300 <= x_pos <= -100 and -200 <= y_pos <= 0 and is_section_empty(1, 0)
    in_fifth_section = -100 <= x_pos <= 100 and -200 <= y_pos <= 0 and is_section_empty(1, 1)
    in_sixth_section = 100 <= x_pos <= 300 and -200 <= y_pos <= 0 and is_section_empty(1, 2)
    in_seventh_section = -300 <= x_pos <= -100 and -400 <= y_pos <= -200 and is_section_empty(2, 0)
    in_eight_section = -100 <= x_pos <= 100 and -400 <= y_pos <= -200 and is_section_empty(2, 1)
    in_ninth_section = 100 <= x_pos <= 300 and -400 <= y_pos <= -200 and is_section_empty(2, 2)

    if in_first_section:
        board[0][0] = "x"
        draw_symbol(section_1_midpoint)
    elif in_second_section:
        board[0][1] = "x"
        draw_symbol(section_2_midpoint)
    elif in_third_section:
        board[0][2] = "x"
        draw_symbol(section_3_midpoint)
    elif in_fourth_section:
        board[1][0] = "x"
        draw_symbol(section_4_midpoint)
    elif in_fifth_section:
        board[1][1] = "x"
        draw_symbol(section_5_midpoint)
    elif in_sixth_section:
        board[1][2] = "x"
        draw_symbol(section_6_midpoint)
    elif in_seventh_section:
        board[2][0] = "x"
        draw_symbol(section_7_midpoint)
    elif in_eight_section:
        board[2][1] = "x"
        draw_symbol(section_8_midpoint)
    elif in_ninth_section:
        board[2][2] = "x"
        draw_symbol(section_9_midpoint)
    else:
        can_user_go = True


def is_section_empty(index1, index2):
    """Checks if a square on the board is empty"""
    if board[index1][index2] == "-":
        return True
    else:
        return False

def erase_text():
    """Erases the text shown on the screen"""
    turtle_pen.speed("fastest")
    turtle_pen.goto(-190, 320)
    turtle_pen.down()
    turtle_pen.width(150)
    turtle_pen.setheading(0)
    turtle_pen.color("yellow")
    turtle_pen.forward(500)
    turtle_pen.speed("normal")


def draw_o(midpoint):
    """Draws an o in the middle of a square"""
    global is_users_turn
    turtle_pen.color("blue")
    turtle_pen.up()
    turtle_pen.goto(midpoint[0], midpoint[1])
    turtle_pen.rt(90)
    turtle_pen.forward(90)
    turtle_pen.lt(90)
    turtle_pen.down()
    turtle_pen.width(15)
    turtle_pen.circle(85)
    turtle_pen.up()
    is_users_turn = True


def cpu_ai_logic():
    """Lets CPU choose a spot and place o"""
    global is_users_turn
    is_users_turn = False
    open_spots = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "-":
                open_spot = (i, j)
                open_spots.append(open_spot)

    if len(open_spots) > 0:
        cpu_choice = random.randrange(0, len(open_spots))
        cpu_choice = open_spots[cpu_choice]

        if cpu_choice == (0, 0):
            board[0][0] = "o"
            draw_symbol(section_1_midpoint)
        elif cpu_choice == (0, 1):
            board[0][1] = "o"
            draw_symbol(section_2_midpoint)
        elif cpu_choice == (0, 2):
            board[0][2] = "o"
            draw_symbol(section_3_midpoint)
        elif cpu_choice == (1, 0):
            board[1][0] = "o"
            draw_symbol(section_4_midpoint)
        elif cpu_choice == (1, 1):
            board[1][1] = "o"
            draw_symbol(section_5_midpoint)
        elif cpu_choice == (1, 2):
            board[1][2] = "o"
            draw_symbol(section_6_midpoint)
        elif cpu_choice == (2, 0):
            board[2][0] = "o"
            draw_symbol(section_7_midpoint)
        elif cpu_choice == (2, 1):
            board[2][1] = "o"
            draw_symbol(section_8_midpoint)
        elif cpu_choice == (2, 2):
            board[2][2] = "o"
            draw_symbol(section_9_midpoint)

        check_for_win("o")


setup_board()
screen.onclick(let_user_place_symbol)
screen.listen()
start_game()
turtle.done()
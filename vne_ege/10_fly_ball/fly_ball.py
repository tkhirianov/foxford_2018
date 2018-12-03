import tkinter
import time
from random import randint

# Режим игры - игра идёт или нет
game_began = False
sleep_time = 50  # ms
scores = 0

initial_balls_number = 5

# Список шариков, каждый из которых - список: [x, y, dx, dy, r, oval_id]
balls = []


# --------- GAME CONTROLLER: ----------
def tick():
    time_label.after(sleep_time, tick)
    time_label['text'] = time.strftime('%H:%M:%S')
    if game_began:
        game_step()


def button_start_game_handler():
    global game_began
    if not game_began:
        game_start()
        game_began = True


def button_stop_game_handler():
    global game_began
    if game_began:
        game_stop()
        game_began = False


# --------- GAME MODEL: ----------
def game_start():
    for i in range(initial_balls_number):
        ball = ball_create()
        balls.append(ball)


def game_stop():
    for ball in balls:
        ball_delete(ball)


def game_step():
    for ball in balls:
        ball_step(ball)


def ball_create():
    r = randint(10, 30)
    x = randint(0 + r, 639 - r)
    y = randint(0 + r, 479 - r)
    dx = randint(-4, 4)
    dy = randint(-4, 4)
    oval_id = canvas.create_oval(x - r, y - r, x + r, y + r, fill='green')
    ball = [x, y, dx, dy, r, oval_id]
    return ball


def ball_delete(ball):
    x, y, dx, dy, r, oval_id = ball
    canvas.delete(oval_id)
    oval_id = None
    ball[:] = x, y, dx, dy, r, oval_id


def ball_step(ball):
    """
    Сдвигает шарик ball в соответствии с его скоростью.
    :param ball: список [x, y, dx, dy, r, oval_id]
    """
    x, y, dx, dy, r, oval_id = ball
    if oval_id is not None:
        x += dx
        y += dy
        if x + r >= 639 or x - r <= 0:
            dx = -dx
        if y + r >= 479 or y - r <= 0:
            dy = -dy
        canvas.coords(oval_id, (x - r, y - r, x + r, y + r))
    ball[:] = x, y, dx, dy, r, oval_id


# --------- GAME VIEW: ----------
root = tkinter.Tk("Лопни шарик!")
root.geometry("640x480")

buttons_panel = tkinter.Frame(bg="gray", width=640)
buttons_panel.pack(side=tkinter.TOP, anchor="nw", fill=tkinter.X)
button_start = tkinter.Button(buttons_panel, text="Start",
                              command=button_start_game_handler)
button_start.pack(side=tkinter.LEFT)
button_stop = tkinter.Button(buttons_panel, text="Stop",
                             command=button_stop_game_handler)
button_stop.pack(side=tkinter.LEFT)
time_label = tkinter.Label(buttons_panel, font='sans 14')
time_label.pack(side=tkinter.LEFT)
scores_text = tkinter.Label(buttons_panel, text="Ваши очки: 0")
scores_text.pack(side=tkinter.RIGHT)
canvas = tkinter.Canvas(root, bg='lightgray')
canvas.pack(anchor="nw", fill=tkinter.BOTH, expand=1)

time_label.after_idle(tick)
root.mainloop()

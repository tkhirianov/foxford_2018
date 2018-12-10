import tkinter
import time
from random import randint


canvas_width = 640
canvas_height = 480

# --------- GAME CONTROLLER: ----------
# Режим игры - игра идёт или нет
game_began = False
sleep_time = 50  # ms
scores = 0


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
initial_balls_number = 5
balls = []  # список объектов типа Ball


def game_start():
    for i in range(initial_balls_number):
        ball = Ball()
        balls.append(ball)


def game_stop():
    for ball in balls:
        ball.delete()


def game_step():
    for ball in balls:
        ball.step()


class Ball:
    def __init__(self):
        self.r = randint(10, 30)
        self.x = randint(0 + self.r, canvas_width - self.r)
        self.y = randint(0 + self.r, canvas_height - self.r)
        self.dx = randint(-4, 4)
        self.dy = randint(-4, 4)
        self.oval_id = canvas.create_oval(self.x - self.r, self.y - self.r,
                                          self.x + self.r, self.y + self.r,
                                          fill='green')

    def delete(self):
        canvas.delete(self.oval_id)
        self.oval_id = None

    def step(self):
        """ Сдвигает шарик ball в соответствии с его скоростью.
        """
        if self.oval_id is not None:
            self.x += self.dx
            self.y += self.dy
            if self.x + self.r >= canvas_width or self.x - self.r <= 0:
                self.dx = -self.dx
            if self.y + self.r >= canvas_height or self.y - self.r <= 0:
                self.dy = -self.dy
            canvas.coords(self.oval_id, (self.x - self.r, self.y - self.r,
                                         self.x + self.r, self.y + self.r))


# --------- GAME VIEW: ----------
root = tkinter.Tk("Лопни шарик!")

buttons_panel = tkinter.Frame(bg="gray", width=canvas_width)
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
canvas = tkinter.Canvas(root, bg='lightgray', width=canvas_width, height=canvas_height)
canvas.pack(anchor="nw", fill=tkinter.BOTH, expand=1)

time_label.after_idle(tick)
root.mainloop()

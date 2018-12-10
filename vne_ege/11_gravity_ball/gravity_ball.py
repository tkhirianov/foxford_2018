import tkinter
import time
import math
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
t = 0
dt = 0.05  # Квант модельного (рассчётного) времени.


def game_start():
    for i in range(initial_balls_number):
        ball = Ball()
        balls.append(ball)


def game_stop():
    for ball in balls:
        ball.delete()


def game_step():
    global t
    for ball in balls:
        ball.step()
    t += dt


class Ball:
    density = 1.0  # стандартная плотность

    def __init__(self):
        self.r = randint(10, 30)
        self.m = self.density*math.pi*self.r**2  # Масса пропорциональна площади, т.е. квадрату радиуса.
        self.x = randint(0 + self.r, canvas_width - self.r)
        self.y = randint(0 + self.r, canvas_height - self.r)
        self.Vx = randint(-100, 100)
        self.Vy = randint(-100, 100)
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
            Fx, Fy = self.force()
            ax = Fx / self.m
            ay = Fy / self.m

            self.x += self.Vx*dt + ax*dt**2 / 2
            self.y += self.Vy*dt + ay*dt**2 / 2
            self.Vx += ax*dt
            self.Vy += ay*dt

            if self.x + self.r >= canvas_width or self.x - self.r <= 0:
                self.Vx = -self.Vx
            if self.y + self.r >= canvas_height or self.y - self.r <= 0:
                self.Vy = -self.Vy
            canvas.coords(self.oval_id, (self.x - self.r, self.y - self.r,
                                         self.x + self.r, self.y + self.r))

    def force(self):
        Fx = 0
        Fy = self.m*9.8  # default gravity
        return Fx, Fy

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

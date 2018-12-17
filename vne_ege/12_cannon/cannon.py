import tkinter
import time
import math
from random import randint


canvas_width = 640
canvas_height = 480
default_initial_balls_number = 10


# --------- GAME MODEL: ----------
class Game:
    def __init__(self, initial_balls_number):
        self.initial_balls_number = initial_balls_number
        self.balls = []  # список объектов типа Ball
        self.tank = Tank(canvas_width//2, canvas_height, "darkgreen")
        self.t = 0
        self.dt = 0.05  # Квант модельного (рассчётного) времени.
        self.paused = True
        for i in range(initial_balls_number):
            ball = Ball()
            self.balls.append(ball)

    def start(self):
        self.paused = False

    def stop(self):
        self.paused = True

    def step(self):
        # рассчёт полёта каждого шарика:
        for ball in self.balls:
            ball.step(self.dt)
        # рассчёт столкновений шариков:
        for i in range(len(self.balls)):
            for k in range(i+1, len(self.balls)):
                if self.balls[i].intersect(self.balls[k]):
                    self.balls[i].collide(self.balls[k])
        self.t += self.dt

    def click(self, x, y):
        # TODO: поменять логику клика - теперь это должен быть выстрел танка (откуда брать энергию?)
        for i in range(len(self.balls)-1, -1, -1):
            if self.balls[i].overlap(x, y):
                self.balls[i].delete()
                self.balls.pop(i)

    def mouse_motion(self, x, y):
        """ При движении мышкой вызываем для танка (пока что единственного) его алгоритм прицеливания """
        self.tank.aim(x,     y)

    def game_over(self):
        for ball in self.balls:
            ball.delete()
        print("Конец игры!")
        self.tank.delete()


class Ball:
    density = 1.0  # стандартная плотность

    def __init__(self):
        self.r = randint(10, 30)
        self.m = self.density * math.pi * self.r ** 2  # Масса пропорциональна площади, т.е. квадрату радиуса.
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

    def step(self, dt):
        """ Сдвигает шарик ball в соответствии с его скоростью.
        """
        if self.oval_id is not None:
            Fx, Fy = self.force()
            ax = Fx / self.m
            ay = Fy / self.m

            self.x += self.Vx * dt + ax * dt ** 2 / 2
            self.y += self.Vy * dt + ay * dt ** 2 / 2
            self.Vx += ax * dt
            self.Vy += ay * dt

            if self.x + self.r >= canvas_width or self.x - self.r <= 0:
                self.Vx = -self.Vx
            if self.y + self.r >= canvas_height or self.y - self.r <= 0:
                self.Vy = -self.Vy
            canvas.coords(self.oval_id, (self.x - self.r, self.y - self.r,
                                         self.x + self.r, self.y + self.r))

    def force(self):
        Fx = 0
        Fy = self.m * 9.8  # default gravity
        return Fx, Fy

    def overlap(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2 <= self.r**2

    def intersect(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 <= (self.r + other.r)**2

    def collide(self, other):
        delta_r = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)**0.5
        ix = (other.x - self.x) / delta_r
        iy = (other.y - self.y) / delta_r
        Vself_normal = self.Vx*ix + self.Vy*iy
        Vother_normal = other.Vx * ix + other.Vy * iy
        self.Vx = self.Vx + (Vother_normal - Vself_normal) * ix
        self.Vy = self.Vy + (Vother_normal - Vself_normal) * iy
        other.Vx = other.Vx + (-Vother_normal + Vself_normal) * ix
        other.Vy = other.Vy + (-Vother_normal + Vself_normal) * iy


class Tank:
    """
    Танк, который умеет прицеливаться в заданную точку и порождать снаряды.
    """
    gun_length = 30
    turret_radius = 15

    def __init__(self, x, y, color):
        """
            x, y - точка центра турели
            dx, dy - вектор ствола танка
        """
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = -1
        self.turret_avatar = canvas.create_arc(self.x - self.turret_radius, self.y - self.turret_radius,
                                               self.x + self.turret_radius, self.y + self.turret_radius,
                                               start=0., extent=180, fill=color)
        x1, y1, x2, y2 = self._gun_xy()
        self.gun_avatar = canvas.create_line(x1, y1, x2, y2, width=5, fill=color)
        # TODO: закончить конструктор, продумать все свойства

    def _gun_xy(self):
        """
        :return: (x1, y1, x2, y2) экранные координаты начала и конца ствола пушки
        """
        x1 = self.x + self.dx * self.turret_radius
        y1 = self.y + self.dy * self.turret_radius
        x2 = self.x + self.dx * self.gun_length
        y2 = self.y + self.dy * self.gun_length
        return x1, y1, x2, y2

    def aim(self, x, y):
        """ Прицеливание ствола в сторону точки (x, y)"""
        r = ((x - self.x)**2 + (y - self.y)**2)**0.5
        self.dx = (x - self.x) / r
        self.dy = (y - self.y) / r
        x1, y1, x2, y2 = self._gun_xy()
        canvas.coords(self.gun_avatar, x1, y1, x2, y2)
        print("Типа прицеливаюсь в ({}, {}).".format(x, y))

    def fire(self, energy):
        """
        Стреляет снарядом, порождая новый объект типа "летящий снаряд".
        :param energy: Энергия выстрела - положительное дробное число.
        :return: Снаряд, который будет поражать цели.
        """
        pass  # TODO: пока снаряд не порождается.
        print("Типа выстрелили!")

    def delete(self):
        pass  # TODO: корректно удалять аватары танка с холста

# --------- GAME CONTROLLER: ----------
# Режим игры - игра идёт или нет
game_began = False
sleep_time = 50  # ms
scores = 0


def tick():
    time_label.after(sleep_time, tick)
    time_label['text'] = time.strftime('%H:%M:%S')
    if game_began:
        game.step()


def button_start_game_handler():
    global game_began
    if not game_began:
        game.start()
        game_began = True


def button_stop_game_handler():
    global game_began
    if game_began:
        game.stop()
        game_began = False


def canvas_click_handler(event):
    if game_began:
        game.click(event.x, event.y)


def canvas_mouse_motion_handler(event):
    if game_began:
        game.mouse_motion(event.x, event.y)

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
canvas.bind("<Button-1>", canvas_click_handler)
canvas.bind("<Motion>", canvas_mouse_motion_handler)

game = Game(default_initial_balls_number)

time_label.after_idle(tick)
root.mainloop()

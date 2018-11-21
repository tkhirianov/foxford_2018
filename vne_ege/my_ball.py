from graphics import *
from time import sleep

win_width = 512
win_height = 512

win = GraphWin("Картина graphics. Автор: Тимофей Фёдорович", win_width, win_height)

dx, dy = 1, 1
x, y = 100, 200
r = 20

ball = Circle(Point(x, y), r)
ball.setFill("brown")
ball.draw(win)

while True:
    x += dx
    y += dy
    ball.move(dx, dy)
    ball.setFill(color_rgb(x//2%256, y//2%256, 100))
    
    if x + r > win_width or x - r < 0:
        dx = -dx
    if y + r > win_height or y - r < 0:
        dy = -dy
    sleep(0.01)

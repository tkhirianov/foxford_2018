from graphics import *

win_width = 600
win_height = 500

def main():
    global win
    win = GraphWin("Картина graphics. Автор: Тимофей Фёдорович", win_width, win_height)
    draw_house(win_width//3, win_height*2//3, 150, 200)
    cursor_point = win.getMouse()
    win.close()


def draw_house(x0, y0, width, height):
    """
        Функция рисует дом в положении x0, y0 на холсте.
        x0, y0 - центральная нижняя точка домика
        width, height - ширина и высота.
    """
    foundation_height = int(0.1*height)
    walls_height = int(0.5*height)
    walls_width = int(0.9*width)
    roof_height = height - walls_height - foundation_height
    window_height, window_width = width//3, walls_height//3

    draw_foundation(x0, y0, width, foundation_height)
    draw_walls(x0, y0 - foundation_height, walls_width, walls_height)
    draw_roof(x0, y0 - foundation_height - walls_height, width, roof_height)
    draw_window(x0, y0 - foundation_height - walls_height//3,
                window_height, window_width)


def draw_foundation(x0, y0, width, height):
    foundation = Rectangle(Point(x0 - width//2, y0 - height), Point(x0 + width//2, y0))
    foundation.setWidth(3)
    foundation.setFill("brown")
    foundation.draw(win)
    print("Основание", x0, y0, width, height)

    
def draw_walls(x0, y0, width, height):
    walls = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    walls.setWidth(3)
    walls.setFill("gray")
    walls.draw(win)
    print("Стены", x0, y0, width, height)


def draw_roof(x0, y0, width, height):
    coordinates = [(x0-width//2, y0), (x0, y0-height), (x0+width//2, y0)]
    points = [Point(x, y) for x, y in coordinates]
    roof = Polygon(points)
    roof.setWidth(3)
    roof.setFill("darkred")
    roof.draw(win)
    print("Крыша", x0, y0, width, height)

    
def draw_window(x0, y0, width, height):
    window = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    window.setWidth(3)
    window.setFill("yellow")
    window.draw(win)
    print("Окно", x0, y0, width, height)



main()


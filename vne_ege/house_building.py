from graphics import *

win_width = 600
win_height = 500

def main():
    global win, house_elements
    win = GraphWin("Картина graphics. Автор: Тимофей Фёдорович", win_width, win_height)
    house_elements = draw_house(win_width//3, win_height*2//3, 150, 200)
    cursor_point = win.getMouse()
    for element in house_elements:
        element.move(50, 0)
    cursor_point = win.getMouse()
    for element in house_elements:
        element.move(0, 50)
    cursor_point = win.getMouse()
    win.close()


def draw_house(x0, y0, width, height):
    """
        Функция рисует дом в положении x0, y0 на холсте.
        x0, y0 - центральная нижняя точка домика
        width, height - ширина и высота.
        
        :return: список нарисованных объектов
    """
    foundation_height = int(0.1*height)
    walls_height = int(0.5*height)
    walls_width = int(0.9*width)
    roof_height = height - walls_height - foundation_height
    window_height, window_width = width//3, walls_height//3

    foundation = draw_foundation(x0, y0, width, foundation_height)
    walls = draw_walls(x0, y0 - foundation_height, walls_width, walls_height)
    roof = draw_roof(x0, y0 - foundation_height - walls_height, width, roof_height)
    house_window = draw_window(x0, y0 - foundation_height - walls_height//3,
                               window_height, window_width)
    return foundation + walls + roof + house_window

def draw_foundation(x0, y0, width, height):
    """
        Функция рисует основание в положении x0, y0 на холсте.
        x0, y0 - центральная нижняя точка основания.
        width, height - ширина и высота.
        
        :return: список нарисованных объектов
    """
    foundation = Rectangle(Point(x0 - width//2, y0 - height), Point(x0 + width//2, y0))
    foundation.setWidth(3)
    foundation.setFill("brown")
    foundation.draw(win)
    print("Основание", x0, y0, width, height)
    return [foundation]

    
def draw_walls(x0, y0, width, height):
    """
        Функция рисует стены в положении x0, y0 на холсте.
        x0, y0 - центральная нижняя точка стен.
        width, height - ширина и высота.
        
        :return: список нарисованных объектов
    """
    walls = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    walls.setWidth(3)
    walls.setFill("gray")
    walls.draw(win)
    print("Стены", x0, y0, width, height)
    return [walls]


def draw_roof(x0, y0, width, height):
    """
        Функция рисует крышу в положении x0, y0 на холсте.
        x0, y0 - центральная нижняя точка крыши.
        width, height - ширина и высота.
        
        :return: список нарисованных объектов
    """
    coordinates = [(x0-width//2, y0), (x0, y0-height), (x0+width//2, y0)]
    points = [Point(x, y) for x, y in coordinates]
    roof = Polygon(points)
    roof.setWidth(3)
    roof.setFill("darkred")
    roof.draw(win)
    print("Крыша", x0, y0, width, height)
    return [roof]

    
def draw_window(x0, y0, width, height):
    """
        Функция рисует окно в положении x0, y0 на холсте.
        x0, y0 - центральная нижняя точка окна.
        width, height - ширина и высота.
        
        :return: список нарисованных объектов
    """
    window = Rectangle(Point(x0-width//2, y0-height), Point(x0+width//2, y0))
    window.setWidth(3)
    window.setFill("yellow")
    window.draw(win)
    print("Окно", x0, y0, width, height)
    return [window]


main()


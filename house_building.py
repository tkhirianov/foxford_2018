from graphics import *

win_width = 600
win_height = 500

def main():
    draw_house(win_width//3, win_height*2//3, 150, 200)


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
    draw_walls(x0, y0-foundation_height, walls_width, walls_height)
    draw_roof(x0, y0 - walls_height, width, roof_height)
    draw_window(x0, y0 - foundation_height - walls_height//3,
                window_height, window_width)


def draw_foundation(x0, y0, width, height):
    pass
    print("Основание", x0, y0, width, height)

    
def draw_walls(x0, y0, width, height):
    pass
    print("Стены", x0, y0, width, height)


def draw_roof(x0, y0, width, height):
    pass
    print("Крыша", x0, y0, width, height)

    
def draw_window(x0, y0, width, height):
    pass
    print("Окно", x0, y0, width, height)

main()

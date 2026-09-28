# 실습 과제 진행
import math
from pico2d import *

open_canvas(800,600)
character = load_image('character.png')

def draw_shape_canvas(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def draw_top():
    for x in range(700, 100, -5):
        draw_shape_canvas(x, 500)

def draw_left():
    for y in range(500, 100, -5):
        draw_shape_canvas(100, y)

def draw_bottom():
    for x in range(100, 700, 5):
        draw_shape_canvas(x, 100)

def draw_right():
    for y in range(100, 500, 5):
        draw_shape_canvas(700, y)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_shape_canvas(x, y)
# -------------------------------------------------------------

def draw_leftside():
    for x in range(100, 400, 5):
        y = 500 - (x - 100) * 4 / 3
        draw_shape_canvas(x, y)

def draw_topside():
    for x in range(700, 100, -5):
        y = 500
        draw_shape_canvas(x, y)


def draw_rightside():
    for x in range(400, 700, 5):
        y = 100 + (x - 400) * 4 / 3
        draw_shape_canvas(x, y)


def move_rectangle():
    draw_top()
    draw_left()
    draw_bottom()
    draw_right()

def move_triangle():
    draw_topside()
    draw_leftside()
    draw_rightside()
    pass


while True:
    move_circle()
    # move_rectangle()
    # move_triangle()
    pass


close_canvas()
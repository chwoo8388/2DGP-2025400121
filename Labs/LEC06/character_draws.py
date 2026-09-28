# 실습 과제 진행
import math
from pico2d import *

open_canvas(800,600)
character = load_image('character.png')


def draw_top():
    for x in range(700, 100, -5):
        clear_canvas()
        character.draw(x, 500)
        update_canvas()
        delay(0.001)

def draw_left():
    for y in range(500, 100, -5):
        clear_canvas()
        character.draw(100, y)
        update_canvas()
        delay(0.001)

def draw_bottom():
    for x in range(100, 700, 5):
        clear_canvas()
        character.draw(x, 100)
        update_canvas()
        delay(0.001)

def draw_right():
    for y in range(100, 500, 5):
        clear_canvas()
        character.draw(700, y)
        update_canvas()
        delay(0.001)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.001)
# -------------------------------------------------------------
def draw_leftside():
    for x in range(400, 700, 5):
        y = 100 + (x - 400) * 4 / 3
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.001)
        
def draw_bottomside():
    # 아래 변 그리기
    pass
def draw_rightside():
    # 오른쪽 변 그리기
    pass


def move_rectangle():
    draw_top()
    draw_left()
    draw_bottom()
    draw_right()

def move_triangle():
    draw_leftside()
    draw_bottomside()
    draw_rightside()
    pass


while True:
    # move_circle()
    # move_rectangle()
    move_triangle()
    pass


close_canvas()
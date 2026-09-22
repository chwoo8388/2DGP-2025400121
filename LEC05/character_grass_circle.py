from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

center_x = 800 // 2
center_y = 600 // 2
radius = 200

angle = 0.0

while True:
    clear_canvas()
    
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    
    character.draw(x, y)
    update_canvas()
    
    angle += 0.03
    
    if angle >= 2 * math.pi:
        angle -= 2 * math.pi
        
    delay(0.01)

close_canvas()
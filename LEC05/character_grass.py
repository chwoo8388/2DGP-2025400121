from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 0, 90

# 1. 오른쪽으로 이동
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    print('x:', x, 'y:', y)
    x += 2
    delay(0.00)

# 2. 위로 이동
while y < 600:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    print('x:', x, 'y:', y)
    y += 2
    delay(0.00)

# 3. 왼쪽으로 이동
while x > 0:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    print('x:', x, 'y:', y)
    x -= 2
    delay(0.00)

# 4. 아래로 이동
while y > 90:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    print('x:', x, 'y:', y)
    y -= 2
    delay(0.00)

close_canvas()
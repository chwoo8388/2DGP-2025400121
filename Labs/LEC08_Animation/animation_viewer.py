from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_viewer_sheet_transparent.png')
frame = 0

for x in range(0, 800, 5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(
        frame * 182, 0,
        182, 182, x, 120,
    )
    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()

from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_viewer_sheet_transparent.png')
character2 = load_image('animation_viewer_walk_jump_sheet_transparent.png')
frame = 0

# for x in range(800, 0 , -5):
#     clear_canvas()
#     grass.draw(400, 30)
#     character.clip_draw(
#         frame * 182, 0,
#         182, 182, x, 120
#     )
#     update_canvas()

#     frame = (frame + 1) % 8
#     delay(0.01)

# for x in range(0, 800, 5):
#     clear_canvas()
#     grass.draw(400, 30)
#     character.clip_composite_draw(
#         frame * 182, 0,
#         182, 182, 0, 'h', x, 120, 182, 182,
#     )
#     update_canvas()

#     frame = (frame + 1) % 8
#     delay(0.01)

# for x in range(800, 395, -5):
#     clear_canvas()
#     grass.draw(400, 30)
#     character2.clip_composite_draw(
#         frame * 180, 0,
#         180, 180, 0, 'h', x, 120, 180, 180,
#     )
#     update_canvas()

#     frame = (frame + 1) % 8
#     delay(0.01)

for x in range(400, -5, -5):
    clear_canvas()
    grass.draw(400, 30)
    progress = (400 - x) / 400
    ground_y = 180
    y = ground_y + 180 * math.sin(math.pi * progress)
    jump_frame = min(int(progress * 12), 11)
    character2.clip_composite_draw(
        jump_frame * 120, 240,
        118, 240, 0, 'h', x, y, 120, 240,
    )
    update_canvas()
    delay(0.05)



close_canvas()

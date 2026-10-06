from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1080, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True

def handle_events():
    global running

    global x
    global y
    global facing_left

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                x = max(50, x - 5)
                facing_left = True
            elif event.key == SDLK_RIGHT:
                x = min(TUK_WIDTH - 50, x + 5)
                facing_left = False
            elif event.key == SDLK_UP:
                y = min(TUK_HEIGHT - 50, y + 5)
            elif event.key == SDLK_DOWN:
                y = max(50, y - 5)
            elif event.key == SDLK_ESCAPE:
                running = False

running = True
x = TUK_WIDTH // 2
y = 90
facing_left = False
frame = 0

# fill here
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if facing_left:
        character.clip_composite_draw(
            frame * 100, 100, 100, 100, 0, 'h', x, y, 100, 100
        )
    else:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
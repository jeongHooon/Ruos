import game_framework
from pico2d import *
import title_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(480, 420)
    image = load_image('title.png')


def exit():
    global image
    del(image)
    close_canvas()


def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(240, 210)
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_ENTER):
                game_framework.push_state(title_state)
    pass


def pause(): pass


def resume(): pass





import game_framework
from pico2d import *
import main_state
import main_state2
import main_state3
import main_state4


name = "PauseState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                game_framework.change_state(main_state)

def draw(frame_time):
    clear_canvas()
    image.draw(240, 210)
    update_canvas()

def update(frame_time):
    pass

def pause():
    pass


def resume():
    pass







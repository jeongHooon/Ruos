import random
import json
import os
import game_framework
from pico2d import *
import title_state
import main_state
import main_state2
import main_state3
import main_state4
import ranking_state


name = "Score_state"
image = None
logo_time = 0.0


def enter():
    global image, life, now_pos
    f = open('life.txt', 'r')
    life = json.load(f)
    f.close()



    now_pos = load_font("lazy_sunday_regular.ttf", 20)
    image = load_image('blackboard.png')


def exit():
    global image, life, now_pos
    result = (1000 * life['life'] + 3000 - 10 * life['time'])

    f = open('ranking_data.txt', 'r')
    score = json.load(f)
    f.close()

    score.append({'time': life['time'], 'life': life['life'], 'score': result})
    f = open('ranking_data.txt', 'w')
    json.dump(score, f)
    f.close()
    del(image)
    del(life)
    del(now_pos)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                game_framework.change_state(title_state)

def draw(frame_time):
    clear_canvas()
    image.draw(240, 210)

    now_pos.draw(205, 300, 'Life : %d' % life['life'], (200, 0, 100))
    now_pos.draw(160, 250, 'Play Time : %d min %d sec ' % (life['time'] / 60, life['time'] % 60), (200, 0, 100))
    now_pos.draw(100, 200, '1000 * %d + 3000 - (%d * 10) = %d' % (life['life'], life['time'],1000*life['life']+ 3000 - 10*life['time']), (200, 0, 100))
    now_pos.draw(190, 150, 'SCORE : %d' % (1000 * life['life'] + 3000 - 10 * life['time']), (200, 0, 100))
    update_canvas()

def update(frame_time):
    pass

def pause():
    pass


def resume():
    pass







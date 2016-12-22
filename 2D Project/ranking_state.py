import random
import json
import os
import game_framework
from pico2d import *

import title_state
import score_state
name = "RankingState"
image = None

def enter():
    global image, font
    font = load_font("lazy_sunday_regular.ttf", 20)
    image = load_image('blackboard.png')

def exit():
    global image, font
    del(image)
    del(font)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                    game_framework.quit(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                    game_framework.change_state(score_state)



def update(frame_time):
    pass

def bubble_sort(data_list):
    for i in range(0, len(data_list)):
        for j in range(i + 1, len(data_list)):
            if data_list[i]['score'] < data_list[j]['score']:
                data_list[i], data_list[j] = data_list[j], data_list[i]
def draw_ranking():
    def print_score(score):
        font.draw(200, score*50,"Time :%4.1f, Life :%3d, Score :%3d" % (score['time'], score['life'], score['score']))
    f = open('ranking_data.txt', 'r')
    score_data = json.load(f)
    f.close()
    bubble_sort(score_data)
    score_data = score_data[:10]

    y=0
    for score in score_data:
        font.draw(100, 370 - y*30, "Time :%4.1f, Life :%3d, Score :%3d" % (score['time'], score['life'], score['score']),(255,255,255))
        y = y+1




def draw(frame_time):
    global image, font
    clear_canvas()
    image.draw(400, 300)
    font.draw(200, 400,'[RANKING]', (255, 0, 0))
    draw_ranking()




    draw_ranking()
    update_canvas()




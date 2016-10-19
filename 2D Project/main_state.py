import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state2
import main_state3

name = "MainState"

boy = None
grass = None
background = None
font = None


class Background:
    x = 1710
    def __init__(self):
        self.image = load_image('background1.png')
        self.obtacle = load_image('bottom.png')
        self.ob1x = 0
        self.ob2x = 0
        self.ob3x = 0
        self.rock = False
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)

    def update(self):
        if Background.x == -1230:
            game_framework.change_state(main_state3)
        elif self.rock == False:
            Background.x -= 1

    def draw(self):
        self.image.clip_draw(0, 0, 3425, 850, Background.x, 0)
        self.now_pos.draw(400, 400,'%d' % Background.x , (200, 0, 100))
        if Background.x < 1000:
            self.obtacle.draw(240 - self.ob1x, 200)
            if self.rock == False:
                self.ob1x += 1
        if Background.x < 240:
            self.obtacle.draw(240 - self.ob2x, 200)
            if self.rock == False:
                self.ob2x += 1
        if Background.x < -500:
            self.obtacle.draw(240 - self.ob3x, 200)
            if self.rock == False:
                self.ob3x += 1
    def control(self,key):
        if key == 'LEFT':
            self.rock = True
        elif key == 'RIGHT':
            self.rock = False

class Grass:
    def __init__(self):
        self.image = load_image('bottom.png')
        self.frame = 0

    def update(self):
        pass

    def draw(self):
        while(self.frame < 16):
            self.image.draw(self.frame * 30 + 15, 15)
            self.frame += 1
        self.frame = self.frame % 16



class Boy:
    def __init__(self):
        self.x, self.y = 0, 60
        self.frame = 0
        self.jump = False
        self.djump = False
        self.jumprock = False
        self.jumpdir1 = 0
        self.jumpdir2 = 0
        self.Rstate = False
        self.Lstate = False
        self.image = load_image('player2.png')

        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        #좌우이동
        if self.Rstate == True:
            if self.x == 240:
                background.control('RIGHT')
                background.update()
            else :
                self.x += 1
        elif self.Lstate == True:
            self.x -= 1
        # 점프
        if self.jump == True:
            self.jumpdir1 += 2
            if self.djump == True:
                self.jump = False
            if self.jumpdir1 > 100:
                self.jump = False
        elif self.jumpdir2 == 0:
            self.jumpdir1 -= 2
            if self.jumpdir1 < 0:
                self.jumpdir1 = 0
                self.jumprock = False
        if self.djump == True:
            self.jumpdir2 += 2
            if self.jumpdir2 > 100:
                self.djump = False
        else :
            self.jumpdir2 -= 2
            if self.jumpdir2 < 0:
                self.jumpdir2 = 0
        delay(0.01)

    def event(self, key):
        if key == 'LEFT':
            self.Lstate = True
        elif key == 'RIGHT':
            self.Rstate = True
            #self.x += 5
        elif key == 'SPACE':
            if self.djump == False and self.jumpdir2 == 0 and self.jumprock == False:
                self.jump = True
                if self.jump == True and self.jumpdir1 > 0:
                        self.djump = True
                        self.jumprock = True
        elif key == 'RCANCLE':
            self.Rstate = False
            background.control('LEFT')
        elif key == 'LCANCLE':
            self.Lstate = False

    def draw(self):
        if self.jumpdir1 :
            self.image.clip_draw(208, 832, 32, 48, self.x, self.y + self.jumpdir1 + self.jumpdir2)
        else:
            self.image.clip_draw(16 + self.frame * 64, 896, 32, 48, self.x, self.y + self.jumpdir1 + self.jumpdir2)



def enter():
    global boy, grass, background
    background = Background()
    boy = Boy()
    grass = Grass()


def exit():
    global boy, grass, background
    del(background)
    del(boy)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            game_framework.change_state(main_state3)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                boy.event('SPACE')
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                boy.event('LEFT')
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                boy.event('RIGHT')
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                boy.event('RCANCLE')
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                boy.event('LCANCLE')
        #elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #game_framework.change_state(main_state3)


def update():
    #grass.update()
    boy.update()


def draw():
    clear_canvas()
    background.draw()
    #grass.draw()
    boy.draw()
    update_canvas()






import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state4

name = "MainState2"

boy = None
grass = None
background = None
object = None
font = None


class Background:
    x = 1710
    def __init__(self):
        self.image = load_image('background2.png')
        self.rock = False
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)
        self.obtacle = load_image('Obtacle1.png')
        self.ob1x = 0
        self.ob2x = 0
        self.ob3x = 0
        self.ob4x = 0
    def update(self):
        if Background.x == -1230:
            game_framework.change_state(main_state4)
        else:
            Background.x -= 1
            object.control()
    def draw(self):

        self.image.clip_draw(0, 0, 3425, 580, Background.x, 135)
        self.now_pos.draw(400, 400, '%d' % Background.x, (200, 0, 100))

        if Background.x < 800:
            self.obtacle.draw(240 - self.ob2x, 150)
            if self.rock == False:
                self.ob2x += 1
        if Background.x < -950:
            self.obtacle.draw(240 - self.ob3x, 200)
            if self.rock == False:
                self.ob3x += 1
    def control(self,key):
        if key == 'LEFT':
            self.rock = True
        elif key == 'RIGHT':
            self.rock = False

class Object:
    def __init__(self):
        self.ob = load_image('Obtacle1.png')
        self.ob1 = load_image('Obtacle5.png')

        self.ob1x, self.ob1y = 350, 200

    def update(self):
        pass


    def draw(self):

        if background.x <= 1600:
            self.ob.draw(self.ob1x, self.ob1y)
        else:
            self.ob1.draw(self.ob1x, self.ob1y)

    def control(self):
        self.ob1x -= 1



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
        if self.Rstate:
            if self.x == 240:
                background.control('RIGHT')
                background.update()
            else :
                self.x += 1
        elif self.Lstate:
            self.x -= 1
        if self.jump:
            self.jumpdir1 += 3
            if self.djump:
                self.jump = False
            if self.jumpdir1 > 100:
                self.jump = False
        elif self.jumpdir2 == 0:
            self.jumpdir1 -= 3
            if self.jumpdir1 < 0:
                self.jumpdir1 = 0
                self.jumprock = False
        if self.djump:
            self.jumpdir2 += 3
            if self.jumpdir2 > 100:
                self.djump = False
        else :
            self.jumpdir2 -= 3
            if self.jumpdir2 < 0:
                self.jumpdir2 = 0
        delay(0.01)

    def handle_events(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.Lstate = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.Rstate = True
            #self.x += 5
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.djump == False and self.jumpdir2 == 0 and self.jumprock == False:
                self.jump = True
                if self.jump == True and self.jumpdir1 > 0:
                        self.djump = True
                        self.jumprock = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.Rstate = False
            background.control('LEFT')
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.Lstate = False

    def draw(self):
        if self.jumpdir1 :
            self.image.clip_draw(208, 832, 32, 48, self.x, self.y + self.jumpdir1 + self.jumpdir2)
        else:
            self.image.clip_draw(16 + self.frame * 64, 896, 32, 48, self.x, self.y + self.jumpdir1 + self.jumpdir2)




def enter():
    global boy, grass, background, object
    background = Background()
    boy = Boy()

    object = Object()


def exit():
    global boy, grass, background, object
    del(background)
    del(boy)
    del(grass)
    del(object)


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
            game_framework.change_state(main_state4)
        else:
            boy.handle_events(event)
        #elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #game_framework.change_state(main_state3)


def update():
    boy.update()


def draw():
    clear_canvas()
    background.draw()
    object.draw()
    boy.draw()
    update_canvas()






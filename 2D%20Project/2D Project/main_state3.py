import random
import json
import os

from pico2d import *

import game_framework
import title_state
#import main_state2
#import main_state3

name = "MainState3"

boy = None
grass = None
background = None
object = None
font = None


class Background:
    x = 1710
    def __init__(self):
        self.image = load_image('background3.png')
        self.rock = False
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)
        self.obtacle = load_image('Obtacle2.png')
        self.ob1x = 0
        self.ob1y = 70
        self.ob2x = 0
        self.ob2y = 70
        self.ob3x = 0
        self.ob3y = 70
        self.ob4x = 0
    def update(self):
        if Background.x == -1230:
            pass
        else:
            Background.x -= 1
            object.control()
    def draw(self):

        self.image.clip_draw(0, 0, 3425, 580, Background.x, 135)
        self.now_pos.draw(400, 400, '%d' % Background.x, (200, 0, 100))
        if Background.x < 1660:
            self.obtacle.draw(240 - self.ob1x, self.ob1y)
            self.ob1y += 2
            if self.rock == False:
                self.ob1x += 1

        if Background.x < -900:
            self.obtacle.draw(240 - self.ob2x, self.ob2y)
            self.ob2y += 2
            if self.rock == False:
                self.ob2x += 1

        if Background.x < -800:
            self.obtacle.draw(240 - self.ob3x, self.ob3y)
            self.ob3y += 2
            if self.rock == False:
                self.ob3x += 1

    def control(self,key):
        if key == 'LEFT':
            self.rock = True
        elif key == 'RIGHT':
            self.rock = False
class Object:
    def __init__(self):
        self.ob = load_image('Obtacle3.png')
        self.i = 0
        self.num = 100

        self.cx1, self.cy1 = 790, 240

        self.ob1x, self.ob1y = 0, 0
        self.ob1delta = 2.0 * math.pi / self.num
        self.ob1r = 20

        self.ob2x, self.ob2y = 0, 0
        self.ob2delta = 2.0 * math.pi / self.num
        self.ob2r = 50

        self.cx2, self.cy2 = 1285, 240

        self.ob3x, self.ob3y = 0, 0
        self.ob3delta = 2.0 * math.pi / self.num
        self.ob3r = 20

        self.ob4x, self.ob4y = 0, 0
        self.ob4delta = 2.0 * math.pi / self.num
        self.ob4r = 50

    def update(self):
        self.ob1delta = 2.0 * math.pi / self.num
        self.ob1x = self.cx1 + (self.ob1r * math.cos(self.ob1delta * self.i))
        self.ob1y = self.cy1 + (self.ob1r * math.sin(self.ob1delta * self.i))

        self.ob2delta = 2.0 * math.pi / self.num
        self.ob2x = self.cx1 + (self.ob2r * math.cos(self.ob2delta * self.i))
        self.ob2y = self.cy1 + (self.ob2r * math.sin(self.ob2delta * self.i))

        self.ob3delta = 2.0 * math.pi / self.num
        self.ob3x = self.cx2 + (self.ob3r * math.cos(self.ob3delta * self.i))
        self.ob3y = self.cy2 + (self.ob3r * math.sin(self.ob3delta * self.i))

        self.ob4delta = 2.0 * math.pi / self.num
        self.ob4x = self.cx2 + (self.ob4r * math.cos(self.ob4delta * self.i))
        self.ob4y = self.cy2 + (self.ob4r * math.sin(self.ob4delta * self.i))


        self.i = self.i + 1
        if self.i == 100:
            self.i = 0
    def draw(self):
        self.ob.draw(self.ob1x, self.ob1y)
        self.ob.draw(self.ob2x, self.ob2y)
        self.ob.draw(self.ob3x, self.ob3y)
        self.ob.draw(self.ob4x, self.ob4y)
    def control(self):
        self.cx1 -= 1
        self.cx2 -= 1
class Boy:
    def __init__(self):
        self.x, self.y = 0, 150
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
        if self.Rstate == True:
            if self.x == 240:
                background.control('RIGHT')
                background.update()
            else :
                self.x += 1
        elif self.Lstate == True:
            self.x -= 1
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
    object.update()


def draw():
    clear_canvas()
    background.draw()
    #grass.draw()
    boy.draw()
    object.draw()
    update_canvas()






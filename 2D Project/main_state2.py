import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state4
import pause_state
import score_state
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
    def update(self,frame_time):
        if Background.x == -1230:
            game_framework.change_state(main_state4)
        else:
            Background.x -= 1
            object.control()
    def draw(self):

        self.image.clip_draw(0, 0, 3425, 580, Background.x, 135)
        self.now_pos.draw(400, 400, '%d' % Background.x, (200, 0, 100))

        if Background.x < 800 and Background.x > -1200:
            self.obtacle.draw(240 - self.ob2x, 150)
            if self.rock == False:
                self.ob2x += 1
        if Background.x < -950 and Background.x > -1200:
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
        pass
        if background.x <= 1600 and Background.x > -1200:
            self.ob.draw(self.ob1x, self.ob1y)
        elif Background.x > -1200:
            self.ob1.draw(self.ob1x, self.ob1y)

    def control(self):
        self.ob1x -= 1



class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3
    def __init__(self):
        self.x, self.y = 0, 60
        self.frame = 0
        self.colideX = 0
        self.jump = False
        self.djump = False
        self.jumprock = False
        self.jumpdir1 = 0
        self.jumpdir2 = 0
        self.Rstate = False
        self.Lstate = False
        self.image = load_image('player2.png')
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.dropY = 60
        self.climb = 0
        self.state = self.RIGHT_STAND
        f = open('life.txt', 'r')
        self.life = json.load(f)
        f.close()
        self.life_time = self.life['time']
        self.life_count = self.life['life']
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time

        self.frame = int(self.total_frames) % 8
        # 좌우이동
        if self.state == self.RIGHT_RUN:
            if self.x >= 240:
                background.control('RIGHT')
                self.colideX += 1
                background.update(frame_time)
            else:
                self.x += (self.dir * distance)
                self.colideX += 1
        elif self.state == self.LEFT_RUN:
            self.x += (self.dir * distance)
            self.colideX -=1

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
        if self.colideX >=210 and self.colideX <= 2550 and self.y <= 150:
            self.dropY -= 3

        elif self.y <=0:
            self.dropY = 150
            self.life_count -= 1
        if self.life_count == 0:
            game_framework.change_state(score_state)
        self.y = self.dropY + self.climb + self.jumpdir1 + self.jumpdir2
        delay(0.01)

    def clear_jump(self):
        self.jumpdir1 = 0
        self.jumpdir2 = 0
        self.jumprock = False
        self.djump = False
        self.jump = False
    def handle_events(self, event, frame_time):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN):
                self.state = self.LEFT_RUN
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN):
                self.state = self.RIGHT_RUN
                background.control('LEFT')
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_F8):
            self.life_count -= 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_F9):
            self.life_time += 60
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_F10):
            Background.x = -1200
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.djump == False and self.jumpdir2 == 0 and self.jumprock == False:
                self.jump = True
                if self.jump == True and self.jumpdir1 > 0:
                        self.djump = True
                        self.jumprock = True


    def draw(self, frame_time):
        self.now_pos.draw(400, 300, '%d' % self.colideX, (200, 0, 100))
        if self.jumpdir1 :
            self.image.clip_draw(208, 832, 32, 48, self.x, self.y)
        else:
            self.image.clip_draw(16 + self.frame * 64, 896, 32, 48, self.x, self.y)
        self.now_pos.draw(170, 400, 'life : %d' % self.life_count, (200, 0, 100))
        self.now_pos.draw(250, 400, 'time : %d' % self.life_time, (200, 0, 100))


def enter():
    global boy, background, object
    background = Background()
    boy = Boy()

    object = Object()


def exit():
    global boy,background, object
    f = open('life.txt', 'w')
    json.dump({'time': boy.life_time, 'life': boy.life_count}, f)
    f.close()
    del(background)
    del(boy)
    del(object)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            game_framework.change_state(main_state4)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            game_framework.change_state(pause_state)
        else:
            boy.handle_events(event,frame_time)


def update(frame_time):
    boy.update(frame_time)


def draw(frame_time):
    clear_canvas()
    background.draw()
    object.draw()
    boy.draw(frame_time)
    update_canvas()






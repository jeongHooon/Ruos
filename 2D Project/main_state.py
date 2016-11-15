import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state2
import main_state3
import pause_state
import score_state

name = "MainState"

boy = None
background = None
object = None
font = None

class Background:
    x = 1710
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        self.image = load_image('background1.png')
        self.obtacle = load_image('bottom.png')
        self.obtacle1 = load_image('Obtacle5.png')
        self.ob1x = 0
        self.ob2x = 0
        self.ob3x = 0
        self.ob4x = 0
        self.rock = False
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)

    def update(self,frame_time):
        self.life_time += frame_time
        distance = Background.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        if Background.x == -1230:
            game_framework.change_state(main_state3)
        elif self.rock == False:
            Background.x -= 1
            object.control()

    def draw(self,frame_time):
        self.image.clip_draw(0, 0, 3425, 850, Background.x, 0)
        self.now_pos.draw(400, 400,'%d' % Background.x , (200, 0, 100))
        """
        if Background.x < 1000:
            self.obtacle.draw(240 - self.ob1x, 200)
            if self.rock == False:
                self.ob1x += 1*frame_time
        if Background.x < 240:
            self.obtacle.draw(240 - self.ob2x, 220)
            if self.rock == False:
                self.ob2x += 1
        if Background.x < -500:
            self.obtacle.draw(240 - self.ob3x, 200)
            if self.rock == False:
                self.ob3x += 1
"""

    def control(self,key):
        if key == 'LEFT':
            self.rock = True
        elif key == 'RIGHT':
            self.rock = False

class Object:
    def __init__(self):
        self.ob = load_image('Obtacle1.png')
        self.ob1 = load_image('Obtacle5.png')

        self.ob1x, self.ob1y = 2280, 200

    def update(self):
        pass

    def draw(self):
        if background.x <= -330:
            self.ob.draw(self.ob1x, self.ob1y)
        else:
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
        self.jump = False
        self.djump = False
        self.jumprock = False
        self.jumpdir1 = 0
        self.jumpdir2 = 0
        self.dropY = 60
        self.climb = 0
        self.colideX = 1710
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0

        self.life_count = 10
        self.state = self.RIGHT_STAND
        self.image = load_image('player2.png')
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)




    def update(self, frame_time):

        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time

        self.frame = int(self.total_frames) % 8

        #좌우이동
        if self.state == self.RIGHT_RUN:
            if self.x >= 240:
                background.control('RIGHT')
                background.update(frame_time)
                self.colideX -= 1
            else :
                self.x += (self.dir * distance)
        else:
            self.x += (self.dir * distance)
        #elif self.Lstate:
            #self.x -= 1
        # 점프
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
        else:
            self.jumpdir2 -= 3
            if self.colideX <= 1630 and self.colideX >= 1620 and self.y < 100:
                self.climb = 30
                boy.clear_jump()
            else:
                if self.climb >= 0:
                    self.climb -= 1
            if self.jumpdir2 < 0:
                self.jumpdir2 = 0

        if self.colideX <= 1636 and self.colideX >= 1542 and self.y < 70:
            self.x -= (self.dir * distance)
        elif self.colideX <= 1620 and self.colideX >= 1542 and self.y < 100:
            self.x -= (self.dir * distance)
        elif self.colideX <= 470 and self.colideX >= 418 and self.y <= 60:
            self.dropY -= 1
        elif self.colideX <= 242 and self.colideX >= 212 and self.y <= 60:
            self.dropY -= 1
        elif self.colideX <= -283 and self.colideX >= -315 and self.y <= 60:
            self.dropY -= 1
        elif self.colideX <= -494 and self.colideX >= -505 and self.y <= 60:
            self.dropY -= 1
        elif self.y <=0:
            self.dropY = 60
            self.life_count -= 1
        if self.life_count == 0:
            game_framework.change_state(score_state)

        self.y = self.dropY + self.climb + self.jumpdir1 + self.jumpdir2



        #self.life_count.append(self.life_count)


        delay(0.01)

    def clear_jump(self):
        self.jumpdir1 = 0
        self.jumpdir2 = 0
        self.jumprock = False
        self.djump = False
        self.jump = False
    def handle_events(self, frame_time,event):
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
            self.life_count -= 9
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

    def draw(self,frame_time):
        if self.jumpdir1 :
            self.image.clip_draw(208, 832, 32, 48, self.x, self.y )
        else:
            self.image.clip_draw(16 + self.frame * 64, 896, 32, 48, self.x, self.y )
        self.now_pos.draw(200, 400, '%d' % self.life_count, (200, 0, 100))
        self.now_pos.draw(250, 400, '%d' % self.life_time, (200, 0, 100))

def enter():
    global boy, background, object
    background = Background()
    boy = Boy()
    object = Object()

def exit():
    global boy, background, object


    f = open('life.txt', 'w')
    json.dump({'time':boy.life_time, 'life':boy.life_count}, f)
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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            game_framework.change_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            game_framework.change_state(main_state3)
        else:
            boy.handle_events(frame_time, event)

def update(frame_time):

    boy.update(frame_time)

def draw(frame_time):
    clear_canvas()
    background.draw(frame_time)
    boy.draw(frame_time)
    object.draw()
    update_canvas()







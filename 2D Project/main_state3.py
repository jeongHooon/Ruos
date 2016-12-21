import random
import json
import os

from pico2d import *

object_data_file = open('object3.txt', 'r')
object_data = json.load(object_data_file)
object_data_file.close()

bottom_data_file = open('object4.txt', 'r')
bottom_data = json.load(bottom_data_file)
bottom_data_file.close()

import game_framework
import title_state
import main_state2
#import main_state3
import pause_state
import score_state
name = "MainState3"

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
    next_stage = False
    def __init__(self):
        self.image = load_image('background3.png')
        self.rock = False
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)
        self.obtacle = load_image('Obtacle2.png')
        self.obtacle1 = load_image('Obtacle4.png')
        self.ob1x = 0
        self.ob1y = 70
        self.ob2x = 0
        self.ob2y = 70
        self.ob3x = 0
        self.ob3y = 70
        self.ob4x = 0
        self.ob4y = 70
        self.ob5x = 0
        self.ob5y = 170
        self.life_time = 0.0
        self.total_frames = 0.0
        self.bgm = load_music("BGM/dungeon.mp3")
        self.bgm.set_volume(60)
        self.bgm.repeat_play()

    def update(self,frame_time):
        self.life_time += frame_time
        distance = Background.RUN_SPEED_PPS * frame_time
        self.total_frames += Background.FRAMES_PER_ACTION * Background.ACTION_PER_TIME * frame_time
        if Background.x < -1230:
            self.next_stage = True
        elif not self.rock and Background.x > -1230:
            Background.x -= 1*distance
            for ob in object:
                ob.control(frame_time)
    def draw(self):

        self.image.clip_draw(0, 0, 3425, 580, Background.x, 135)
        #self.now_pos.draw(400, 400, '%d' % Background.x, (200, 0, 100))


        if Background.x < 1660 and Background.x > -1200:
            self.obtacle.draw(240 - self.ob1x, self.ob1y)
            self.ob1y += 7
            if self.rock == False:
                self.ob1x += 1

        if Background.x < -800 and Background.x > -1200:
            self.obtacle.draw(240 - self.ob2x, self.ob2y)
            self.ob2y += 7
            if self.rock == False:
                self.ob2x += 1

        if Background.x < -900 and Background.x > -1200:
            self.obtacle.draw(240 - self.ob3x, self.ob3y)
            self.ob3y += 7
            if self.rock == False:
                self.ob3x += 1
        if Background.x < -1000 and Background.x > -1200:
            self.obtacle.draw(240 - self.ob4x, self.ob4y)
            self.ob4y += 7
            if self.rock == False:
                self.ob4x += 1
        if Background.x < -520 and Background.x > -1200:
            self.obtacle1.draw(480 - self.ob5x, self.ob5y)
            self.ob5x += 10
    def collid(self):
        self.rock = True
    def not_collid(self):
        self.rock = False

    def control(self,key):
        if key == 'LEFT':
            self.rock = True
        elif key == 'RIGHT':
            self.rock = False
class Object:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    def __init__(self):
        self.ob = load_image('Obtacle3.png')
        self.i = 0
        self.num = 100
        self.life_time = 0.0
        self.total_frames = 0.0
        self.cx, self.cy = 0,0
        self.obx, self.oby = 0, 0
        self.ob1delta = 2.0 * math.pi / self.num
        self.obr = 0


    def create(self):
        object = []
        for name in object_data:
            ob = Object()
            ob.cx = object_data[name]['cx']
            ob.cy = object_data[name]['cy']
            ob.obr = object_data[name]['obr']
            """
            ob.left = object_data[name]['left']
            ob.right = object_data[name]['right']
            ob.bottom = object_data[name]['bottom']
            ob.top = object_data[name]['top'] """
            object.append(ob)

        return object

    def get_bb(self):
        return self.obx-15, self.oby-10, self.obx+10, self.oby+10

    def update(self):
        self.ob1delta = 2.0 * math.pi / self.num
        self.obx = self.cx + (self.obr * math.cos(self.ob1delta * self.i))
        self.oby = self.cy + (self.obr * math.sin(self.ob1delta * self.i))

        self.i = self.i + 1
        if self.i == 100:
            self.i = 0

    def draw(self):
        #draw_rectangle(*self.get_bb())
        self.ob.draw(self.obx, self.oby)

    def control(self,frame_time):
        self.life_time += frame_time
        distance = Object.RUN_SPEED_PPS * frame_time
        self.total_frames += Object.FRAMES_PER_ACTION * Object.ACTION_PER_TIME * frame_time
        self.cx -= 1 * distance
class Object:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    def __init__(self):
        self.ob = load_image('Obtacle3.png')
        self.i = 0
        self.num = 100
        self.life_time = 0.0
        self.total_frames = 0.0
        self.cx, self.cy = 0,0
        self.obx, self.oby = 0, 0
        self.ob1delta = 2.0 * math.pi / self.num
        self.obr = 0


    def create(self):
        object = []
        for name in object_data:
            ob = Object()
            ob.cx = object_data[name]['cx']
            ob.cy = object_data[name]['cy']
            ob.obr = object_data[name]['obr']
            """
            ob.left = object_data[name]['left']
            ob.right = object_data[name]['right']
            ob.bottom = object_data[name]['bottom']
            ob.top = object_data[name]['top'] """
            object.append(ob)

        return object

    def get_bb(self):
        return self.obx-15, self.oby-10, self.obx+10, self.oby+10

    def update(self):
        self.ob1delta = 2.0 * math.pi / self.num
        self.obx = self.cx + (self.obr * math.cos(self.ob1delta * self.i))
        self.oby = self.cy + (self.obr * math.sin(self.ob1delta * self.i))

        self.i = self.i + 1
        if self.i == 100:
            self.i = 0

    def draw(self):
        #draw_rectangle(*self.get_bb())
        self.ob.draw(self.obx, self.oby)

    def control(self,frame_time):
        self.life_time += frame_time
        distance = Object.RUN_SPEED_PPS * frame_time
        self.total_frames += Object.FRAMES_PER_ACTION * Object.ACTION_PER_TIME * frame_time
        self.cx -= 1 * distance


class Bottom:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        self.life_time = 0.0
        self.total_frames = 0.0

        self.left = 0
        self.right = 0
        self.bottom = 0
        self.top = 0

    def update(self, frame_time):
        pass

    def create(self):
        bottom = []
        for name in bottom_data:
            bo = Bottom()
            bo.left = bottom_data[name]['left']
            bo.right = bottom_data[name]['right']
            bo.bottom = bottom_data[name]['bottom']
            bo.top = bottom_data[name]['top']
            bottom.append(bo)
        return bottom

    def draw(self):
        pass
        #draw_rectangle(self.left, self.bottom, self.right, self.top)

    def control(self, frame_time):
        self.life_time += frame_time
        distance = Object.RUN_SPEED_PPS * frame_time
        self.total_frames += Object.FRAMES_PER_ACTION * Object.ACTION_PER_TIME * frame_time
        self.left -= 1 * distance
        self.right -= 1 * distance

    def get_bb(self):
        return self.left, self.bottom, self.right, self.top


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
        self.x, self.y = 0, 150
        self.colideX = 1710
        self.frame = 0
        self.drop = False
        self.jump = False
        self.djump = False
        self.jumprock = False
        self.fall_state = False
        self.collid_state = False
        self.collid_stack = 0
        self.jumpdir1 = 0
        self.jumpdir2 = 0
        self.minY = 0
        self.dropY=150
        self.climb = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.state = self.RIGHT_STAND
        self.over_count =0
        f = open('life.txt', 'r')
        self.life = json.load(f)
        f.close()
        self.life_time = self.life['time']
        self.life_count = self.life['life']
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)
        self.image = load_image('player2.png')
        self.jump_sound = load_wav('SE/jump.wav')
        self.jump_sound.set_volume(50)
        self.gameover_sound = load_wav('SE/gameover.wav')
        self.gameover_sound.set_volume(50)

    def update(self,frame_time):
        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time

        self.frame = int(self.total_frames) % 8
        if self.over_count == 0:
            if self.state == self.RIGHT_RUN:
                if self.x >= 240:
                    background.control('RIGHT')
                    background.update(frame_time)
                    self.colideX -= 1 * distance
                else:
                    if not self.fall_state:
                        self.x += (self.dir * distance)
            else:
                if not self.fall_state:
                    self.x += (self.dir * distance)

        if self.jump:
            self.jumpdir1 += 3
            if self.djump:
                self.jump = False
            if self.jumpdir1 > 100:
                self.jump = False
                self.fall_state = True
        elif self.fall_state and not self.djump and self.jumpdir2 == 0:
            self.jumpdir1 -= 3

            if self.jumpdir1 < 0:
                self.jumpdir1 = 0
                self.jumprock = False
        if self.djump:
            self.jumpdir2 += 3
            if self.jumpdir2 > 100:
                self.djump = False
        else:
            if self.fall_state:
                self.jumpdir2 -= 3
                if self.jumpdir2 < 0:
                    self.jumpdir2 = 0
        if self.fall_state and self.jumpdir2 == 0 and self.jumpdir1 == 0:
            #self.dropY -= 3
            if self.dropY < self.minY:
                self.dropY = self.minY
        if self.colideX <= 470 and self.colideX >= 418 and self.y <= 60:
            self.dropY -= 3
        elif self.colideX <= 242 and self.colideX >= 212 and self.y <= 60:
            self.dropY -= 3
        elif self.colideX <= -283 and self.colideX >= -315 and self.y <= 60:
            self.dropY -= 3
        elif self.colideX <= -494 and self.colideX >= -505 and self.y <= 60:
            self.dropY -= 3
        elif self.y <= 0:
            self.dropY = 150
            self.life_count -= 1
        if self.life_count == 0:
            self.gameover_sound.play()
            self.over_count += 1
            if self.over_count == 300:
                game_framework.change_state(score_state)

        self.y = self.dropY + self.jumpdir1 + self.jumpdir2

        # few second immune collid
        if self.collid_state:
            self.collid_stack += 1
            if self.collid_stack > 100:
                self.collid_stack = 0
                self.collid_state = False

        delay(0.01)

    def clear_jump(self):
        self.jumpdir1 = 0
        self.jumpdir2 = 0
        self.jumprock = False
        self.djump = False
        self.jump = False

    def clear_fall(self):
        if not self.jump and not self.djump:
            self.fall_state = True
            self.minY = 150

    def handle_events(self, event,frame_time):
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
                self.jump_sound.play()
                self.jump = True
                if self.jump == True and self.jumpdir1 > 0:
                        self.djump = True
                        self.jumprock = True

    def draw(self):
        #self.now_pos.draw(400, 300, '%d' % self.colideX, (200, 0, 100))
        #self.draw_bb()
        if self.jumpdir1 :
            self.image.clip_draw(208, 832, 32, 48, self.x, self.y )
        else:
            self.image.clip_draw(16 + self.frame * 64, 896, 32, 48, self.x, self.y)
        self.now_pos.draw(170, 400, 'life : %d' % self.life_count, (200, 0, 100))
        self.now_pos.draw(250, 400, 'time : %d' % self.life_time, (200, 0, 100))

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 10, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def collid_object(self):
        if not self.collid_state and self.over_count == 0:
            self.life_count -= 1
            self.collid_state = True

    def reset(self):
        pass

    def fall(self):
        if not self.jump and not self.djump:
            self.dropY += self.jumpdir1 + self.jumpdir2
            self.minY = self.dropY
            self.jumpdir1 = 0
            self.jumpdir2 = 0
            self.fall_state = False
            self.jumprock = False

            # print("collid")
        else:
            print("collid2")

def enter():
    global boy, background, object,bottom
    background = Background()
    boy = Boy()
    object = Object().create()
    bottom = Bottom().create()

def exit():
    global boy, background, object,bottom
    f = open('life.txt', 'w')
    json.dump({'time': boy.life_time, 'life': boy.life_count}, f)
    f.close()
    del(background)
    del(boy)
    del (object)
    del (bottom)



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
            game_framework.change_state(main_state2)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_k):
            game_framework.change_state(score_state)
        else:
            boy.handle_events(event, frame_time)


def update(frame_time):
    state = False
    for ob in object:
        ob.update()
        if collide(boy, ob):
            boy.collid_object()
    for bo in bottom:
        if collide(boy, bo):
            boy.fall()
            state = True
        elif not state:
            boy.clear_fall()
            # background.not_collid()
    boy.update(frame_time)


def draw(frame_time):
    clear_canvas()
    background.draw()
    #boy.draw_bb()
    boy.draw()
    for ob in object:
        ob.draw()
    for bo in bottom:
        bo.draw()
    update_canvas()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
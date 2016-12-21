import random
import json
import os

from pico2d import *
object_data_file = open('object.txt', 'r')
object_data = json.load(object_data_file)
object_data_file.close()

object_data_file2 = open('object2.txt', 'r')
object_data2 = json.load(object_data_file2)
object_data_file2.close()
import game_framework
import title_state
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
    next_stage = False
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
        self.bgm = load_music("BGM/field.mp3")
        self.bgm.set_volume(60)
        self.bgm.repeat_play()

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Background.RUN_SPEED_PPS * frame_time
        self.total_frames += Background.FRAMES_PER_ACTION * Background.ACTION_PER_TIME * frame_time
        if Background.x < -1230:
            self.next_stage = True
        elif not self.rock and Background.x > -1230:
            Background.x -= 1*distance
            for ob in object:
                ob.control(frame_time)
            for ra in rader:
                ra.control(frame_time)

    def draw(self):
        self.image.clip_draw(0, 0, 3425, 850, Background.x, 0)
        #self.now_pos.draw(400, 400,'%d' % Background.x , (200, 0, 100))
        if self.next_stage:
            self.now_pos.draw(200, 200, ' press "a" ', (200, 0, 100))
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
        self.life_time = 0.0
        self.total_frames = 0.0

        self.left = 0
        self.right = 0
        self.bottom = 0
        self.top = 0
        self.ob = load_image('Obtacle1.png')
        self.ob1 = load_image('Obtacle5.png')


    def update(self, frame_time):
        pass

    def create(self):
        object = []
        for name in object_data:
            ob = Object()
            ob.left = object_data[name]['left']
            ob.right = object_data[name]['right']
            ob.bottom = object_data[name]['bottom']
            ob.top = object_data[name]['top']
            object.append(ob)
        return object

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

class Rader:

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
        rader = []
        for name in object_data2:
            ra = Rader()
            ra.left = object_data2[name]['left']
            ra.right = object_data2[name]['right']
            ra.bottom = object_data2[name]['bottom']
            ra.top = object_data2[name]['top']
            rader.append(ra)
        return rader

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

class Laser:

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
        self.la = load_image('Obtacle4.png')
        self.lax = 600
        self.lay = 180
        self.laser = False


    def update(self, frame_time):
        self.life_time += frame_time
        distance = Object.RUN_SPEED_PPS * frame_time
        self.total_frames += Object.FRAMES_PER_ACTION * Object.ACTION_PER_TIME * frame_time
        if self.laser:
            self.lax -= 3 * distance

    def draw(self):
        #draw_rectangle(*self.get_bb())
        if self.laser:
            self.la.draw(self.lax, self.lay)
    def on_laser(self):
        self.lax = 500
        self.laser = True

    def get_bb(self):
        return self.lax-30, self.lay - 10, self.lax+30, self.lay+10

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
        self.fall_state = False
        self.minY = 0
        self.dropY = 63
        self.climb = 0
        self.collid_state = False
        self.collid_stack = 0
        self.colideX = 1710
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.jump_sound = load_wav('SE/jump.wav')
        self.jump_sound.set_volume(50)
        self.gameover_sound = load_wav('SE/gameover.wav')
        self.gameover_sound.set_volume(50)
        self.life_count = 5
        self.over_count = 0
        self.state = self.RIGHT_STAND
        self.image = load_image('player2.png')
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)




    def update(self, frame_time):

        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time

        self.frame = int(self.total_frames) % 8
        if self.over_count == 0:
            #좌우이동
            if self.state == self.RIGHT_RUN:
                if self.x >= 240:
                    background.control('RIGHT')
                    background.update(frame_time)
                    self.colideX -= 1* distance
                else :
                    if not self.fall_state:
                        print(25112)
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
            self.dropY -=3
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
        elif self.y <=0:
            self.dropY = 63
            self.life_count -= 1
        if self.life_count == 0:
            self.gameover_sound.play()
            self.over_count += 1
            if self.over_count == 300:
                game_framework.change_state(score_state)

        self.y = self.dropY + self.jumpdir1 + self.jumpdir2

        #few second immune collid
        if self.collid_state:
            self.collid_stack +=1
            if self.collid_stack > 100:
                self.collid_stack = 0
                self.collid_state = False


        #self.life_count.append(self.life_count)


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
            self.minY = 60


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
            if not self.djump and self.jumpdir2 == 0 and not self.jumprock:
                self.jump_sound.play()
                self.jump = True
                if self.jump and self.jumpdir1 > 0:
                        self.djump = True
                        self.jumprock = True

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 10, self.y + 15

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass
    def collid_laser(self):
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

            #print("collid")
        else:
            print("collid2")

    def draw(self):
        #self.now_pos.draw(400, 300, '%d' % self.colideX, (200, 0, 100))
        self.draw_bb()
        if self.jumpdir1 > 0:
            self.image.clip_draw(208, 832, 32, 48, self.x, self.y)
        else:
            self.image.clip_draw(16 + self.frame * 64, 896, 32, 48, self.x, self.y)
        self.now_pos.draw(170, 400, 'life : %d' % self.life_count, (200, 0, 100))
        self.now_pos.draw(250, 400, 'time : %d' % self.life_time, (200, 0, 100))

def enter():
    global boy, background, object , rader,laser
    background = Background()
    boy = Boy()
    laser = Laser()
    rader = Rader().create()
    object = Object().create()

def exit():
    global boy, background, object,rader,laser


    f = open('life.txt', 'w')
    json.dump({'time':boy.life_time, 'life':boy.life_count}, f)
    f.close()
    del(background)
    del(boy)
    del(object)
    del(rader)
    del(laser)

def pause():
    pass

def resume():
    pass

def collid(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

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
    state = False

    boy.update(frame_time)
    laser.update(frame_time)
    if collid(boy,laser):
        boy.collid_laser()
    for ob in object:
        if collid(boy, ob):
            boy.fall()
            state = True
        elif not state:
            boy.clear_fall()
            #background.not_collid()
    for ra in rader:
        ra.update(frame_time)
        if collid(boy, ra):
            laser.on_laser()

def draw(frame_time):
    clear_canvas()
    background.draw()
    boy.draw()
    for ob in object:
        ob.draw()
    for ra in rader:
        ra.draw()
    laser.draw()
    update_canvas()







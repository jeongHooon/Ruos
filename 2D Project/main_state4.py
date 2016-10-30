import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state2
#import main_state3

name = "MainState4"

boy = None
grass = None
background = None
object = None
font = None


class Background:
    x = 1710
    def __init__(self):
        self.image = load_image('background4.png')
        self.rock = False
        self.now_pos = load_font("lazy_sunday_regular.ttf", 20)
        self.obtacle = load_image('Obtacle2.png')
        self.ob1x = 0
        self.ob1y = 70
        self.ob2x = 0
        self.ob2y = 0
        self.ob3x = 0
        self.ob3y = 0
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
        if Background.x < 1444:
            self.obtacle.draw(240 - self.ob1x, self.ob1y)
            self.ob1y += 2
            if self.rock == False:
                self.ob1x += 1

        if Background.x < 85:
            self.obtacle.draw(240 - self.ob2x, self.ob2y)
            self.ob2y += 2
            if self.ob2y == 420:
                self.ob2y = 0
            if self.rock == False:
                self.ob2x += 1

        if Background.x < 85:
            self.obtacle.draw(265 - self.ob3x, self.ob3y)
            self.ob3y += 2
            if self.ob3y == 420:
                self.ob3y = 0
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

        self.cx1, self.cy1 = 1060, 140

        self.ob1x, self.ob1y = 0, 0
        self.ob1delta = 2.0 * math.pi / self.num
        self.ob1r = 20

        self.ob2x, self.ob2y = 0, 0
        self.ob2delta = 2.0 * math.pi / self.num
        self.ob2r = 50

        self.cx2, self.cy2 = 1185, 250

        self.ob3x, self.ob3y = 0, 0
        self.ob3delta = 2.0 * math.pi / self.num
        self.ob3r = 20

        self.ob4x, self.ob4y = 0, 0
        self.ob4delta = 2.0 * math.pi / self.num
        self.ob4r = 50

        self.cx3, self.cy3 = 503, 190

        self.ob5x, self.ob5y = 0, 0
        self.ob5delta = 2.0 * math.pi / self.num
        self.ob5r = 20

        self.ob6x, self.ob6y = 0, 0
        self.ob6delta = 2.0 * math.pi / self.num
        self.ob6r = 50

        self.cx4, self.cy4 = 930, 5

        self.ob7x, self.ob7y = 0, 0
        self.ob7delta = 2.0 * math.pi / self.num
        self.ob7r = 20

        self.ob8x, self.ob8y = 0, 0
        self.ob8delta = 2.0 * math.pi / self.num
        self.ob8r = 50

        self.cx5, self.cy5 = 1190, 5

        self.ob9x, self.ob9y = 0, 0
        self.ob9delta = 2.0 * math.pi / self.num
        self.ob9r = 20

        self.ob10x, self.ob10y = 0, 0
        self.ob10delta = 2.0 * math.pi / self.num
        self.ob10r = 50

        self.cx6, self.cy6 = 1319, 140

        self.ob11x, self.ob11y = 0, 0
        self.ob11delta = 2.0 * math.pi / self.num
        self.ob11r = 20

        self.ob12x, self.ob12y = 0, 0
        self.ob12delta = 2.0 * math.pi / self.num
        self.ob12r = 50

        self.cx7, self.cy7 = 1444, 5

        self.ob13x, self.ob13y = 0, 0
        self.ob13delta = 2.0 * math.pi / self.num
        self.ob13r = 20

        self.ob14x, self.ob14y = 0, 0
        self.ob14delta = 2.0 * math.pi / self.num
        self.ob14r = 50

        self.cx8, self.cy8 = 1574, 140

        self.ob15x, self.ob15y = 0, 0
        self.ob15delta = 2.0 * math.pi / self.num
        self.ob15r = 20

        self.ob16x, self.ob16y = 0, 0
        self.ob16delta = 2.0 * math.pi / self.num
        self.ob16r = 50

        self.cx9, self.cy9 = 1760, 240

        self.ob17x, self.ob17y = 0, 0
        self.ob17delta = 2.0 * math.pi / self.num
        self.ob17r = 20

        self.ob18x, self.ob18y = 0, 0
        self.ob18delta = 2.0 * math.pi / self.num
        self.ob18r = 50

        self.cx10, self.cy10 = 1975, 110

        self.ob19x, self.ob19y = 0, 0
        self.ob19delta = 2.0 * math.pi / self.num
        self.ob19r = 20

        self.ob20x, self.ob20y = 0, 0
        self.ob20delta = 2.0 * math.pi / self.num
        self.ob20r = 50

        self.cx11, self.cy11 = 2207, 70

        self.ob21x, self.ob21y = 0, 0
        self.ob21delta = 2.0 * math.pi / self.num
        self.ob21r = 20

        self.ob22x, self.ob22y = 0, 0
        self.ob22delta = 2.0 * math.pi / self.num
        self.ob22r = 50

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

        self.ob5delta = 2.0 * math.pi / self.num
        self.ob5x = self.cx3 + (self.ob5r * math.cos(self.ob5delta * self.i))
        self.ob5y = self.cy3 + (self.ob5r * math.sin(self.ob5delta * self.i))

        self.ob6delta = 2.0 * math.pi / self.num
        self.ob6x = self.cx3 + (self.ob6r * math.cos(self.ob6delta * self.i))
        self.ob6y = self.cy3 + (self.ob6r * math.sin(self.ob6delta * self.i))

        self.ob7delta = 2.0 * math.pi / self.num
        self.ob7x = self.cx4 + (self.ob7r * math.cos(self.ob7delta * self.i))
        self.ob7y = self.cy4 + (self.ob7r * math.sin(self.ob7delta * self.i))

        self.ob8delta = 2.0 * math.pi / self.num
        self.ob8x = self.cx4 + (self.ob8r * math.cos(self.ob8delta * self.i))
        self.ob8y = self.cy4 + (self.ob8r * math.sin(self.ob8delta * self.i))

        self.ob9delta = 2.0 * math.pi / self.num
        self.ob9x = self.cx5 + (self.ob9r * math.cos(self.ob9delta * self.i))
        self.ob9y = self.cy5 + (self.ob9r * math.sin(self.ob9delta * self.i))

        self.ob10delta = 2.0 * math.pi / self.num
        self.ob10x = self.cx5 + (self.ob10r * math.cos(self.ob10delta * self.i))
        self.ob10y = self.cy5 + (self.ob10r * math.sin(self.ob10delta * self.i))

        self.ob11delta = 2.0 * math.pi / self.num
        self.ob11x = self.cx6 + (self.ob11r * math.cos(self.ob11delta * self.i))
        self.ob11y = self.cy6 + (self.ob11r * math.sin(self.ob11delta * self.i))

        self.ob12delta = 2.0 * math.pi / self.num
        self.ob12x = self.cx6 + (self.ob12r * math.cos(self.ob12delta * self.i))
        self.ob12y = self.cy6 + (self.ob12r * math.sin(self.ob12delta * self.i))

        self.ob13delta = 2.0 * math.pi / self.num
        self.ob13x = self.cx7 + (self.ob13r * math.cos(self.ob13delta * self.i))
        self.ob13y = self.cy7 + (self.ob13r * math.sin(self.ob13delta * self.i))

        self.ob14delta = 2.0 * math.pi / self.num
        self.ob14x = self.cx7 + (self.ob14r * math.cos(self.ob14delta * self.i))
        self.ob14y = self.cy7 + (self.ob14r * math.sin(self.ob14delta * self.i))

        self.ob15delta = 2.0 * math.pi / self.num
        self.ob15x = self.cx8 + (self.ob15r * math.cos(self.ob15delta * self.i))
        self.ob15y = self.cy8 + (self.ob15r * math.sin(self.ob15delta * self.i))

        self.ob4delta = 2.0 * math.pi / self.num
        self.ob16x = self.cx8 + (self.ob16r * math.cos(self.ob16delta * self.i))
        self.ob16y = self.cy8 + (self.ob16r * math.sin(self.ob16delta * self.i))

        self.ob17delta = 2.0 * math.pi / self.num
        self.ob17x = self.cx9 + (self.ob17r * math.cos(self.ob17delta * self.i))
        self.ob17y = self.cy9 + (self.ob17r * math.sin(self.ob17delta * self.i))

        self.ob18delta = 2.0 * math.pi / self.num
        self.ob18x = self.cx9 + (self.ob18r * math.cos(self.ob18delta * self.i))
        self.ob18y = self.cy9 + (self.ob18r * math.sin(self.ob18delta * self.i))

        self.ob19delta = 2.0 * math.pi / self.num
        self.ob19x = self.cx10 + (self.ob19r * math.cos(self.ob19delta * self.i))
        self.ob19y = self.cy10 + (self.ob19r * math.sin(self.ob19delta * self.i))

        self.ob20delta = 2.0 * math.pi / self.num
        self.ob20x = self.cx10 + (self.ob20r * math.cos(self.ob20delta * self.i))
        self.ob20y = self.cy10 + (self.ob20r * math.sin(self.ob20delta * self.i))

        self.ob21delta = 2.0 * math.pi / self.num
        self.ob21x = self.cx11 + (self.ob21r * math.cos(self.ob21delta * self.i))
        self.ob21y = self.cy11 + (self.ob21r * math.sin(self.ob21delta * self.i))

        self.ob22delta = 2.0 * math.pi / self.num
        self.ob22x = self.cx11 + (self.ob22r * math.cos(self.ob22delta * self.i))
        self.ob22y = self.cy11 + (self.ob22r * math.sin(self.ob22delta * self.i))

        self.i = self.i + 1
        if self.i == 100:
            self.i = 0
    def draw(self):
        self.ob.draw(self.ob1x, self.ob1y)
        self.ob.draw(self.ob2x, self.ob2y)
        self.ob.draw(self.ob3x, self.ob3y)
        self.ob.draw(self.ob4x, self.ob4y)
        self.ob.draw(self.ob5x, self.ob5y)
        self.ob.draw(self.ob6x, self.ob6y)
        self.ob.draw(self.ob7x, self.ob7y)
        self.ob.draw(self.ob8x, self.ob8y)
        self.ob.draw(self.ob9x, self.ob9y)
        self.ob.draw(self.ob10x, self.ob10y)
        self.ob.draw(self.ob11x, self.ob11y)
        self.ob.draw(self.ob12x, self.ob12y)
        self.ob.draw(self.ob13x, self.ob13y)
        self.ob.draw(self.ob14x, self.ob14y)
        self.ob.draw(self.ob15x, self.ob15y)
        self.ob.draw(self.ob16x, self.ob16y)
        self.ob.draw(self.ob17x, self.ob17y)
        self.ob.draw(self.ob18x, self.ob18y)
        self.ob.draw(self.ob19x, self.ob19y)
        self.ob.draw(self.ob20x, self.ob20y)
        self.ob.draw(self.ob21x, self.ob21y)
        self.ob.draw(self.ob22x, self.ob22y)
    def control(self):
        self.cx1 -= 1
        self.cx2 -= 1
        self.cx3 -= 1
        self.cx4 -= 1
        self.cx5 -= 1
        self.cx6 -= 1
        self.cx7 -= 1
        self.cx8 -= 1
        self.cx9 -= 1
        self.cx10 -= 1
        self.cx11 -= 1
class Boy:
    def __init__(self):
        self.x, self.y = 0, 130
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
        else:
                boy.handle_events(event)


def update():
    boy.update()
    object.update()


def draw():
    clear_canvas()
    background.draw()
    boy.draw()
    object.draw()
    update_canvas()






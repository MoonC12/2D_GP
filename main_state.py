import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
map01 = None
font = None



class Map:
    def __init__(self):
        self.image = load_image('Map.png')

    def draw(self):
        self.image.draw(400, 300)


#class Boy:
    #def __init__(self):
        #self.x, self.y = 0, 90
        #self.frame = 0
        #self.image = load_image('run_animation.png')
        #self.dir = 1

    #def update(self):
        #self.frame = (self.frame + 1) % 8
        #self.x += self.dir
        #if self.x >= 800:
            #self.dir = -1
        #elif self.x <= 0:
            #self.dir = 1

    #def draw(self):
        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Character:
    image = None

    LEFT_RUN, RIGHT_RUN, DROP_RIGHT, DROP_LEFT= 0, 1, 2, 3

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x > 60 and self.x < 240:
            if self.x < 60:
                self.state = self.RIGHT_RUN
                self.x = 60
        if self.x > 240 and self.x < 560:
            if self.x < 240:
                self.state = self.DROP_LEFT
                self.x = 240
        if self.x > 560 and self.x < 740:
            if self.x < 560:
                self.state = self.DROP_LEFT
                self.x = 560


    def handle_right_run(self):
        self.x += 5
        self.run_frames +=1
        if self.x > 60 and self.x < 240:
            if self.x > 240:
                self.state = self.DROP_RIGHT
                self.x = 240
        if self.x > 240 and self.x < 560:
            if self.x > 560:
                self.state = self.DROP_RIGHT
                self.x = 560
        if self.x > 560 and self.x < 740:
            if self.x > 740:
                self.state = self.LEFT_RUN
                self.x = 740

    def handle_drop_right(self):
        self.y -= 5
        self.run_frames +=1
        if self.y > 425:
            if self.y < 425:
                self.state = self.RIGHT_RUN
                self.y = 425
        




    handle_state = {
                LEFT_RUN:   handle_left_run,
                RIGHT_RUN:  handle_right_run
    }


    def __init__(self):
        self.x, self.y = 60, 60
        self.frame = 0
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Character.image == None:
            Character.image = load_image('Monster.png')

    def update(self):
        #if self.state == self.DROP:
            #self.frame = (self.frame + 1) % 12
            #self.y -= (self.dir * 5)
        if self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 1) % 12
            self.x += (self.dir * 5)
        elif self.state == self.LEFT_RUN:
            self.frame = (self.frame + 1) % 12
            self.x += (self.dir * 5)

        if self.x > 240:
            self.dir = -1
            self.x = 240
            self.state = self.LEFT_RUN
        elif self.x < 60:
            self.dir = 1
            self.x = 60
            self.state = self.RIGHT_RUN

    def draw(self):
        self.image.clip_draw(self.frame * 50, self.state * 60, 45, 50, self.x, self.y)


def enter():
    global map01, character#, boy
    #boy = Boy()
    character = Character()
    map01 = Map()


def exit():
    global map01, character#, boy
    #del(boy)
    del(character)
    del(map01)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


def update():
    #boy.update()
    character.update()


def draw():
    clear_canvas()
    map01.draw()
    #boy.draw()
    character.draw()
    update_canvas()
    delay(0.05)






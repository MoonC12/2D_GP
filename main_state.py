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

class Monster:
    image = None
    monster_dir = random.randint(0, 1)    #0 -> left  1 -> right
    LEFT_RUN, RIGHT_RUN, DROP_LEFT, DROP_RIGHT, SPAWN= 0, 1, 2, 3, 4

    def handle_spawn(self):
        if self.monster_dir == 0:
            self.state = self.DROP_LEFT
        if self.monster_dir == 1:
            self.state = self.DROP_RIGHT

    def handle_left_run(self):
        self.x -= 5
        if self.y == 300 or self.y == 60:
            if self.x < 60:
                self.state = self.RIGHT_RUN
                self.x = 60
            if self.x > 400 and self.x < 540:
                self.state = self.DROP_LEFT
                self.x = 540
        if self.y == 425 or self.y == 180:
            if self.x < 220:
                self.state = self.DROP_LEFT
                self.x = 220


    def handle_right_run(self):
        self.x += 5
        if self.y == 300 or self.y == 60:
            if self.x < 400 and self.x > 270:
                self.state = self.DROP_RIGHT
                self.x = 270
            if self.x > 740:
                self.state = self.LEFT_RUN
                self.x = 740
        if self.y == 425 or self.y == 180:
            if self.x > 590:
                self.state = self.DROP_RIGHT
                self.x = 590

    def handle_drop_right(self):
        self.y -= 5
        if self.y == 425:
            self.state = self.RIGHT_RUN
            self.y = 425
        if self.y == 300:
            self.state = self.RIGHT_RUN
            self.y = 300
        if self.y == 180:
            self.state = self.RIGHT_RUN
            self.y = 180
        if self.y == 60:
            self.state = self.RIGHT_RUN
            self.y = 60
        if self.y < 60:
            if self.y < 0:
                self.state = self.SPAWN
                self.monster_dir = random.randint(0, 1)
                self.x, self.y = 400, 600

    def handle_drop_left(self):
        self.y -= 5
        if self.y == 425:
            self.state = self.LEFT_RUN
            self.y = 425
        if self.y == 300:
                self.state = self.LEFT_RUN
                self.y = 300
        if self.y == 180:
            self.state = self.LEFT_RUN
            self.y = 180
        if self.y == 60:
            self.state = self.LEFT_RUN
            self.y = 60
        if self.y < 60:
            if self.y < 0:
                self.state = self.SPAWN
                self.monster_dir = random.randint(0, 1)
                self.x, self.y = 400, 600


    handle_state = {
                LEFT_RUN:   handle_left_run,
                RIGHT_RUN:  handle_right_run,
                DROP_RIGHT: handle_drop_right,
                DROP_LEFT:  handle_drop_left,
                SPAWN:  handle_spawn
    }

    def update(self):
        self.frame = (self.frame + 1) % 12
        self.handle_state[self.state](self)

    def __init__(self):
        self.x, self.y = 400, 600
        self.frame = 0
        self.state = self.SPAWN
        if Monster.image == None:
            Monster.image = load_image('Monster.png')

    def draw(self):
        self.image.clip_draw(self.frame * 50, self.state * 60, 45, 50, self.x, self.y)


def enter():
    global map01, monster#, boy
    #boy = Boy()
    monster = Monster()
    map01 = Map()


def exit():
    global map01, monster#, boy
    #del(boy)
    del(monster)
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
    monster.update()


def draw():
    clear_canvas()
    map01.draw()
    #boy.draw()
    monster.draw()
    update_canvas()
    delay(0.05)






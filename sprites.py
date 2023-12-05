import pygame as pg
from pygame.sprite import Sprite
import os
from settings import *
import random
from random import randint
from pygame.math import Vector2 as vec

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(100, 100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -4
        if keys[pg.K_d]:
            self.acc.x = 4
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        ghits = pg.sprite.collide_rect(self, self.game.ground)       
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits or ghits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x < 0 + 15:
            self.pos.x = 0 + 15
        if self.pos.x > WIDTH - 15:
            self.pos.x = WIDTH - 15
        self.rect.midbottom = self.pos

class Platform(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(randint(COLORS))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.speed = 0
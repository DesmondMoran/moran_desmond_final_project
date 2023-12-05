# This file was created by: Desmond Moran

# Title: Endless runner plaformer

# Sources:
# https://www.youtube.com/watch?v=ZV8TNrwqG1Y
# https://github.com/parthbyt/Infinite-Runner-Pygame
# https://quirkycort.github.io/tutorials/20-Pygame-Zero-Basics/30-Ninja/40-jump.html

# Goals: 
    # mobs that endlessly chase you
    # player health and score
    # player upgrades/power ups
    # increasing speed
    # relayable without quitting

import pygame as pg
from pygame.sprite import Sprite
import random 
from random import randint
import os
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("EndLess Runner")
        self.clock = pg.time.Clock()
        self.running = True 

    def new (self):
        self.background = BLACK
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.ground = Platform(*GROUND)
        self.all_sprites.add(self.ground)
        self.score = SCORE
        for p in PLATFORM_LIST:
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
        ghits = pg.sprite.collide_rect(self.player, self.ground)
        if hits or ghits:
            if self.player.vel.y < 0:
                self.player.rect.top = hits[0].rect.bottom
                self.player.vel.y = -self.player.vel.y
            # this is what prevents the player from falling through the platform when falling down...
            elif self.player.vel.y > 0:
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    self.player.vel.x = hits[0].speed*1.6
                if ghits:
                    self.player.pos.y = self.ground.rect.top
                    self.player.vel.y = 0

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
    def draw(self):            
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # self.screen.blit(self.background, (0,0))
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 22, BLACK, WIDTH/2, HEIGHT-40)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

g = Game()
while g.running:
    g.new()

pg.quit()
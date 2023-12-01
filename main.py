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

        
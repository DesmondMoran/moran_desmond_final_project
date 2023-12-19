# file created by: Desmond Moran
import random 
from random import choices
from random import randint
import pygame as pg

pg.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
Color = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

# Player settings and variables
score = 0 
player_x = 50 
player_y = 430
y_acc = 0
x_acc = 0

# Obstacle settings and variables
obstacles = [randint(300, 425), 650, 850, 1050]
obstacle_vel = 4

# Game settings
WIDTH = 1000
HEIGHT = 500
FPS = 60 
GRAV = 1.5
Active = True

screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Test Final')
background = BLACK
font_name = pg.font.match_font('arial')
font = pg.font.Font(font_name, 16)
timer = pg.time.Clock()
running = True

while running:
    timer.tick(FPS)
    screen.fill(background)
    ground = pg.draw.rect(screen, GREEN, [0, 450, WIDTH, 5])
    player = pg.draw.rect(screen, PURPLE, [player_x, player_y, 20, 20])

   # Drawing the obstacles on screen
    obstacle0 = pg.draw.rect(screen, RED, [obstacles[0], 430, 20, 20])
    obstacle1 = pg.draw.rect(screen, ORANGE, [obstacles[1], 430, 20, 20])
    obstacle2 = pg.draw.rect(screen, YELLOW, [obstacles[2], 430, 20, 20])
    obstacle3 = pg.draw.rect(screen, BLUE, [obstacles[3], 430, 20, 20])

    for event in pg.event.get():
         if event.type == pg.QUIT:
            running = False
         if event.type == pg.KEYDOWN and not Active:
            if event.key == pg.K_SPACE:
               Active = True
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and y_acc == 0:
              y_acc = 20
            if event.key == pg.K_d:
              x_acc = 10
            if event.key == pg.K_a:
              x_acc = -10 
         if event.type == pg.KEYUP:
            if event.key == pg.K_d:
              x_acc = 0
            if event.key == pg.K_a:
               x_acc = 0

    for i in range(len(obstacles)):
      if Active:
         obstacles[i] -= obstacle_vel
         if obstacles[i] < -20:
            obstacles[i] = random.randint(1050, 1250)
            score += 1

    if 0 <= player_x <= 980:
       player_x += x_acc
    if player_x < 0:
       player_x = 0
    if player_x > 980:
       player_x = 980

    if y_acc > 0 or player_y < 430:
       player_y -= y_acc
       y_acc -= GRAV
    if player_y > 430:
       player_y = 430
    if player_y == 430 and y_acc < 0:
        y_acc = 0


    pg.display.flip()

pg.quit()


# Game settings
WIDTH = 1000
HEIGHT = 500
FPS = 60 
SCORE = 0 

# Player settings
PLAYER_JUMP = 20
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.25

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [WHITE, RED, GREEN, BLUE]

obstacles = []

GROUND = (-20, HEIGHT - 40, WIDTH+40, 40, " ")
OBSTACLE_LIST = []
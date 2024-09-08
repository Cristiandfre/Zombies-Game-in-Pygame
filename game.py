#import libraries
import pygame, sys
from pygame.locals import *

#initializing
pygame.init()
pygame.mixer.init()

#fps 
FPS = 25
FramePerSec = pygame.time.Clock()

#colors
WHITE = (255, 255, 255)

#variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = (800, 600)
GAMEOVER = pygame.transform.scale(pygame.image.load('./Img/Game Over/GameOver.png'), (400, 200))
GAMENAME = pygame.transform.scale(pygame.image.load('./Img/Game Name/duum.png'), (430, 150))
RANKING = pygame.transform.scale(pygame.image.load('./Img/Ranking/ranking.png'), (430, 150))
CONTROL = pygame.transform.scale(pygame.image.load('./Img/Control/control.png'), (430, 150))
ARROW = pygame.transform.scale(pygame.image.load('./Img/Back Arrow/arrow.png'), (50, 50))
LEFT = pygame.transform.scale(pygame.image.load('./Img/Movements/left.png'), (20, 20))
RIGHT = pygame.transform.scale(pygame.image.load('./Img/Movements/right.png'), (20, 20))
UP = pygame.transform.scale(pygame.image.load('./Img/Movements/up.png'), (20, 20))
BULLET = pygame.transform.scale(pygame.image.load('./Img/Bullets/2.png'), (4, 12))

#music
background_sound = pygame.mixer.Sound("./Music/Escape_Looping.mp3")
gameOver_sound = pygame.mixer.Sound("./Music/gameOver.wav")
attack1_sound = pygame.mixer.Sound("./Music/boxing_hitwall1.wav")
attack2_sound = pygame.mixer.Sound("./Music/punch.wav")
shoot_sound = pygame.mixer.Sound("./Music/ot_attack.wav")
go_sound = pygame.mixer.Sound("./Music/go.mp3")
dying_sound = pygame.mixer.Sound("./Music/dying.wav")
selecting_sound = pygame.mixer.Sound("./Music/selecting.wav")
reload_sound = pygame.mixer.Sound("./Music/reload.mp3")


#world
tiles = [pygame.image.load('./World/Tiles/Tile_01.png'), pygame.image.load('./World/Tiles/Tile_03.png'), pygame.image.load('./World/Tiles/Tile_04.png'), pygame.image.load('./World/Tiles/Tile_11.png'), pygame.image.load('./World/Tiles/Tile_13.png') ,pygame.image.load('./World/Tiles/Tile_20.png'), pygame.image.load('./World/Tiles/Tile_22.png'), pygame.image.load('./World/Tiles/Tile_14.png'), pygame.image.load('./World/Tiles/Tile_19.png')]
others = [pygame.image.load('./World/Others/3.png'), pygame.image.load('./World/Others/11.png'), pygame.image.load('./World/Others/18.png'), pygame.image.load('./World/Others/Tile_05.png'), pygame.image.load('./World/Others/14.png'), pygame.image.load('./World/Others/Pointer2.png'), pygame.image.load('./World/Others/Box3.png'), pygame.image.load('./World/Others/6.png')]
backgroundNotProcessed = [pygame.image.load('./World/Background/1.png'), pygame.image.load('./World/Background/2.png'), pygame.image.load('./World/Background/3.png'), pygame.image.load('./World/Background/4.png'), pygame.image.load('./World/Background/5.png')]
background = []

for x in range(5):
    background.append(pygame.transform.scale(backgroundNotProcessed[x], SCREEN))

world_map = [[0 for _ in range(26)] for _ in range(20)]

#world - ground
for x in range(26):
    world_map[17][x] = 2
    world_map[18][x] = 4
    world_map[19][x] = 4
#world - block 
for x in range(10):
    if x == 2 or x == 8:
        continue
    world_map[11][x] = 11

for x in range(10):
    world_map[12][x] = 2 
    world_map[13][x] = 5

for x in range(7):
    world_map[10][25-x] = 5
    world_map[9][25-x] = 2 
    world_map[8][24-x] = 13 #relva vermelha

#arvores dos andares
world_map[10][2] = 12 #Arvores
world_map[10][8] = 12 #Arvores 

world_map[7][18] = 14

#arvores do chao
world_map[15][7] = 15
world_map[15][15] = 15

#pointer
world_map[16][24] = 16
world_map[16][1] = 16

#boxes
world_map[16][22] = 17
world_map[16][10] = 18



world_map[12][10] = 3
world_map[13][10] = 7

world_map[10][18] = 9
world_map[9][18] = 8





#player1
P1run_right = [pygame.image.load('./Players/P1/run/tile000.png'), pygame.image.load('./Players/P1/run/tile001.png'), pygame.image.load('./Players/P1/run/tile002.png'), pygame.image.load('./Players/P1/run/tile003.png'), pygame.image.load('./Players/P1/run/tile004.png'), pygame.image.load('./Players/P1/run/tile005.png'), pygame.image.load('./Players/P1/run/tile006.png'), pygame.image.load('./Players/P1/run/tile007.png')]
P1idle_right = [pygame.image.load('./Players/P1/idle/tile000.png'), pygame.image.load('./Players/P1/idle/tile001.png'), pygame.image.load('./Players/P1/idle/tile002.png'), pygame.image.load('./Players/P1/idle/tile003.png'), pygame.image.load('./Players/P1/idle/tile004.png'), pygame.image.load('./Players/P1/idle/tile005.png')]
P1jump_right = [pygame.image.load('./Players/P1/jump/tile000.png'), pygame.image.load('./Players/P1/jump/tile001.png'), pygame.image.load('./Players/P1/jump/tile002.png'), pygame.image.load('./Players/P1/jump/tile003.png'), pygame.image.load('./Players/P1/jump/tile004.png'), pygame.image.load('./Players/P1/jump/tile005.png'), pygame.image.load('./Players/P1/jump/tile006.png'), pygame.image.load('./Players/P1/jump/tile007.png'), pygame.image.load('./Players/P1/jump/tile008.png'), pygame.image.load('./Players/P1/jump/tile009.png'), pygame.image.load('./Players/P1/jump/tile010.png'),]
P1attack1_right = [pygame.image.load('./Players/P1/attack1/tile000.png'), pygame.image.load('./Players/P1/attack1/tile001.png'), pygame.image.load('./Players/P1/attack1/tile002.png'), pygame.image.load('./Players/P1/attack1/tile003.png'), pygame.image.load('./Players/P1/attack1/tile004.png'), pygame.image.load('./Players/P1/attack1/tile005.png'),]
P1recharge_right = [pygame.image.load('./Players/P1/recharge/tile000.png'), pygame.image.load('./Players/P1/recharge/tile001.png'), pygame.image.load('./Players/P1/recharge/tile002.png'), pygame.image.load('./Players/P1/recharge/tile003.png'), pygame.image.load('./Players/P1/recharge/tile004.png'), pygame.image.load('./Players/P1/recharge/tile005.png'), pygame.image.load('./Players/P1/recharge/tile006.png'), pygame.image.load('./Players/P1/recharge/tile007.png'), pygame.image.load('./Players/P1/recharge/tile008.png'), pygame.image.load('./Players/P1/recharge/tile009.png'), pygame.image.load('./Players/P1/recharge/tile010.png'), pygame.image.load('./Players/P1/recharge/tile011.png'),] 
P1hurt_right = [pygame.image.load('./Players/P1/hurt/tile000.png'), pygame.image.load('./Players/P1/hurt/tile001.png')]
P1dead_right = [pygame.image.load('./Players/P1/dead/tile000.png'), pygame.image.load('./Players/P1/dead/tile001.png'), pygame.image.load('./Players/P1/dead/tile002.png'), pygame.image.load('./Players/P1/dead/tile003.png')]
P1attack2_right = [pygame.image.load('./Players/P1/attack2/tile000.png'), pygame.image.load('./Players/P1/attack2/tile001.png'), pygame.image.load('./Players/P1/attack2/tile002.png')]
P1shoot_right = [pygame.image.load('./Players/P1/shoot/tile000.png'), pygame.image.load('./Players/P1/shoot/tile001.png'), pygame.image.load('./Players/P1/shoot/tile002.png'), pygame.image.load('./Players/P1/shoot/tile003.png'), pygame.image.load('./Players/P1/shoot/tile004.png'), pygame.image.load('./Players/P1/shoot/tile005.png'), pygame.image.load('./Players/P1/shoot/tile006.png'), pygame.image.load('./Players/P1/shoot/tile007.png'), pygame.image.load('./Players/P1/shoot/tile008.png'), pygame.image.load('./Players/P1/shoot/tile009.png'), pygame.image.load('./Players/P1/shoot/tile010.png'), pygame.image.load('./Players/P1/shoot/tile011.png') ]


P1run_left = []
P1idle_left = []
P1jump_left = []
P1attack1_left = []
P1recharge_left = []
P1hurt_left = [] 
P1dead_left = []
P1attack2_left = [] 
P1shoot_left = [] 

for x in range(8):
    P1run_left.append(pygame.transform.flip(P1run_right[x], True, False))
for x in range(6):
    P1idle_left.append(pygame.transform.flip(P1idle_right[x], True, False))
for x in range(11):
    P1jump_left.append(pygame.transform.flip(P1jump_right[x], True, False))
for x in range(6):
    P1attack1_left.append(pygame.transform.flip(P1attack1_right[x], True, False))
for x in range(12):
    P1recharge_left.append(pygame.transform.flip(P1recharge_right[x], True, False))
for x in range(2):
    P1hurt_left.append(pygame.transform.flip(P1hurt_right[x], True, False))
for x in range(4): 
    P1dead_left.append(pygame.transform.flip(P1dead_right[x], True, False))
for x in range(3):
    P1attack2_left.append(pygame.transform.flip(P1attack2_right[x], True, False))
for x in range(12):
    P1shoot_left.append(pygame.transform.flip(P1shoot_right[x], True, False))

#Enemy 1
#check
E1run_right = [pygame.image.load('./Enemies/E1/Run/tile000.png'), pygame.image.load('./Enemies/E1/Run/tile001.png'), pygame.image.load('./Enemies/E1/Run/tile002.png'), pygame.image.load('./Enemies/E1/Run/tile003.png'), pygame.image.load('./Enemies/E1/Run/tile004.png'), pygame.image.load('./Enemies/E1/Run/tile005.png'), pygame.image.load('./Enemies/E1/Run/tile006.png'), pygame.image.load('./Enemies/E1/Run/tile007.png')]
#check
E1idle_right = [pygame.image.load('./Enemies/E1/Idle/tile000.png'), pygame.image.load('./Enemies/E1/Idle/tile001.png'), pygame.image.load('./Enemies/E1/Idle/tile002.png'), pygame.image.load('./Enemies/E1/Idle/tile003.png'), pygame.image.load('./Enemies/E1/Idle/tile004.png'), pygame.image.load('./Enemies/E1/Idle/tile005.png'), pygame.image.load('./Enemies/E1/Idle/tile006.png'), pygame.image.load('./Enemies/E1/Idle/tile007.png'), pygame.image.load('./Enemies/E1/Idle/tile008.png')]
#check
E1hurt_right = [pygame.image.load('./Enemies/E1/Hurt/tile000.png'), pygame.image.load('./Enemies/E1/Hurt/tile001.png'), pygame.image.load('./Enemies/E1/Hurt/tile002.png'), pygame.image.load('./Enemies/E1/Hurt/tile003.png'), pygame.image.load('./Enemies/E1/Hurt/tile004.png')]
#check
E1dead_right = [pygame.image.load('./Enemies/E1/Dead/tile000.png'), pygame.image.load('./Enemies/E1/Dead/tile001.png'), pygame.image.load('./Enemies/E1/Dead/tile002.png'), pygame.image.load('./Enemies/E1/Dead/tile003.png'), pygame.image.load('./Enemies/E1/Dead/tile004.png'), ]
#check
E1attack1_right = [pygame.image.load('./Enemies/E1/Attack1/tile000.png'), pygame.image.load('./Enemies/E1/Attack1/tile001.png'), pygame.image.load('./Enemies/E1/Attack1/tile002.png'), pygame.image.load('./Enemies/E1/Attack1/tile003.png')]
#check
E1attack2_right = [pygame.image.load('./Enemies/E1/Attack2/tile000.png'), pygame.image.load('./Enemies/E1/Attack2/tile001.png'), pygame.image.load('./Enemies/E1/Attack2/tile002.png'), pygame.image.load('./Enemies/E1/Attack2/tile003.png')]
#check
E1attack3_right = [pygame.image.load('./Enemies/E1/Attack3/tile000.png'), pygame.image.load('./Enemies/E1/Attack3/tile001.png'), pygame.image.load('./Enemies/E1/Attack3/tile002.png'), pygame.image.load('./Enemies/E1/Attack3/tile003.png'),]
#check
E1jump_right = [pygame.image.load('./Enemies/E1/Jump/tile000.png'), pygame.image.load('./Enemies/E1/Jump/tile001.png'), pygame.image.load('./Enemies/E1/Jump/tile002.png'), pygame.image.load('./Enemies/E1/Jump/tile003.png'), pygame.image.load('./Enemies/E1/Jump/tile004.png'), pygame.image.load('./Enemies/E1/Jump/tile005.png')]
#check
E1eating_right = [pygame.image.load('./Enemies/E1/Eating/tile000.png'), pygame.image.load('./Enemies/E1/Eating/tile001.png'), pygame.image.load('./Enemies/E1/Eating/tile002.png'), pygame.image.load('./Enemies/E1/Eating/tile003.png'), pygame.image.load('./Enemies/E1/Eating/tile004.png'), pygame.image.load('./Enemies/E1/Eating/tile005.png'), pygame.image.load('./Enemies/E1/Eating/tile006.png'), pygame.image.load('./Enemies/E1/Eating/tile007.png'), pygame.image.load('./Enemies/E1/Eating/tile008.png'), pygame.image.load('./Enemies/E1/Eating/tile009.png'), pygame.image.load('./Enemies/E1/Eating/tile010.png')]

E1run_left = []
E1idle_left = []
E1hurt_left = []
E1dead_left = []
E1attack1_left = []
E1attack2_left = []
E1attack3_left = []
E1jump_left = []
E1eating_left = []

for x in range(8):
    E1run_left.append(pygame.transform.flip(E1run_right[x], True, False))
for x in range(9):
    E1idle_left.append(pygame.transform.flip(E1idle_right[x], True, False))
for x in range(5):
    E1hurt_left.append(pygame.transform.flip(E1hurt_right[x], True, False))
for x in range(5):
    E1dead_left.append(pygame.transform.flip(E1dead_right[x], True, False))
for x in range(4):
    E1attack1_left.append(pygame.transform.flip(E1attack1_right[x], True, False))
for x in range(4):
    E1attack2_left.append(pygame.transform.flip(E1attack2_right[x], True, False))
for x in range(4):
    E1attack3_left.append(pygame.transform.flip(E1attack3_right[x], True, False))
for x in range(6):
    E1jump_left.append(pygame.transform.flip(E1jump_right[x], True, False))
for x in range(11):
    E1eating_left.append(pygame.transform.flip(E1eating_right[x], True, False))

#Enemy 2
#check
E2run_right = [pygame.image.load('./Enemies/E2/Run/tile000.png'), pygame.image.load('./Enemies/E2/Run/tile001.png'), pygame.image.load('./Enemies/E2/Run/tile002.png'), pygame.image.load('./Enemies/E2/Run/tile003.png'), pygame.image.load('./Enemies/E2/Run/tile004.png'), pygame.image.load('./Enemies/E2/Run/tile005.png'), pygame.image.load('./Enemies/E2/Run/tile006.png')]
#check
E2idle_right = [pygame.image.load('./Enemies/E2/Idle/tile000.png'), pygame.image.load('./Enemies/E2/Idle/tile001.png'), pygame.image.load('./Enemies/E2/Idle/tile002.png'), pygame.image.load('./Enemies/E2/Idle/tile003.png'), pygame.image.load('./Enemies/E2/Idle/tile004.png'), pygame.image.load('./Enemies/E2/Idle/tile005.png'), pygame.image.load('./Enemies/E2/Idle/tile006.png'), pygame.image.load('./Enemies/E2/Idle/tile007.png')]
#check
E2hurt_right = [pygame.image.load('./Enemies/E2/Hurt/tile000.png'), pygame.image.load('./Enemies/E2/Hurt/tile001.png'), pygame.image.load('./Enemies/E2/Hurt/tile002.png')]
#check
E2dead_right = [pygame.image.load('./Enemies/E2/Dead/tile000.png'), pygame.image.load('./Enemies/E2/Dead/tile001.png'), pygame.image.load('./Enemies/E2/Dead/tile002.png'), pygame.image.load('./Enemies/E2/Dead/tile003.png'), pygame.image.load('./Enemies/E2/Dead/tile004.png'), ]
#check
E2attack1_right = [pygame.image.load('./Enemies/E2/Attack1/tile000.png'), pygame.image.load('./Enemies/E2/Attack1/tile001.png'), pygame.image.load('./Enemies/E2/Attack1/tile002.png'), pygame.image.load('./Enemies/E2/Attack1/tile003.png'), pygame.image.load('./Enemies/E2/Attack1/tile004.png')]
#check
E2attack2_right = [pygame.image.load('./Enemies/E2/Attack2/tile000.png'), pygame.image.load('./Enemies/E2/Attack2/tile001.png'), pygame.image.load('./Enemies/E2/Attack2/tile002.png'), pygame.image.load('./Enemies/E2/Attack2/tile003.png')]
#check
E2attack3_right = [pygame.image.load('./Enemies/E2/Attack3/tile000.png'), pygame.image.load('./Enemies/E2/Attack3/tile001.png'), pygame.image.load('./Enemies/E2/Attack3/tile002.png'), pygame.image.load('./Enemies/E2/Attack3/tile003.png'), pygame.image.load('./Enemies/E2/Attack3/tile004.png')]
#check
E2jump_right = [pygame.image.load('./Enemies/E2/Jump/tile000.png'), pygame.image.load('./Enemies/E2/Jump/tile001.png'), pygame.image.load('./Enemies/E2/Jump/tile002.png'), pygame.image.load('./Enemies/E2/Jump/tile003.png'), pygame.image.load('./Enemies/E2/Jump/tile004.png'), pygame.image.load('./Enemies/E2/Jump/tile005.png'), pygame.image.load('./Enemies/E2/Jump/tile006.png'), pygame.image.load('./Enemies/E2/Jump/tile007.png')]

E2run_left = []
E2idle_left = []
E2hurt_left = []
E2dead_left = []
E2attack1_left = []
E2attack2_left = []
E2attack3_left = []
E2jump_left = []

for x in range(7):
    E2run_left.append(pygame.transform.flip(E2run_right[x], True, False))
for x in range(8):
    E2idle_left.append(pygame.transform.flip(E2idle_right[x], True, False))
for x in range(3):
    E2hurt_left.append(pygame.transform.flip(E2hurt_right[x], True, False))
for x in range(5):
    E2dead_left.append(pygame.transform.flip(E2dead_right[x], True, False))
for x in range(5):
    E2attack1_left.append(pygame.transform.flip(E2attack1_right[x], True, False))
for x in range(4):
    E2attack2_left.append(pygame.transform.flip(E2attack2_right[x], True, False))
for x in range(5):
    E2attack3_left.append(pygame.transform.flip(E2attack3_right[x], True, False))
for x in range(8):
    E2jump_left.append(pygame.transform.flip(E2jump_right[x], True, False))


#Enemy 3
E3run_right = [pygame.image.load('./Enemies/E3/Run/tile000.png'), pygame.image.load('./Enemies/E3/Run/tile001.png'), pygame.image.load('./Enemies/E3/Run/tile002.png'), pygame.image.load('./Enemies/E3/Run/tile003.png'), pygame.image.load('./Enemies/E3/Run/tile004.png'), pygame.image.load('./Enemies/E3/Run/tile005.png'), pygame.image.load('./Enemies/E3/Run/tile006.png')]
E3idle_right = [pygame.image.load('./Enemies/E3/Idle/tile000.png'), pygame.image.load('./Enemies/E3/Idle/tile001.png'), pygame.image.load('./Enemies/E3/Idle/tile002.png'), pygame.image.load('./Enemies/E3/Idle/tile003.png'), pygame.image.load('./Enemies/E3/Idle/tile004.png')]
E3hurt_right = [pygame.image.load('./Enemies/E3/Hurt/tile000.png'), pygame.image.load('./Enemies/E3/Hurt/tile001.png'), pygame.image.load('./Enemies/E3/Hurt/tile002.png')]
E3dead_right = [pygame.image.load('./Enemies/E3/Dead/tile000.png'), pygame.image.load('./Enemies/E3/Dead/tile001.png'), pygame.image.load('./Enemies/E3/Dead/tile002.png'), pygame.image.load('./Enemies/E3/Dead/tile003.png'), pygame.image.load('./Enemies/E3/Dead/tile004.png')]
E3attack1_right = [pygame.image.load('./Enemies/E3/Attack1/tile000.png'), pygame.image.load('./Enemies/E3/Attack1/tile001.png'), pygame.image.load('./Enemies/E3/Attack1/tile002.png'), pygame.image.load('./Enemies/E3/Attack1/tile003.png')]
E3attack2_right = [pygame.image.load('./Enemies/E3/Attack2/tile000.png'), pygame.image.load('./Enemies/E3/Attack2/tile001.png'), pygame.image.load('./Enemies/E3/Attack2/tile002.png'), pygame.image.load('./Enemies/E3/Attack2/tile003.png')]
E3attack3_right = [pygame.image.load('./Enemies/E3/Attack3/tile000.png'), pygame.image.load('./Enemies/E3/Attack3/tile001.png'), pygame.image.load('./Enemies/E3/Attack3/tile002.png'), pygame.image.load('./Enemies/E3/Attack3/tile003.png')]
E3jump_right = [pygame.image.load('./Enemies/E3/Jump/tile000.png'), pygame.image.load('./Enemies/E3/Jump/tile001.png'), pygame.image.load('./Enemies/E3/Jump/tile002.png'), pygame.image.load('./Enemies/E3/Jump/tile003.png'), pygame.image.load('./Enemies/E3/Jump/tile004.png'), pygame.image.load('./Enemies/E3/Jump/tile005.png')]
E3scream_right = [pygame.image.load('./Enemies/E3/Scream/tile000.png'), pygame.image.load('./Enemies/E3/Scream/tile001.png'), pygame.image.load('./Enemies/E3/Scream/tile002.png'), pygame.image.load('./Enemies/E3/Scream/tile003.png'), pygame.image.load('./Enemies/E3/Scream/tile004.png')]

E3run_left = []
E3idle_left = []
E3hurt_left = []
E3dead_left = []
E3attack1_left = []
E3attack2_left = []
E3attack3_left = []
E3jump_left = []
E3scream_left = []


for x in range(7):
    E3run_left.append(pygame.transform.flip(E3run_right[x], True, False))
for x in range(5):
    E3idle_left.append(pygame.transform.flip(E3idle_right[x], True, False))
for x in range(3):
    E3hurt_left.append(pygame.transform.flip(E3hurt_right[x], True, False))
for x in range(5):
    E3dead_left.append(pygame.transform.flip(E3dead_right[x], True, False))
for x in range(4):
    E3attack1_left.append(pygame.transform.flip(E3attack1_right[x], True, False))
for x in range(4):
    E3attack2_left.append(pygame.transform.flip(E3attack2_right[x], True, False))
for x in range(4):
    E3attack3_left.append(pygame.transform.flip(E3attack3_right[x], True, False))
for x in range(6):
    E3jump_left.append(pygame.transform.flip(E3jump_right[x], True, False))
for x in range(5):
    E3scream_left.append(pygame.transform.flip(E3scream_right[x], True, False))

#bullet 
bullet_right = pygame.transform.scale(pygame.image.load('./Bullet/3.png'), (15, 15))
bullet_left = pygame.transform.flip(bullet_right, True, False)

#white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Duum")

#classes and functions
#tem os adornos do mapa
class Others(pygame.sprite.Sprite):
    def __init__(self, number, center):
        super().__init__()
        if number == 11:
            self.image = others[3]
            self.rect = self.image.get_rect()
            self.rect.center = center

        if number == 12:
            self.image = others[1]
            self.rect = self.image.get_rect()
            self.rect.center = center
        
        if number == 13:
            self.image = others[4]
            self.rect = self.image.get_rect()
            self.rect.center = center
        
        if number == 14:
            self.image = others[0]
            self.rect = self.image.get_rect()
            self.rect.center = center

        if number == 15:
            self.image = others[2]
            self.rect = self.image.get_rect()
            self.rect.center = center
        
        if number == 16:
            self.image = others[5]
            self.rect = self.image.get_rect()
            self.rect.center = center
        
        if number == 17:
            self.image = others[6]
            self.rect = self.image.get_rect()
            self.rect.center = center
        
        if number == 18:
            self.image = others[7]
            self.rect = self.image.get_rect()
            self.rect.center = center

#é o chão
class Tiles(pygame.sprite.Sprite):
    def __init__(self, number, center):
        super().__init__()
        if number == 2:
            self.image = tiles[1]
            self.rect = self.image.get_rect()
            self.rect.center = center
        if number == 3: 
            self.image = tiles[2]
            self.rect = self.image.get_rect()
            self.rect.center = center
        if number == 4:
            self.image = tiles[3]
            self.rect = self.image.get_rect()
            self.rect.center = center
        if number == 5:
            self.image = tiles[5]
            self.rect = self.image.get_rect()
            self.rect.center = center
        if number == 6:
            self.image = tiles[4]
            self.rect = self.image.get_rect()
            self.rect.center = center
        if number == 7:
            self.image = tiles[6]
            self.rect = self.image.get_rect()
            self.rect.center = center
        if number == 8:
            self.image = tiles[7]
            self.rect = self.image.get_rect()
            self.rect.center = center
        if number == 9:
            self.image = tiles[8]
            self.rect = self.image.get_rect()
            self.rect.center = center

#deteta os pes do P1, serve para o jogador não ficar no ar quando se colocar num canto dos andares
def detectFeets(rect):
    width = rect.width//4 
    height = rect.height//4
    left = rect.left + 25
    top = rect.top + 60
    return pygame.Rect(left, top, width, height)

#tem a mesma funcionalidade da função anterior, embora, aplicado as imagens dos zombies
def detectFeetsZombie1(rect):
    width = rect.width//4 
    height = rect.height//4
    left = rect.left + 25
    top = rect.top + 50
    return pygame.Rect(left, top, width, height)
    font = pygame.font.SysFont("Normal", 15)
    
#serve para desenhar os botões relativos ao menu 
def draw_button(text, pos_x, pos_y, width, height, countingButton):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (mouse[0] > pos_x and mouse[0] <  pos_x + width) and (mouse[1] > pos_y and mouse[1] < pos_y + height):
        if countingButton[0] == 0:
            pygame.mixer.Sound.play(selecting_sound)
            countingButton[0] = 1
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (pos_x, pos_y, width, height))
        textDone = font.render(text, True, (255 ,255 ,255))
        rect_text = textDone.get_rect()
        rect_text.center = ((pos_x + 120), (pos_y + 23))
        DISPLAYSURF.blit(textDone, rect_text)
        if click[0] == 1:
            pygame.mixer.Sound.play(shoot_sound)
            return 1
        else:
            return 0
    else:
        countingButton[0] = 0
        pygame.draw.rect(DISPLAYSURF, (54, 85, 143), (pos_x, pos_y, width, height))
        textDone = font.render(text, True, (212, 228, 188))
        rect_text = textDone.get_rect()
        rect_text.center = ((pos_x + 120), (pos_y + 23))
        DISPLAYSURF.blit(textDone, rect_text)
        return 0
    
#serve para desenhas os botões que andam para atras
def draw_backbutton(pos_x, pos_y):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect = ARROW.get_rect()
    rect.center = (pos_x, pos_y)

    if (mouse[0] > rect.left and mouse[0] <  rect.left + 50) and (mouse[1] > rect.top and mouse[1] < rect.top + 50):
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), rect, 2)
        DISPLAYSURF.blit(ARROW, rect)
        if click[0]:
            return 1
        else:
            return 0
    else:
        
        DISPLAYSURF.blit(ARROW, rect)
        return 0

    

#é a classe das balas da arma do jogador
class bulletGun(pygame.sprite.Sprite):
    def __init__(self, orientation, player):
        super().__init__()
        self.orientation = orientation
        if orientation == 1:
            self.image = bullet_left
            self.rect = self.image.get_rect()
            self.rect.center = player.rect.center
            self.rect.top = self.rect.top - 5
            self.active = 1
        elif orientation == 0:
            self.image = bullet_right
            self.rect = self.image.get_rect()
            self.rect.center = player.rect.center
            self.rect.top = self.rect.top - 5
            self.active = 1
        else:
            self.active = 0
            return None

    def moveBullet(self):
        if self.orientation == 1:
            self.rect.move_ip(-30, 0)
        else: 
            self.rect.move_ip(30, 0)
    
            
#esta classe é feita para poder referenciar o rect dos pes e não do jogador (pygame não permite que uma classe que herda do Sprites tenha mais do que um rect)
class feet(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = rect

#Classe do inimigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self, orientation, enemy): 
        super().__init__()
        self.orientation = orientation #Serve para orientar ao inimigo ao igual que o P1
        self.enemy = enemy #Serve para saber o tipo do inimigo
        self.indice = 0
        if self.enemy == 1:
            self.animations_left = [E1idle_left, E1run_left, E1jump_left, E1attack1_left, E1attack2_left, E1attack3_left, E1hurt_left, E1dead_left]
            self.animations_right = [E1idle_right, E1run_right, E1jump_right, E1attack1_right, E1attack2_right, E1attack3_right, E1hurt_right, E1dead_right]
            if self.orientation == 1:
                self.image = self.animations_left[0][self.indice]
                self.rect = self.image.get_rect();
                self.feet = feet(detectFeetsZombie1(self.rect))
            else: 
                self.image = self.animations_right[0][self.indice]
                self.rect = self.image.get_rect();
                self.feet = feet(detectFeetsZombie1(self.rect))

        elif self.enemy == 2:
            self.animations_left = [E2idle_left, E2run_left, E2jump_left, E2attack1_left, E2attack2_left, E2attack3_left, E2hurt_left, E2dead_left]
            self.animations_right = [E2idle_right, E2run_right, E2jump_right, E2attack1_right, E2attack2_right, E2attack3_right, E2hurt_right, E2dead_right]
            if self.orientation == 1:
                self.image = self.animations_left[0][self.indice]
                self.rect = self.image.get_rect();
                self.feet = feet(detectFeetsZombie1(self.rect))
            else: 
                self.image = self.animations_right[0][self.indice]
                self.rect = self.image.get_rect();
                self.feet = feet(detectFeetsZombie1(self.rect))
        else: 
            self.animations_left = [E3idle_left, E3run_left, E3jump_left, E3attack1_left, E3attack2_left, E3attack3_left, E3hurt_left, E3dead_left, E3scream_left]
            self.animations_right = [E3idle_right, E3run_right, E3jump_right, E3attack1_right, E3attack2_right, E3attack3_right, E3hurt_right, E3dead_right, E3scream_right]
            if self.orientation == 1:
                self.image = self.animations_left[0][self.indice]
                self.rect = self.image.get_rect();
                self.feet = feet(detectFeetsZombie1(self.rect))
            else: 
                self.image = self.animations_right[0][self.indice]
                self.rect = self.image.get_rect();
                self.feet = feet(detectFeetsZombie1(self.rect))

        if self.orientation == 1:
            self.rect.center = (802, 500)
        else: 
            self.rect.center = (-2, 500)
        self.specificCondition = 0
        self.smooth = 0 #serve para fazer a animacao mais natural
        self.attack = 0 #serve para altenar os combates 
        self.fallingCondition = 0 #serve para a gravidade
        self.jumpingCondition = 0 #serve para indicar ao programa que o inimigo esta a saltar
        self.jumpHeight = 0 #serve para definir a altura do inimigo
        self.vida = 100 #e a vida do inimigo 
        self.playerDead = 0
        self.oldPlayerDead = -1
        self.deadAnimation = 1

    #metodo executado aquando um inimigo morrer
    def dead(self):
        if self.deadAnimation == 1:
            if self.orientation == 1:
                if self.specificCondition < 4:
                    self.image = self.animations_left[7][self.specificCondition]
                    self.rect.size = self.image.get_size()
                    self.specificCondition += 1
                else:
                    self.specificCondition = 0
            else:
                if self.specificCondition < 4:
                    self.image = self.animations_right[7][self.specificCondition]
                    self.rect.size = self.image.get_size()
                    self.specificCondition += 1
            self.deadAnimation = 0
            
        else:
            if self.orientation == 1:
                self.image = self.animations_left[7][3]
                self.rect.size = self.image.get_size()
                self.rect.top = self.rect.top + 10
                self.rect.height = 1
            else:
                self.image = self.animations_right[7][3]
                self.rect.size = self.image.get_size()
                self.rect.top = self.rect.top + 10
                self.rect.height = 1

    #metodo que faz com que os zombies persigam ao jogador
    def track(self, player, EnemyCollidePlayer, EnemyCollideTiles):
        #vida do inimigo 
        pygame.draw.rect(DISPLAYSURF, (255, 0 , 0), (self.rect.x, self.rect.y - 20, self.rect.width, 5))
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (self.rect.x, self.rect.y - 19, self.rect.width * (self.vida/100), 3))
        
        #permite detetar ao jogador 
        dx = player.rect.left - self.rect.left
        
        dy = player.rect.top - self.rect.top 

        #serve para fazer com que o inimigo caia
        if EnemyCollideTiles == 0 and self.jumpingCondition == 0:
            self.fallingCondition = 1 
        
        #serve para fazer com que o inimigo baixe e continue a perseguir ao jogador
        if dy > 15:
            EnemyCollideTiles = 0
            self.fallingCondition = 1


        
        if self.fallingCondition == 0: 
            if self.jumpingCondition == 0: 
                if self.vida > 0 : 
                    if player.deadStatus == 0:
                        if EnemyCollidePlayer == 0: 
                            if dx < -50: #o player esta mais perto do zero do que o inimigo (ou seja a esquerda)
                                if self.enemy == 1: #enemy 1
                                    if self.specificCondition < 8:
                                        self.image = self.animations_left[1][self.specificCondition]
                                        self.rect.size = self.image.get_size()
                                        self.feet = feet(detectFeetsZombie1(self.rect))
                                        self.rect.move_ip(-5,0)
                                        if self.smooth == 1: 
                                            self.specificCondition += 1
                                            self.smooth = 0
                                        else: 
                                            self.smooth += 1
                                    else:
                                        self.specificCondition = 0
                                        self.orientation = 1
                                elif self.enemy == 2: #enemy 2
                                    if self.specificCondition < 7:
                                        self.image = self.animations_left[1][self.specificCondition]
                                        self.rect.size = self.image.get_size()
                                        self.feet = feet(detectFeetsZombie1(self.rect))
                                        self.rect.move_ip(-5,0)
                                        if self.smooth == 1: 
                                            self.specificCondition += 1
                                            self.smooth = 0
                                        else: 
                                            self.smooth += 1
                                    else:
                                        self.specificCondition = 0
                                        self.orientation = 1
                                else: #enemy 3
                                    if self.specificCondition < 7:
                                        self.image = self.animations_left[1][self.specificCondition]
                                        self.rect.size = self.image.get_size()
                                        self.feet = feet(detectFeetsZombie1(self.rect))
                                        self.rect.move_ip(-5,0)
                                        if self.smooth == 1: 
                                            self.specificCondition += 1
                                            self.smooth = 0
                                        else: 
                                            self.smooth += 1
                                    else:
                                        self.specificCondition = 0
                                        self.orientation = 1



                            elif dx > 50:  #o player esta mais longe do zero do que o inimigo (a direita)
                                if self.enemy == 1:
                                    if self.specificCondition < 8:
                                        self.image = self.animations_right[1][self.specificCondition]
                                        self.rect.size = self.image.get_size()
                                        self.feet = feet(detectFeetsZombie1(self.rect))
                                        self.rect.move_ip(5, 0)
                                        if self.smooth == 1: 
                                            self.specificCondition += 1
                                            self.smooth = 0
                                        else: 
                                            self.smooth += 1
                                    else:
                                        self.specificCondition = 0
                                        self.orientation = 0
                                elif self.enemy == 2:
                                    if self.specificCondition < 7:
                                        self.image = self.animations_right[1][self.specificCondition]
                                        self.rect.size = self.image.get_size()
                                        self.feet = feet(detectFeetsZombie1(self.rect))
                                        self.rect.move_ip(5, 0)
                                        if self.smooth == 1: 
                                            self.specificCondition += 1
                                            self.smooth = 0
                                        else: 
                                            self.smooth += 1
                                    else:
                                        self.specificCondition = 0
                                        self.orientation = 0
                                else: 
                                    if self.specificCondition < 7:
                                        self.image = self.animations_right[1][self.specificCondition]
                                        self.rect.size = self.image.get_size()
                                        self.feet = feet(detectFeetsZombie1(self.rect))
                                        self.rect.move_ip(5, 0)
                                        if self.smooth == 1: 
                                            self.specificCondition += 1
                                            self.smooth = 0
                                        else: 
                                            self.smooth += 1
                                    else:
                                        self.specificCondition = 0
                                        self.orientation = 0


                            else: 
                                #o player esta a uma altura diferente do inimigo
                                if dy < 1 and dy > -1 :
                                    # a altura nao e muito (serve para situações especificas o inimigo nao ficar colado)
                                    if self.enemy == 1:
                                        if self.specificCondition < 4:
                                            #o inimigo faz idle
                                            if self.orientation == 1:
                                                self.image = self.animations_left[0][self.specificCondition]
                                                self.rect.size = self.image.get_size()
                                                self.feet = feet(detectFeetsZombie1(self.rect))
                                                self.specificCondition += 1
                                            else:
                                                self.image = self.animations_right[0][self.specificCondition]
                                                self.rect.size = self.image.get_size()
                                                self.feet = feet(detectFeetsZombie1(self.rect))
                                                self.specificCondition += 1
                                        else:
                                            self.specificCondition = 0
                                    elif self.enemy == 2:
                                        if self.specificCondition < 8:
                                            if self.orientation == 1:
                                                self.image = self.animations_left[0][self.specificCondition]
                                                self.rect.size = self.image.get_size()
                                                self.feet = feet(detectFeets(self.rect))
                                                self.specificCondition += 1
                                            else:
                                                self.image = self.animations_right[0][self.specificCondition]
                                                self.rect.size = self.image.get_size()
                                                self.feet = feet(detectFeets(self.rect))
                                                self.specificCondition += 1
                                        else:
                                            self.specificCondition = 0
                                    else:
                                        if self.specificCondition < 4:
                                            if self.orientation == 1:
                                                self.image = self.animations_left[0][self.specificCondition]
                                                self.rect.size = self.image.get_size()
                                                self.feet = feet(detectFeets(self.rect))
                                                self.specificCondition += 1
                                            else:
                                                self.image = self.animations_right[0][self.specificCondition]
                                                self.rect.size = self.image.get_size()
                                                self.feet = feet(detectFeets(self.rect))
                                                self.specificCondition += 1
                                        else:
                                            self.specificCondition = 0

                                else:
                                    #a altura e enorme e o inimigo deve fazer o salto
                                    self.jumpingCondition = 1

                                            
                        else:
                            if self.enemy == 1:
                                if self.attack < 3:
                                    if self.specificCondition < 4:
                                        if dx < 0:
                                            self.image = self.animations_left[self.attack+3][self.specificCondition]
                                            self.rect.size = self.image.get_size()
                                            self.feet = feet(detectFeets(self.rect))
                                            self.specificCondition += 1
                                        if dx > 0:
                                            self.image = self.animations_right[self.attack+3][self.specificCondition]
                                            self.rect.size = self.image.get_size()
                                            self.feet = feet(detectFeets(self.rect))
                                            self.specificCondition += 1
                                        

                                    else:
                                        self.specificCondition = 0
                                        self.attack += 1

                                    player.vida = player.vida - 10

                                else:
                                    self.attack = 0
                            
                            elif self.enemy == 2:
                                if self.attack < 3:
                                    if self.specificCondition < 4:
                                        if dx < 0:
                                            self.image = self.animations_left[self.attack+3][self.specificCondition]
                                            self.rect.size = self.image.get_size()
                                            self.feet = feet(detectFeets(self.rect))
                                            self.specificCondition += 1
                                        if dx > 0:
                                            self.image = self.animations_right[self.attack+3][self.specificCondition]
                                            self.rect.size = self.image.get_size()
                                            self.feet = feet(detectFeets(self.rect))
                                            self.specificCondition += 1
                                    else:
                                        self.specificCondition = 0
                                        self.attack += 1
                                        
                                    player.vida = player.vida - 10

                                else:
                                    self.attack = 0
                            else:
                                if self.attack < 3:
                                    if self.specificCondition < 4:
                                        if dx < 0:
                                            self.image = self.animations_left[self.attack+3][self.specificCondition]
                                            self.rect.size = self.image.get_size()
                                            self.feet = feet(detectFeets(self.rect))
                                            self.specificCondition += 1
                                        if dx > 0:
                                            self.image = self.animations_right[self.attack+3][self.specificCondition]
                                            self.rect.size = self.image.get_size()
                                            self.feet = feet(detectFeets(self.rect))
                                            self.specificCondition += 1
                                    else:
                                        self.specificCondition = 0
                                        self.attack += 1

                                    player.vida = player.vida - 10

                                else:
                                    self.attack = 0
                    else:
                        if self.enemy == 1:
                            if self.specificCondition < 4:
                                if self.orientation == 1:
                                    self.image = self.animations_left[0][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.specificCondition += 1
                                else:
                                    self.image = self.animations_right[0][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.specificCondition += 1
                            else:
                                self.specificCondition = 0

                        elif self.enemy == 2:
                            if self.specificCondition < 8:
                                if self.orientation == 1:
                                    self.image = self.animations_left[0][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeets(self.rect))
                                    self.specificCondition += 1
                                else:
                                    self.image = self.animations_right[0][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeets(self.rect))
                                    self.specificCondition += 1
                            else:
                                self.specificCondition = 0

                        else:
                            if dx < 0:
                                if self.specificCondition < 5:
                                    self.image = self.animations_left[0][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.specificCondition += 1
                                else:
                                    self.specificCondition = 0

                            else:
                                if self.specificCondition < 5:
                                    self.image = self.animations_left[0][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.specificCondition += 1
                                else:
                                    self.specificCondition = 0
                else: 
                    self.dead()



            else: 
                if dy < 0: #o jogador esta acima do inimigo 
                    if dx < 0:
                        #o jogador esta acima do inimigo e a sua esquerda
                        if self.enemy == 1:
                            if self.jumpHeight < 36:
                                if self.specificCondition < 4:  
                                    self.image = self.animations_left[2][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.specificCondition += 1
                                    self.jumpHeight += 1
                                else:
                                    self.image = self.animations_left[2][3]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.jumpHeight += 1
                                    
                            else:
                                self.fallingCondition = 1
                                self.jumpingCondition = 0
                                self.jumpHeight = 0
                                self.specificCondition = 0

                        elif self.enemy == 2:
                            if self.jumpHeight < 36:
                                if self.specificCondition < 7:  
                                    self.image = self.animations_left[2][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.specificCondition += 1
                                    self.jumpHeight += 1
                                else:
                                    self.image = self.animations_left[2][3]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.jumpHeight += 1
                                    
                            else:
                                self.fallingCondition = 1
                                self.jumpingCondition = 0
                                self.jumpHeight = 0
                                self.specificCondition = 0
                        else:
                            if self.jumpHeight < 36:
                                if self.specificCondition < 5:  
                                    self.image = self.animations_left[2][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.specificCondition += 1
                                    self.jumpHeight += 1
                                else:
                                    self.image = self.animations_left[2][3]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.jumpHeight += 1
                            else:
                                self.fallingCondition = 1
                                self.jumpingCondition = 0
                                self.jumpHeight = 0
                                self.specificCondition = 0


                        
                    else: 
                        if self.enemy == 1:
                            if self.jumpHeight < 55:
                                if self.specificCondition < 4:  
                                    self.image = self.animations_right[2][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.specificCondition += 1
                                else:
                                    self.image = self.animations_right[2][3]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                self.jumpHeight += 1
                            else:
                                self.fallingCondition = 1
                                self.jumpingCondition = 0
                                self.jumpHeight = 0
                                self.specificCondition = 0
                        elif self.enemy == 2:
                            if self.jumpHeight < 55:
                                if self.specificCondition < 4:  
                                    self.image = self.animations_right[2][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.specificCondition += 1
                                else:
                                    self.image = self.animations_right[2][3]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                self.jumpHeight += 1
                            else:
                                self.fallingCondition = 1
                                self.jumpingCondition = 0
                                self.jumpHeight = 0
                                self.specificCondition = 0
                        else:
                            if self.jumpHeight < 55:
                                if self.specificCondition < 4:  
                                    self.image = self.animations_right[2][self.specificCondition]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                    self.specificCondition += 1
                                else:
                                    self.image = self.animations_right[2][3]
                                    self.rect.size = self.image.get_size()
                                    self.feet = feet(detectFeetsZombie1(self.rect))
                                    self.rect.move_ip(0, -5)
                                self.jumpHeight += 1
                            else:
                                self.fallingCondition = 1
                                self.jumpingCondition = 0
                                self.jumpHeight = 0
                                self.specificCondition = 0
      
                elif dy > 0: # o jogador esta embaixo de mim 
                    self.fallingCondition = 1
                    self.jumpingCondition = 0
                elif dy == 0 or EnemyCollideTiles == 0: #faz ao inimigo cair quer seja não tenha tocado chão quer seja chegou ate o jogador e deve tocar o chão
                    self.fallingCondition = 1
                    self.jumpingCondition = 0

                
        else:
            #falling
            if EnemyCollideTiles == 0:
                #ainda nao tem tocado o chao
                if self.enemy == 1:
                    if dx > 0:
                        self.image = self.animations_right[2][4]
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeetsZombie1(self.rect))
                        self.rect.move_ip(0, 5)
                    else:
                        self.image = self.animations_left[2][4]
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeetsZombie1(self.rect))
                        self.rect.move_ip(0, 5)
                elif self.enemy == 2:
                    if dx > 0:
                        self.image = self.animations_right[2][4]
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeetsZombie1(self.rect))
                        self.rect.move_ip(0, 5)
                    else:
                        self.image = self.animations_left[2][4]
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeetsZombie1(self.rect))
                        self.rect.move_ip(0, 5)
                else:
                    if dx > 0:
                        self.image = self.animations_right[2][4]
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeetsZombie1(self.rect))
                        self.rect.move_ip(0, 5)
                    else:
                        self.image = self.animations_left[2][4]
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeetsZombie1(self.rect))
                        self.rect.move_ip(0, 5)

            else:
                #tocou o chao
                self.fallingCondition = 0
                if self.specificCondition < 1:
                    if dx > 0:
                        if self.enemy == 1:
                            self.image = self.animations_right[2][self.specificCondition + 5]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeetsZombie1(self.rect))
                            self.specificCondition += 1
                        elif self.enemy == 2:
                            self.image = self.animations_right[2][self.specificCondition + 5]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeetsZombie1(self.rect))
                            self.specificCondition += 1
                        else:
                            self.image = self.animations_right[2][self.specificCondition + 5]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeetsZombie1(self.rect))
                            self.specificCondition += 1

                    elif dx < 0:
                        if self.enemy == 1:
                            self.image = self.animations_left[2][self.specificCondition + 5]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeetsZombie1(self.rect))
                            self.specificCondition += 1
                        elif self.enemy == 2:
                            self.image = self.animations_left[2][self.specificCondition + 5]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeetsZombie1(self.rect))
                            self.specificCondition += 1
                        else:
                            self.image = self.animations_left[2][self.specificCondition + 5]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeetsZombie1(self.rect))
                            self.specificCondition += 1
                
                else:
                    self.jumpingCondition = 0
                    self.specificCondition = 0
        


                       






        
        



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.oldPlayerCollideTiles = 1 #serve para saber se o personagem esteve no chao no ciclo pasado
        self.specificCondition = 0 #serve para o personagem fazer a animacao de tocar o chao e se levantar 
        self.specificConditionJumping = 0 #serve para saber se o personagem ainda ta a efetuar o salto
        self.specificConditionAttack = 0 #serve para saber o estado do ataque 
        self.specificConditionShoot = 0 #serve para saber o estado do disparo
        self.jumpingHeight = 0
        self.fallCondition = 0 #serve para verificar se o personagem esta no ar 
        self.jumpingCondition = 0 #serve para saber se o personagem saltou
        self.attack1Condition = 0 #serve para fazer o ataque numero 1
        self.attack2Condition = 0 #serve para fazer o ataque numero 2
        self.shootCondition = 0 #serve para disparar
        self.rechargeCondition = 0 #serve para carregar a arma
        self.orientation = 1 #serve para saber a orientacao do personagem para left orientation e igual 1 para right e igual a 0
        self.indice = 0
        self.animations_left = [P1idle_left, P1run_left, P1jump_left, P1attack2_left, P1shoot_left, P1attack1_left, P1recharge_left, P1dead_left]
        self.animations_right = [P1idle_right, P1run_right, P1jump_right, P1attack2_right, P1shoot_right, P1attack1_right, P1recharge_right, P1dead_right]
        self.image = self.animations_left[0][self.indice]
        self.rect = self.image.get_rect()
        self.feet = feet(detectFeets(self.rect))
        self.rect.center = (150, 490)
        self.oldKey = 0
        self.shootLeft = 0 #serve para arranjar um bug dos disparos quando o personagem esta orientado para a esquerda
        self.vida = 2000 #e a vida do personagem
        self.deadStatus = 0
        self.deadAnimation = 1
        self.bullet = pygame.sprite.Group()
        self.QtBullets = 18

    def dead(self):
        if self.deadAnimation == 1:
            if self.orientation == 1:
                if self.specificCondition < 4:
                    self.image = self.animations_left[7][self.specificCondition]
                    self.rect.size = self.image.get_size()
                    self.specificCondition += 1
                else:
                    self.specificCondition = 0
            else:
                if self.specificCondition < 4:
                    self.image = self.animations_right[7][self.specificCondition]
                    self.rect.size = self.image.get_size()
                    self.specificCondition += 1
                else:
                    self.specificCondition = 0
            self.deadAnimation = 0
            pygame.mixer.Sound.play(dying_sound)
        else:
            if self.orientation == 1:
                self.image = self.animations_left[7][3]
                self.rect.size = self.image.get_size()
            else:
                self.image = self.animations_right[7][3]
                self.rect.size = self.image.get_size()



    def move(self, playerCollideTiles, deadStatus):
        #vida do jogador
        pygame.draw.rect(DISPLAYSURF, (255, 0 , 0), (self.rect.x, self.rect.y - 20, self.rect.width, 5))
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (self.rect.x, self.rect.y - 19, self.rect.width * (self.vida/2000), 3))
        

        self.deadStatus = deadStatus
        pressed_keys = pygame.key.get_pressed()

        if(playerCollideTiles == 0 and self.jumpingCondition == 0):
            self.fallCondition = 1


        if self.fallCondition == 0 :
            if self.jumpingCondition == 0:
                if self.deadStatus == 0:
                    if self.rechargeCondition == 0:
                        if self.shootCondition == 0:
                            if self.attack1Condition == 0: 
                                if self.attack2Condition == 0: 
                                    if pressed_keys[K_LEFT] or pressed_keys[K_RIGHT] or pressed_keys[K_UP] or pressed_keys[K_x] or pressed_keys[K_z] or pressed_keys[K_c] or pressed_keys[K_r]:
                                            if self.rect.left > 0:
                                                if pressed_keys[K_LEFT]:
                                                    if self.oldKey != K_LEFT:
                                                        self.indice = 0
                                                    else:
                                                        if self.indice > 6:
                                                            self.indice = 0
                                                        else:
                                                            self.indice = self.indice + 1
                                                    self.image = self.animations_left[1][self.indice]
                                                    self.rect.size = self.image.get_size()
                                                    self.feet = feet(detectFeets(self.rect))
                                                    self.rect.move_ip(-10, 0)
                                                    self.oldKey = K_LEFT
                                                    self.orientation = 1

                                        
                                            if self.rect.right < SCREEN_WIDTH:
                                                if pressed_keys[K_RIGHT]:
                                                    if self.oldKey != K_RIGHT:
                                                        self.indice = 0
                                                    else:
                                                        if self.indice > 6:
                                                            self.indice = 0
                                                        else:
                                                            self.indice = self.indice + 1

                                                    self.image = self.animations_right[1][self.indice]
                                                    self.rect.size = self.image.get_size()
                                                    self.feet = feet(detectFeets(self.rect))
                                                    self.rect.move_ip(10,0)
                                                    self.oldKey = K_RIGHT
                                                    self.orientation = 0
                                                

                                            if pressed_keys[K_UP]:
                                                self.jumpingCondition = 1

                                            if pressed_keys[K_z]:
                                                self.attack2Condition = 1

                                            if pressed_keys[K_x]:
                                                self.shootCondition = 1

                                            if pressed_keys[K_c]:
                                                self.attack1Condition = 1
                                            
                                            if pressed_keys[K_r]:
                                                self.rechargeCondition = 1
                                            
                                                
                                        
                                    else:
                                        if self.oldKey != 0:
                                            self.indice = 0
                                        else:
                                            if self.indice > 4:
                                                self.indice = 0
                                            else:
                                                self.indice = self.indice + 1
                                        if self.orientation == 0:
                                            self.image = self.animations_right[0][self.indice]
                                            self.rect.size = self.image.get_size()
                                            self.feet = feet(detectFeets(self.rect))
                                            self.oldKey = 0
                                        else: 
                                            self.image = self.animations_left[0][self.indice]
                                            self.rect.size = self.image.get_size()
                                            self.feet = feet(detectFeets(self.rect))
                                            self.oldKey = 0
                                else:
                                    if self.specificConditionAttack < 3: 
                                        if pressed_keys[K_LEFT]: 
                                            self.image = self.animations_left[3][self.specificConditionAttack]
                                            self.rect.size = self.image.get_size()
                                            self.rect.move_ip(-5, 0)
                                            self.orientation = 1

                                            enemies_beaten = pygame.sprite.spritecollide(P1, enemies_sprites, False)
                                            for enemy in enemies_beaten:
                                                enemy.vida = enemy.vida - 4
                                                pygame.mixer.Sound.play(attack2_sound)

                                            self.specificConditionAttack += 1
                                        elif pressed_keys[K_RIGHT]:
                                            self.image = self.animations_right[3][self.specificConditionAttack]
                                            self.rect.size = self.image.get_size()
                                            self.rect.move_ip(5, 0)
                                            self.orientation = 0

                                            enemies_beaten = pygame.sprite.spritecollide(P1, enemies_sprites, False)
                                            for enemy in enemies_beaten:
                                                enemy.vida = enemy.vida - 4
                                                pygame.mixer.Sound.play(attack2_sound)

                                            self.specificConditionAttack += 1
                                        else: 
                                            if self.orientation == 1:
                                                self.image = self.animations_left[3][self.specificConditionAttack]
                                                self.rect.size = self.image.get_size()
         
                                                enemies_beaten = pygame.sprite.spritecollide(P1, enemies_sprites, False)
                                                for enemy in enemies_beaten:
                                                    enemy.vida = enemy.vida - 4
                                                    pygame.mixer.Sound.play(attack2_sound)

                                                self.specificConditionAttack += 1
                                            else: 
                                                self.image = self.animations_right[3][self.specificConditionAttack]
                                                self.rect.size = self.image.get_size()

                                                enemies_beaten = pygame.sprite.spritecollide(P1, enemies_sprites, False)
                                                for enemy in enemies_beaten:
                                                    enemy.vida = enemy.vida - 4
                                                    pygame.mixer.Sound.play(attack2_sound)

                                                self.specificConditionAttack += 1
                                    else:
                                        self.specificConditionAttack = 0 
                                        self.attack2Condition = 0
                            else: 
                                if self.specificConditionAttack < 6:

                                    if self.orientation == 1:
                                        self.image = self.animations_left[5][self.specificConditionAttack]
                                        self.rect.size = self.image.get_size()

                                        enemies_beaten = pygame.sprite.spritecollide(P1, enemies_sprites, False)
                                        for enemy in enemies_beaten:
                                            enemy.vida = enemy.vida - 6
                                            pygame.mixer.Sound.play(attack1_sound)

                                        self.specificConditionAttack += 1
                                    else: 
                                        self.image = self.animations_right[5][self.specificConditionAttack]
                                        self.rect.size = self.image.get_size()

                                        enemies_beaten = pygame.sprite.spritecollide(P1, enemies_sprites, False)
                                        for enemy in enemies_beaten:
                                            enemy.vida = enemy.vida - 6
                                            pygame.mixer.Sound.play(attack1_sound)

                                        self.specificConditionAttack += 1
                                else: 
                                    self.attack1Condition = 0
                                    self.specificConditionAttack = 0

                        else: #SHOOT
                            if self.QtBullets > 0:
                                
                                if self.specificConditionShoot < 11: 
                                    
                                    if self.specificConditionShoot == 0:
                                        pygame.mixer.Sound.play(shoot_sound)

                                    if self.orientation == 1:
                                        self.shootLeft = 1 #e so para arranjar o bug do disparo 
                                        self.image = self.animations_left[4][self.specificConditionShoot]
                                        self.rect.size = self.image.get_size()
                                        self.rect.width = self.rect.width - 58 
                                        if self.specificConditionShoot == 2:
                                            newBullet = bulletGun(1, self)
                                            self.bullet.add(newBullet)
                                            
                                        self.specificConditionShoot += 1
                                    else: 
                                        self.shootLeft = 0 #e so para arranjar o bud do disparo
                                        self.image = self.animations_right[4][self.specificConditionShoot]
                                        self.rect.size = self.image.get_size()
                                        self.rect.width = self.rect.width - 58 
                                        if self.specificConditionShoot == 2:
                                            newBullet = bulletGun(0, self)
                                            self.bullet.add(newBullet)
                                            

                                        self.specificConditionShoot += 1
                                        
                                            
                                else:
                                    self.specificConditionShoot = 0 
                                    self.QtBullets -= 1
                                    
                                    if self.orientation == 1:
                                        self.image = self.animations_left[0][0]
                                        self.shootLeft = 0
                                        self.shootCondition = 0
                                    else: 
                                        self.image = self.animations_right[0][0]
                                        self.shootLeft = 0
                                        self.shootCondition = 0
                            else:
                                self.specificConditionShoot = 0
                                self.shootLeft = 0
                                self.shootCondition = 0
                                
                                    
                                
                    else: #RECHARGE
                        if self.specificConditionShoot < 11:

                            if self.specificConditionShoot == 2:
                                pygame.mixer.Sound.play(reload_sound)

                            if self.orientation == 1:
                                self.image = self.animations_left[6][self.specificConditionShoot]
                                self.rect.size = self.image.get_size()
                                self.specificConditionShoot += 1
                            else:
                                self.image = self.animations_right[6][self.specificConditionShoot]
                                self.rect.size = self.image.get_size()
                                self.specificConditionShoot += 1
                        else:
                            
                            self.specificConditionShoot = 0 
                            self.rechargeCondition = 0
                            self.QtBullets = 18
                else:
                    self.dead()
                        
                    
            else:
                if self.jumpingHeight < 25:
                    if self.specificConditionJumping < 4: 
                        if pressed_keys[K_LEFT]: 
                            self.image = self.animations_left[2][self.specificConditionJumping + 1]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeets(self.rect))
                            self.rect.move_ip(-10,-10)
                            if pygame.sprite.spritecollideany(P1, tilesGroup):
                                self.rect.move_ip(10,0)
                            self.orientation = 1
                            self.specificConditionJumping += 1
                        elif pressed_keys[K_RIGHT]:
                            self.image = self.animations_right[2][self.specificConditionJumping + 1]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeets(self.rect))
                            self.rect.move_ip(10,-10)
                            if pygame.sprite.spritecollideany(P1, tilesGroup):
                                self.rect.move_ip(10,0)
                            self.orientation = 0
                            self.specificConditionJumping += 1
                        else: 
                            if self.orientation == 1:
                                self.image = self.animations_left[2][self.specificConditionJumping + 1]
                                self.rect.size = self.image.get_size()
                                self.feet = feet(detectFeets(self.rect))
                                self.rect.move_ip(0, -10)
                                self.specificConditionJumping += 1
                            else: 
                                self.image = self.animations_right[2][self.specificConditionJumping + 1]
                                self.rect.size = self.image.get_size()
                                self.feet = feet(detectFeets(self.rect))
                                self.rect.move_ip(0, -10)
                                self.specificConditionJumping += 1
                        self.jumpingHeight += 1

                    else:
                        if pressed_keys[K_LEFT]: 
                            self.image = self.animations_left[2][6]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeets(self.rect))
                            self.rect.move_ip(-10,-10)
                            if pygame.sprite.spritecollideany(P1, tilesGroup):
                                self.rect.move_ip(10,0)
                            self.orientation = 1
                            self.specificConditionJumping += 1
                            self.jumpingHeight += 1
                        elif pressed_keys[K_RIGHT]:
                            self.image = self.animations_right[2][6]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeets(self.rect))
                            self.rect.move_ip(10,-10)
                            if pygame.sprite.spritecollideany(P1, tilesGroup):
                                self.rect.move_ip(-10,0)
                            self.orientation = 0
                            self.specificConditionJumping += 1
                            self.jumpingHeight += 1
                        else: 
                            if self.orientation == 1:
                                self.image = self.animations_left[2][6]
                                self.rect.size = self.image.get_size()
                                self.feet = feet(detectFeets(self.rect))
                                self.rect.move_ip(0, -10)
                                self.jumpingHeight += 1
                            else: 
                                self.image = self.animations_right[2][6]
                                self.rect.size = self.image.get_size()
                                self.feet = feet(detectFeets(self.rect))
                                self.rect.move_ip(0, -10)
                                self.jumpingHeight += 1
                else:    
                    self.specificConditionJumping = 0
                    self.fallCondition = 1 #1
                    self.jumpingHeight = 0
                        

        else:
            if self.jumpingCondition == 1 and self.fallCondition == 1:
                if playerCollideTiles == 0: #enquanto esteja a cair(playerCollideTiles == 0)
                    if self.orientation == 1: #se esta a cair e o utilizador nao toca numa tecla, o personagem fica com esta orientacao
                        self.image = self.animations_left[2][7]
                    else:
                        self.image = self.animations_right[2][7]

                    if pressed_keys[K_LEFT] : #se esta a cair e o utilizador toca a tecla da esquerda fica com esta orientacao
                        self.image = self.animations_left[2][7] 
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeets(self.rect))
                        self.rect.move_ip(-10 , 10)
                        if pygame.sprite.spritecollideany(P1, tilesGroup):
                            self.rect.move_ip(10,0)
                        self.orientation = 1
                    elif pressed_keys[K_RIGHT] : 
                        self.image = self.animations_right[2][7] 
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeets(self.rect))
                        self.rect.move_ip(10 , 10)
                        if pygame.sprite.spritecollideany(P1, tilesGroup):
                            self.rect.move_ip(-10,0)
                        self.orientation = 0
                    else:                     #se o utilizador nao tocar nenhuma tecla o personagem cai so na vertical
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeets(self.rect))
                        self.rect.move_ip(0, 10)
                        
                else: #chegou ao chao e faz a animacao
                    if self.specificCondition < 3:
                        if self.orientation == 1:
                            self.image = self.animations_left[2][8 + self.specificCondition]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeets(self.rect))
                            self.specificCondition += 1
                        else:
                            self.image = self.animations_right[2][8 + self.specificCondition]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeets(self.rect))
                            self.specificCondition += 1
                    else: 
                        self.fallCondition = 0
                        self.specificCondition = 0
                        self.jumpingCondition = 0
            else: 
                if playerCollideTiles != 1:
                    if self.orientation == 1: #se esta a cair e o utilizador nao toca numa tecla, o personagem fica com esta orientacao
                        self.image = self.animations_left[2][7]
                    else:
                        self.image = self.animations_right[2][7]

                    if pressed_keys[K_LEFT] : #se esta a cair e o utilizador toca a tecla da esquerda fica com esta orientacao
                        self.image = self.animations_left[2][7] 
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeets(self.rect))
                        self.rect.move_ip(-5 , 10)
                        if pygame.sprite.spritecollideany(P1, tilesGroup):
                            self.rect.move_ip(5,0)
                        self.orientation = 1
                    elif pressed_keys[K_RIGHT] : 
                        self.image = self.animations_right[2][7] 
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeets(self.rect))
                        self.rect.move_ip(5 , 10)
                        if pygame.sprite.spritecollideany(P1, tilesGroup):
                            self.rect.move_ip(-5,0)
                        self.orientation = 0
                    else:                     #se o utilizador nao tocar nenhuma tecla o personagem cai so na vertical
                        self.rect.size = self.image.get_size()
                        self.feet = feet(detectFeets(self.rect))
                        self.rect.move_ip(0, 10)
                else: 
                    if self.specificCondition < 3:
                        if self.orientation == 1:
                            self.image = self.animations_left[2][8 + self.specificCondition]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeets(self.rect))
                            self.specificCondition += 1
                        else:
                            self.image = self.animations_right[2][8 + self.specificCondition]
                            self.rect.size = self.image.get_size()
                            self.feet = feet(detectFeets(self.rect))
                            self.specificCondition += 1
                    else: 
                        self.fallCondition = 0
                        self.specificCondition = 0
                        self.jumpingCondition = 0

            
                


            
        



#set up world Sprites
tilesGroup = []

othersGroup = []
for y in range(20):
    for x in range(26):
        if world_map[y][x] == 2:
            tilesGroup.append(Tiles(2, (x*32, y*32)))
        if world_map[y][x] == 3:
            othersGroup.append(Tiles(3, (x*32, y*32))) #tileGroup (trocar arranja o erro)
        if world_map[y][x] == 4:
            othersGroup.append(Tiles(4, (x*32, y*32))) #tileGroup (trocar arranja o erro)
        if world_map[y][x] == 5:
            othersGroup.append(Tiles(5, (x*32, y*32))) #tileGroup (trocar arranja o erro)
        if world_map[y][x] == 6:
            othersGroup.append(Tiles(6, (x*32, y*32))) #tileGroup (trocar arranja o erro)
        if world_map[y][x] == 7:
            othersGroup.append(Tiles(7, (x*32, y*32))) #tileGroup (trocar arranja o erro)
        if world_map[y][x] == 8:
            othersGroup.append(Tiles(8, (x*32, y*32))) #tileGroup (trocar arranja o erro)
        if world_map[y][x] == 9:
            othersGroup.append(Tiles(9, (x*32, y*32))) #tileGroup (trocar arranja o erro)0
        if world_map[y][x] == 11:
            othersGroup.append(Others(11, (x*32, y*32)))
        if world_map[y][x] == 12:
            othersGroup.append(Others(12, (x*32, y*32)))
        if world_map[y][x] == 13:
            othersGroup.append(Others(13, (x*32, y*34)))
        if world_map[y][x] == 14:
            othersGroup.append(Others(14, (x*32, y*32)))
        if world_map[y][x] == 15:
            othersGroup.append(Others(15, (x*32, y*32)))
        if world_map[y][x] == 16:
            othersGroup.append(Others(16, (x*32, y*32)))
        if world_map[y][x] == 17:
            othersGroup.append(Others(17, (x*32, y*32.5)))
        if world_map[y][x] == 18:
            othersGroup.append(Others(18, (x*32, y*32)))
        


        





#verifica se esta a tocar o chao 
playerCollideTiles = 0

#verifica se os inimigos estao a tocar o jogador
EnemyCollidePlayer = 0

#verifica se os inimigos estao no chao
EnemyCollideTiles = 0

#Score
scoreNum = 0
scoreText = "Score: "

font = pygame.font.SysFont("Verdana", 26)
text = font.render(scoreText, True, (212, 228, 188))
number = font.render(str(scoreNum), True, (255, 10, 100))

rect_text = text.get_rect()
rect_text.center = (380, 50)
rect_number = number.get_rect()
rect_number.center = (427, 50)


#Save Variable
saved = 1
pygame.mixer.Sound.play(background_sound, -1)
countingButton = [[0], [0], [0], [0]]

while True:
    saved = 0
    DISPLAYSURF.fill(WHITE)
    #background
    for x in range(5):
        DISPLAYSURF.blit(background[x], (0,0))
    pygame.draw.rect(DISPLAYSURF, (150, 172 ,183), (250, 140, 320, 420))
    DISPLAYSURF.blit(GAMENAME, (200, 0))
    
    
    button1 = draw_button("Start", 290, 180, 250, 50, countingButton[0])
    button2 = draw_button("Ranking", 290, 280, 250, 50, countingButton[1])
    button3 = draw_button("Controls", 290, 380, 250, 50, countingButton[2])
    button4 = draw_button("Exit", 290, 480, 250, 50, countingButton[3])

    #events ocurred in a cicle
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if button1 == 1: #opcao 1 do menu (jogo)

        pygame.mixer.Sound.play(go_sound) 

        scoreNum = 0
        number = font.render(str(scoreNum), True, (255, 10, 100))


        P1 = Player()
        E1 = Enemy(1, 1)
        E2 = Enemy(0, 2)
        E3 = Enemy(1, 3)
        E4 = Enemy(0, 1)

        #set up sprites groups
        all_sprites = pygame.sprite.Group()
        all_sprites.add(P1)
        enemies_sprites = pygame.sprite.Group()
        enemies_sprites.add(E1)
        enemies_sprites.add(E2)
        enemies_sprites.add(E3)
        enemies_sprites.add(E4)

        #contador de ciclos
        ciCounter = 0

        #ciclo do jogo 
        while True: 
                           
            ciCounter += 1

            
            if ciCounter > 100:
                E1 = Enemy(1, 1)
                E2 = Enemy(0, 2)
                E3 = Enemy(1, 3)
                E4 = Enemy(0, 1)
                enemies_sprites.add(E1)
                enemies_sprites.add(E2)
                enemies_sprites.add(E3)
                enemies_sprites.add(E4)
                ciCounter = 0

            backButton = 0

            #refresh
            DISPLAYSURF.fill(WHITE)

            #background
            for x in range(5):
                DISPLAYSURF.blit(background[x], (0,0))
            
            #world
            for tile in tilesGroup:
                DISPLAYSURF.blit(tile.image, tile.rect)
            for others in othersGroup:
                DISPLAYSURF.blit(others.image, others.rect)

            #back button 
            backButton = draw_backbutton(50, 50)

            if backButton == 1:
                break

            #events ocurred in a cicly 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


            if pygame.sprite.spritecollideany(P1.feet, tilesGroup):
                playerCollideTiles = 1
            else:
                playerCollideTiles = 0
            
            if P1.vida < 0:
                if ciCounter == 50: 
                    pygame.mixer.Sound.play(gameOver_sound)
                P1.move(playerCollideTiles, 1)
                DISPLAYSURF.blit(P1.image, P1.rect)
                #Game Over
                DISPLAYSURF.blit(GAMEOVER, (200, 110))
                if saved == 0 :
                    with open('score.txt', 'r') as file:
                        lines = file.readlines()
                    if not lines:
                        with open('score.txt', 'w') as file:
                            file.write(str(scoreNum) + '\n')
                            for x in range(4):
                                file.write('0000\n')
                    else:
                        numbers = []
                        for line in lines:
                            num = int(line.strip())
                            numbers.append(num)
                        for x in range(5):
                            if scoreNum > numbers[x]:
                                for y in range(4 - x): 
                                    numbers[4 - y] = numbers[3 - y]
                                numbers[x] = scoreNum
                                break
                        numbersStr = []
                        for x in range(5):
                            numbersStr.append(str(numbers[x]) + '\n')
                        with open('score.txt', 'w') as file:
                            file.writelines(numbersStr)
                        saved = 1
                
                
            else:
                for bullet in P1.bullet:
                    bullet.moveBullet()
                    DISPLAYSURF.blit(bullet.image, bullet.rect)
                    
                P1.move(playerCollideTiles, 0)
                if P1.shootLeft == 1:
                    left = P1.rect.left - 65
                    DISPLAYSURF.blit(P1.image, (left, P1.rect.top))
                else: 
                    DISPLAYSURF.blit(P1.image, P1.rect)
            
            for enemy in enemies_sprites:
                if pygame.sprite.collide_rect(enemy, P1):
                    EnemyCollidePlayer = 1  
                else: 
                    EnemyCollidePlayer = 0
                
                if pygame.sprite.spritecollideany(enemy.feet, tilesGroup):
                    EnemyCollideTiles = 1
                else:
                    EnemyCollideTiles = 0

                if pygame.sprite.spritecollide(enemy, P1.bullet, True):
                    enemy.vida = enemy.vida - 70
                
                if enemy.rect.top > 700: 
                    enemies_sprites.remove(enemy)
                    scoreNum += 1 
                    number = font.render(str(scoreNum), True, (255, 10, 100))


                    
                
                enemy.track(P1, EnemyCollidePlayer, EnemyCollideTiles)
                DISPLAYSURF.blit(enemy.image, enemy.rect)

            #desenha os quadros do score
            pygame.draw.rect(DISPLAYSURF, (150, 172, 183), (305, 15, 180, 70))
            pygame.draw.rect(DISPLAYSURF, (54, 85, 143), (320, 26, 150, 50))
            
            #desenha o score
            DISPLAYSURF.blit(text, rect_text)
            DISPLAYSURF.blit(number, rect_number)
            
            #desenha os quadros da contagem das balas
            pygame.draw.rect(DISPLAYSURF, (150, 172, 183), (600, 15, 180, 70))
            pygame.draw.rect(DISPLAYSURF, (54, 85, 143), (615, 26, 150, 50))

            #desenha a contagem das balas
            if P1.QtBullets > 9:
                for x in range(P1.QtBullets - 9):
                    DISPLAYSURF.blit(BULLET, (625 + (x*15), 35))

                for y in range(9):
                    DISPLAYSURF.blit(BULLET, (625 + (y*15), 55))

            else:
                for y in range(P1.QtBullets):
                    DISPLAYSURF.blit(BULLET, (625 + (y*15), 55))

                


            pygame.display.update()
            FramePerSec.tick(FPS)
    
    #opcao 2 do menu (Ranking)
    elif button2 == 1: 
        while True:
            backButton = 0

            DISPLAYSURF.fill(WHITE)
            for x in range(5):
                DISPLAYSURF.blit(background[x], (0,0))
            DISPLAYSURF.blit(RANKING, (200, 0))
            pygame.draw.rect(DISPLAYSURF, (150, 172 ,183), (250, 140, 320, 420))
            pygame.draw.rect(DISPLAYSURF, (54, 85, 143), (275, 170, 270, 370))

            #back button 
            backButton = draw_backbutton(50, 50)

            if backButton == 1:
                break

            with open('score.txt', 'r') as file:
                lines = file.readlines()
            
            number1 = font.render('1. ', True, (212, 228, 188))
            number2 = font.render('2. ', True, (212, 228, 188))
            number3 = font.render('3. ', True, (212, 228, 188))
            number4 = font.render('4. ', True, (212, 228, 188))
            number5 = font.render('5. ', True, (212, 228, 188))

            DISPLAYSURF.blit(number1, (300, 180))
            DISPLAYSURF.blit(number2, (300, 250))
            DISPLAYSURF.blit(number3, (300, 320))
            DISPLAYSURF.blit(number4, (300, 390))
            DISPLAYSURF.blit(number5, (300, 460))

            score1 = font.render(lines[0].strip(), True, (212, 228, 188))
            score2 = font.render(lines[1].strip(), True, (212, 228, 188))
            score3 = font.render(lines[2].strip(), True, (212, 228, 188))
            score4 = font.render(lines[3].strip(), True, (212, 228, 188))
            score5 = font.render(lines[4].strip(), True, (212, 228, 188))

            DISPLAYSURF.blit(score1, (480, 180))
            DISPLAYSURF.blit(score2, (480, 250))
            DISPLAYSURF.blit(score3, (480, 320))
            DISPLAYSURF.blit(score4, (480, 390))
            DISPLAYSURF.blit(score5, (480, 460))


            #events ocurred in a cicle
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update() 
            FramePerSec.tick(FPS)
    
    elif button3 == 1: #opcao 3 do menu controles
        fontSmaller = pygame.font.SysFont("Verdana", 20)
        while True:
            backButton = 0

            DISPLAYSURF.fill(WHITE)
            for x in range(5):
                DISPLAYSURF.blit(background[x], (0,0))
            DISPLAYSURF.blit(CONTROL, (200, 0))
            pygame.draw.rect(DISPLAYSURF, (150, 172, 183), (250, 140, 320, 420))
            pygame.draw.rect(DISPLAYSURF, (54, 85, 143), (275, 170, 270, 370))

            #back button 
            backButton = draw_backbutton(50, 50)

            if backButton == 1:
                break

            with open('score.txt', 'r') as file:
                lines = file.readlines()
            
            move = fontSmaller.render('Move: ', True, (212, 228, 188))
            jump = fontSmaller.render('Jump: ', True, (212, 228, 188))
            attack1 = fontSmaller.render('Attack1:', True, (212, 228, 188))
            attack2 = fontSmaller.render('Attack2:', True, (212, 228, 188))
            shoot = fontSmaller.render('Shoot: ', True, (212, 228, 188))
            recharge = fontSmaller.render('Recharge:', True, (212, 228, 188))

            DISPLAYSURF.blit(move, (300, 180))
            DISPLAYSURF.blit(jump, (300, 240))
            DISPLAYSURF.blit(attack1, (300, 300))
            DISPLAYSURF.blit(attack2, (300, 360))
            DISPLAYSURF.blit(shoot, (300, 420))
            DISPLAYSURF.blit(recharge, (300, 480))

            attack1Showed = fontSmaller.render('Z', True, (212, 228, 188))
            attack2Showed = fontSmaller.render('C', True, (212, 228, 188))
            shootShowed = fontSmaller.render('X', True, (212, 228, 188))
            rechargeShowed = fontSmaller.render('R', True, (212, 228, 188))

            DISPLAYSURF.blit(RIGHT, (430, 185))
            DISPLAYSURF.blit(LEFT, (480, 185))
            DISPLAYSURF.blit(UP, (480, 240))
            DISPLAYSURF.blit(attack1Showed, (480, 300))
            DISPLAYSURF.blit(attack2Showed, (480, 360))
            DISPLAYSURF.blit(shootShowed, (480, 420))
            DISPLAYSURF.blit(rechargeShowed, (480, 480))

            #events ocurred in a cicle
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            


            pygame.display.update()
            FramePerSec.tick(FPS)


    elif button4 == 1:
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)




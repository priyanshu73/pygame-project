import pygame
import random
import math
from pygame import mixer
#initialize pygame
pygame.init()

#create a screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load('background1.png')

#Title and icon
pygame.display.set_caption('Yeti Yankees')
icon = pygame.image.load('nepal.png')
pygame.display.set_icon(icon)
#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#player
playerimg = pygame.image.load('ship1.png')

playerx = 370
playery = 480
playerx_change = 0
#enemy
enemyimg = pygame.image.load('alien.png')
enemyx = random.randint(0,736)
enemyy = random.randint(0,150)


enemyimg = []
enemyx_change =[]
enemyy_change =[]
enemyx = []
enemyy = []
num_of_enemies = 7
for i in range(num_of_enemies):
    
    enemyimg.append(pygame.image.load('alien.png'))
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(0,100))
    enemyx_change.append(1)
    enemyy_change.append(20)
running = True 


#bullet
bulletimg = pygame.image.load('bullet.png')
bulletx = 370
bullety = 512
bulletx_change = 0
bullety_change = .75
#ready > not moving can't see bullet
#fire > the bullet is movng
bullet_state = 'ready'
#score 
score_value= 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 600
texty = 11
#game over
over_font = pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score = font.render("SCORE: " + str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))
def game_over_text():
    game_over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over_text, (200,250))
def player(x,y):
     screen.blit(playerimg, (x, y))
def enemy(x,y,i):
     screen.blit(enemyimg[i], (x, y))
  
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16,y + 10))
    
def iscollison(a,b,c,d):
    distance = math.sqrt((math.pow(a-c,2))+(math.pow(b-d,2)))
    if distance < 50:
        return True
    else:
        return False


while running:  
    #RGB
    screen.fill((0,0,0))
    #background image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
     #if keystroke check right or left
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
              playerx_change =  -.6
            if event.key == pygame.K_RIGHT:
              playerx_change =  .6
            if event.key == pygame.K_SPACE:
                 if bullet_state is 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    #get the current x cordinate of the ship
                    bulletx = playerx
                    fire_bullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              playerx_change = 0
    
    playerx += playerx_change
    if playerx <= 0 :
        playerx = 0
    elif playerx >=736:
        playerx = 736
    
    for i in range(num_of_enemies):
        
        
        #game over
        if enemyy[i] > 400:
            
            for j in range(num_of_enemies):
                enemyy[j] = 2000 
            game_over_text()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0 :
            enemyx_change[i] = 1
            enemyy[i] += enemyy_change[i] 
        elif enemyx[i]>=736:
            enemyx_change[i] = -1
            enemyy[i] += enemyy_change[i]
  
     #collison   
        collison = iscollison(enemyx[i],enemyy[i],bulletx,bullety)
        if collison == True:
            bullet_sound = mixer.Sound('laser.wav')
            bullet_sound.play()
            bullety = 480
            bullet_state='ready'
            score_value += 1
            
            enemyx[i] = random.randint(0,736)
            enemyy[i]= random.randint(0,100)
        enemy(enemyx[i],enemyy[i],i)
        
      #bullet movement
    if bullety <= 0 :
        bullety = 480
        bullet_state='ready'
    if bullet_state is 'fire':
        bullety -= bullety_change
        fire_bullet(bulletx,bullety)
    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()
    
    
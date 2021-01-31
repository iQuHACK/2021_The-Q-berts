# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import math

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 800])

#background
background = pygame.image.load("spacebackground.PNG")


#player
player_image = pygame.image.load("qbert.PNG")
playerX = 500
playerY = 200
#change in quberts position
x1_change=0
y1_change=0

def player(x,y):
    screen.blit(player_image, (x,y))


#enemy
enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
  enemy_image.append(pygame.image.load("redballenemy.PNG"))
  enemy_image.append(pygame.image.load("blueballenemy.PNG"))
  enemy_image.append(pygame.image.load("snakeenemy.PNG"))
  enemyX.append(random.randint(0,750))
  enemyY.append(random.randint(0,500))
  #change in enemies position
  enemyX_change.append(10)
  enemyY_change.append(10)

 # initial_cube_image = pygame.image.load("cube1.png")

final_cube_image = pygame.image.load("cube2.png")

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))

def isenemyCollision(enemyX, enemyY, playerX, playerY):
  distance = math.sqrt((math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2))))
  if distance < 70:
    return True
  else:
    return False

#game_over_text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
  over_text = over_font.render("Game Over", True, (255, 255, 255))
  screen.blit(over_text, (200, 250))

# Run until the user asks to quit
running = True
while running:

   # Fill the background with white, r, g, b
    screen.fill((255, 200, 255))
    #background
    screen.blit(background, (0,0))


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if keystroke is pressed check whether l or r
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = -10
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 10
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 10
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1_change = 0
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 0
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = 0
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 0
                x1_change = 0
 #changes quberts position if inside bounds
    if playerX>900: 
        playerX=890
    elif playerX<-10:
      playerX=10
    else:
        playerX = playerX + x1_change
    if playerY>700: 
        playerY=690
    elif playerY<-10:
      playerY=10
    else:
        playerY = playerY + y1_change

    for i in range(num_of_enemies):

      enemyX[i] += enemyX_change[i]
      enemyY[i] += enemyY_change[i]
      if enemyX[i] > 900:
        enemyX_change[i] = -10
      elif enemyX[i] < 0:
        enemyX_change[i] = 10
      if enemyY[i] > 700:
        enemyY_change[i] = -10
      elif enemyY[i] < -10:
        enemyY_change[i] = 10
      
      enemycollision = isenemyCollision(enemyX[i], enemyY[i], playerX, playerY)
      if enemycollision:
        game_over_text()
        break

      enemy(enemyX[i], enemyY[i], i)



    player(playerX, playerY)

    # Flip the display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
quit()

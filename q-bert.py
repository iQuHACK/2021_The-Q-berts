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

import os
print(os.environ.get('IONQ_API_KEY'))

%env IONQ_API_KEY = ***************

import numpy as np
from numpy import pi
# import ipywidgets as widgets
# from IPython.display import display
# from qutip import Bloch
import matplotlib
# import time
from qiskit import *
# from qiskit import Aer, execute
from qiskit.tools.visualization import plot_histogram

from qiskit_ionq_provider import IonQProvider

# makes quantum curcuit for the height, bhcircuit = blockHeightCircuit
bhCircuit=QuantumCircuit(3, 3)
bhCircuit.h(1)
bhCircuit.z(1)
bhCircuit.h(0)
bhCircuit.h(2)

# backend_sim = Aer.get_backend('statevector_simulator')
# sim = execute(bhCircuit, backend_sim, shots=5000)
# sim_result = sim.result()
# statevector = sim_result.get_statevector()
# print(statevector)

bhCircuit.draw(output='mpl')

bhCircuit.measure([0,1,2], [0,1,2])

provider = IonQProvider("***************")
backend = provider.get_backend("ionq_qpu")

job = backend.run(bhCircuit)

# backend = Aer.get_backend('qasm_simulator')
# result = execute(bhCircuit, backend = backend, shots = 5000).result()
# counts = result.get_counts()
# print(counts)

# boardspace =[[0, 0, 0, 0, 0, 0, 0], 
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0]]

# plot_histogram(counts)

result = job.result()
plot_histogram(result.get_counts())

#player
player_image = pygame.image.load("qbert.PNG")
playerX = 500
playerY = 200
#change in quberts position
x1_change=0
y1_change=0

def player(x,y):
    screen.blit(player_image, (x,y))
cube1 = pygame.image.load("cube1.png")
cube2 = pygame.image.load("cube1.png")
cube3 = pygame.image.load("cube1.png")
cube4 = pygame.image.load("cube1.png")
cube5 = pygame.image.load("cube1.png")
cube6 = pygame.image.load("cube1.png")
cube7 = pygame.image.load("cube1.png")
cube8 = pygame.image.load("cube1.png")
cube9 = pygame.image.load("cube1.png")
cube10 = pygame.image.load("cube1.png")
cube11 = pygame.image.load("cube1.png")
cube12 = pygame.image.load("cube1.png")
cube13 = pygame.image.load("cube1.png")
cube14 = pygame.image.load("cube1.png")
cube15 = pygame.image.load("cube1.png")
cube16 = pygame.image.load("cube1.png")
cube17 = pygame.image.load("cube1.png")
cube18 = pygame.image.load("cube1.png")
cube19 = pygame.image.load("cube1.png")
cube20 = pygame.image.load("cube1.png")
cube21 = pygame.image.load("cube1.png")
cube22 = pygame.image.load("cube1.png")
cube23 = pygame.image.load("cube1.png")
cube24 = pygame.image.load("cube1.png")
cube25 = pygame.image.load("cube1.png")
hcube1 = pygame.image.load("cube2.png")
hcube2 = pygame.image.load("cube2.png")
hcube3 = pygame.image.load("cube2.png")
hcube4 = pygame.image.load("cube2.png")
hcube5 = pygame.image.load("cube2.png")
hcube6 = pygame.image.load("cube2.png")
hcube7 = pygame.image.load("cube2.png")
hcube8 = pygame.image.load("cube2.png")
hcube9 = pygame.image.load("cube2.png")
hcube10 = pygame.image.load("cube2.png")
hcube11 = pygame.image.load("cube2.png")
hcube12 = pygame.image.load("cube2.png")
hcube13 = pygame.image.load("cube2.png")
hcube14 = pygame.image.load("cube2.png")
hcube15 = pygame.image.load("cube2.png")
hcube16 = pygame.image.load("cube2.png")
hcube17 = pygame.image.load("cube2.png")
hcube18 = pygame.image.load("cube2.png")
hcube19 = pygame.image.load("cube2.png")
hcube20 = pygame.image.load("cube2.png")
hcube21 = pygame.image.load("cube2.png")
hcube22 = pygame.image.load("cube2.png")
hcube23 = pygame.image.load("cube2.png")
hcube24 = pygame.image.load("cube2.png")
hcube25 = pygame.image.load("cube2.png")
cx=[]
cy=[]
for i in range(26):
  
  if i<6:
    cx.append(i)
    cy.append(i)
    cx[i]=20+boardspace[i]+57*i
    cy[i]=300+boardspace[i]+39*i
  elif (i>=6) and (i<11):
    cx.append(i)
    cy.append(i)
    cx[i]=70+boardspace[i]+57*i-278
    cy[i]=200+boardspace[i]+39*i-135
  elif (i>=11) and (i<16):
    cx.append(i)
    cy.append(i)
    cx[i]=120+boardspace[i]+57*i-278*2
    cy[i]=100+boardspace[i]+39*i-135*2
  elif (i>=16) and (i<21):
    cx.append(i)
    cy.append(i)
    cx[i]=170+boardspace[i]+57*i-278*3
    cy[i]=boardspace[i]+39*i-135*3
  elif (i>=21) and (i<26):
    cx.append(i)
    cy.append(i)
    cx[i]=220+boardspace[i]+57*i-278*4
    cy[i]=-100+boardspace[i]+39*i-135*4

screen.blit(cube21,  (cx[21], cy[21]))
screen.blit(cube22,  (cx[22], cy[22]))
screen.blit(cube23,  (cx[23], cy[23]))
screen.blit(cube24,  (cx[24], cy[24]))
screen.blit(cube25,  (cx[25], cy[25]))
screen.blit(cube16,  (cx[16], cy[16]))
screen.blit(cube17,  (cx[17], cy[17]))
screen.blit(cube18,  (cx[18], cy[18]))
screen.blit(cube19,  (cx[19], cy[19]))
screen.blit(cube20,  (cx[20], cy[20]))
screen.blit(cube11,  (cx[11], cy[11]))
screen.blit(cube12,  (cx[12], cy[12]))
screen.blit(cube13,  (cx[13], cy[13]))
screen.blit(cube14,  (cx[14], cy[14]))
screen.blit(cube15,  (cx[15], cy[15]))
screen.blit(cube6,  (cx[6], cy[6]))
screen.blit(cube7,  (cx[7], cy[7]))
screen.blit(cube8,  (cx[8], cy[8]))
screen.blit(cube9,  (cx[9], cy[9]))
screen.blit(cube10,  (cx[10], cy[10]))
screen.blit(cube1,  (cx[1], cy[1]))
screen.blit(cube2,  (cx[2], cy[2]))
screen.blit(cube3,  (cx[3], cy[3]))
screen.blit(cube4,  (cx[4], cy[4]))
screen.blit(cube5,  (cx[5], cy[5]))
 
 




#player
player_image = pygame.image.load("qbert.PNG")
playerX = 370
playerY = 480
#change in quberts position
x1_change=0
y1_change=0



def player(x,y):
    screen.blit(player_image, (x,y))
x1=cx[1]
x2=cx[2]
x3=cx[3]
x4=cx[4]
x5=cx[5]
x6=cx[6]
x7=cx[7]
x8=cx[8]
x9=cx[9]
x10=cx[10]
x11=cx[11]
x12=cx[12]
x13=cx[13]
x14=cx[14]
x15=cx[15]
x16=cx[16]
x17=cx[17]
x18=cx[18]
x19=cx[19]
x20=cx[20]
x21=cx[21]
x22=cx[22]
x23=cx[23]
x24=cx[24]
x25=cx[25]



y1=cy[1]
y2=cy[2]
y3=cy[3]
y4=cy[4]
y5=cy[5]
y6=cy[6]
y7=cy[7]
y8=cy[8]
y9=cy[9]
y10=cy[10]
y11=cy[11]
y12=cy[12]
y13=cy[13]
y14=cy[14]
y15=cy[15]
y16=cy[16]
y17=cy[17]
y18=cy[18]
y19=cy[19]
y20=cy[20]
y21=cy[21]
y22=cy[22]
y23=cy[23]
y24=cy[24]
y25=cy[25]


def iscubeCollision1(x1, y1, playerX, playerY):
  distance = int(math.sqrt((math.pow(x1 - playerX, 2) + (math.pow(y1 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision2 (x2, y2, playerX, playerY):
  distance = int(math.sqrt((math.pow (x2 - playerX, 2) + (math.pow(y2 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision3 (x3, y3, playerX, playerY):
  distance = int(math.sqrt((math.pow(x3 - playerX, 2) + (math.pow(y3 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision4 (x4, y4, playerX, playerY):
  distance = int(math.sqrt((math.pow (x4 - playerX, 2) + (math.pow(y4 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision5 (x5, y5, playerX, playerY):
  distance = int(math.sqrt((math.pow (x5 - playerX, 2) + (math.pow(y5 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision6 (x6, y6, playerX, playerY):
  distance = int(math.sqrt((math.pow (x6 - playerX, 2) + (math.pow(y6 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision7 (x7, y7, playerX, playerY):
  distance = int(math.sqrt((math.pow (x7 - playerX, 2) + (math.pow(y7 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision8 (x8, y8, playerX, playerY):
  distance = int(math.sqrt((math.pow (x8 - playerX, 2) + (math.pow(y8 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision9 (x9, y9, playerX, playerY):
  distance = int(math.sqrt((math.pow (x9 - playerX, 2) + (math.pow(y9 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision10 (x10, y10, playerX, playerY):
  distance = int(math.sqrt((math.pow (x10 - playerX, 2) + (math.pow(y10 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision11 (x11, y11, playerX, playerY):
  distance = int(math.sqrt((math.pow (x11 - playerX, 2) + (math.pow(y11 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision12 (x12, y12, playerX, playerY):
  distance = int(math.sqrt((math.pow (x12 - playerX, 2) + (math.pow(y12 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision13 (x13, y13, playerX, playerY):
  distance = int(math.sqrt((math.pow (x13 - playerX, 2) + (math.pow(y13 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision14 (x14, y14, playerX, playerY):
  distance = int(math.sqrt((math.pow (x14 - playerX, 2) + (math.pow (y14 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision15 (x15, y15, playerX, playerY):
  distance = int(math.sqrt((math.pow (x15 - playerX, 2) + (math.pow(y15 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision16 (x16, y16, playerX, playerY):
  distance = int(math.sqrt((math.pow (x16 - playerX, 2) + (math.pow(y16 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision17 (x17, y17, playerX, playerY):
  distance = int(math.sqrt((math.pow (x17 - playerX, 2) + (math.pow(y17 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision18 (x18, y18, playerX, playerY):
  distance = int(math.sqrt((math.pow (x18 - playerX, 2) + (math.pow(y18 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision19 (x19, y19, playerX, playerY):
  distance = int(math.sqrt((math.pow (x19 - playerX, 2) + (math.pow(y19 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision20 (x20, y20, playerX, playerY):
  distance = int(math.sqrt((math.pow (x20 - playerX, 2) + (math.pow(y20 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision21 (x22, y21, playerX, playerY):
  distance = int(math.sqrt((math.pow (x21 - playerX, 2) + (math.pow(y21 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision22 (x22, y22, playerX, playerY):
  distance = int(math.sqrt((math.pow (x22 - playerX, 2) + (math.pow(y22 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision23 (x23, y23, playerX, playerY):
  distance = int(math.sqrt((math.pow (x23 - playerX, 2) + (math.pow(y23 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision24 (x24, y24, playerX, playerY):
  distance = int(math.sqrt((math.pow (x24 - playerX, 2) + (math.pow(y24 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

def iscubeCollision25 (x25, y25, playerX, playerY):
  distance = int(math.sqrt((math.pow (x25 - playerX, 2) + (math.pow(y25 - playerY, 2)))))
  if distance < 75.0:
    return True
  else:
      return False

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
        #is collision happening?
        
        cubecollision1 = iscubeCollision1(cx[1], cy[1], playerX,playerY)
        if cubecollision1:
           #add change the image
           imgcube1 = pygame.image.load("cube2.png")
        
        cubecollision2 = iscubeCollision2 (cx[2], cy[2], playerX, playerY)
        if cubecollision2:
          #add change the image
          imgcube2 = pygame.image.load("cube2.png")
        
        cubecollision3 = iscubeCollision3 (cx[3], cy[3], playerX, playerY)
        if cubecollision3:
          #add change the image
          imgcube3 = pygame.image.load("cube2.png")
      
        cubecollision4 = iscubeCollision4 (cx[4], cy[4], playerX, playerY)
        if cubecollision4:
          #add change the image
          imgcube4 = pygame.image.load("cube2.png")

        cubecollision5 = iscubeCollision5 (cx[5], cy[5], playerX, playerY) 
        if cubecollision5:
          #add change the image
          imgcube5 = pygame.image.load("cube2.png")
         
        cubecollision6 = iscubeCollision6 (cx[6], cy[6], playerX, playerY) 
        if cubecollision6:
          #add change the image
           imgcube6 = pygame.image.load("cube2.png")
      
        cubecollision7 = iscubeCollision7 (cx[7], cy[7], playerX, playerY)
        if cubecollision7:
          #add change the image
          imgcube7 = pygame.image.load("cube2.png")
 
        cubecollision8 = iscubeCollision8 (cx[8], cy[8], playerX, playerY) 
        if cubecollision8:
          #add change the image
          imgcube8 = pygame.image.load("cube2.png")
 
        cubecollision9 = iscubeCollision9 (cx[8], cy[8], playerX, playerY) 
        if cubecollision9:
          #add change the image
          imgcube9 = pygame.image.load("cube2.png")
 
        cubecollision10 = iscubeCollision10 (cx[10], cy[10], playerX, playerY) 
        if cubecollision10:
          #add change the image
          imgcube10 = pygame.image.load("cube2.png")
        
        cubecollision11 = iscubeCollision11 (cx[11], cy[11], playerX, playerY) 
        if cubecollision11:
          #add change the image
          imgcube11 = pygame.image.load("cube2.png")
      
        cubecollision12 = iscubeCollision12 (cx[12], cy[12], playerX, playerY)
        if cubecollision12:
          #add change the image
          imgcube12 = pygame.image.load("cube2.png")
 
        cubecollision13 = iscubeCollision13 (cx[13], cy[13], playerX, playerY)
        if cubecollision13:
          #add change the image
          imgcube13 = pygame.image.load("cube2.png")
          
        cubecollision14 = iscubeCollision14 (cx[14], cy[14], playerX, playerY)
        if cubecollision14:
          #add change the image
          imgcube14 = pygame.image.load("cube2.png")
 
        cubecollision15 = iscubeCollision15 (cx[15], cy[15], playerX, playerY)
        if cubecollision15:
          #add change the image
          imgcube15 = pygame.image.load("cube2.png")
 
        cubecollision16 = iscubeCollision16 (cx[16], cy[16], playerX, playerY)
        if cubecollision16:
          #add change the image
          imgcube16 = pygame.image.load("cube2.png")
      
        cubecollision17 = iscubeCollision17 (cx[17], cy[17], playerX, playerY)
        if cubecollision17:
          #add change the image
          imgcube17 = pygame.image.load("cube2.png")
 
        cubecollision18 = iscubeCollision18 (cx[18], cy[18], playerX, playerY)
        if cubecollision18:
          #add change the image
          imgcube18 = pygame.image.load("cube2.png")
 
        cubecollision19 = iscubeCollision19 (cx[19], cy[19], playerX, playerY)
        if cubecollision19:
          #add change the image
          imgcube19 = pygame.image.load("cube2.png")
 
        cubecollision20 = iscubeCollision20 (cx[20], cy[20], playerX, playerY)
        if cubecollision20:
          #add change the image
          imgcube20 = pygame.image.load("cube2.png")
 
        cubecollision21 = iscubeCollision21 (cx[21], cy[21], playerX, playerY)
        if cubecollision21:
          #add change the image
          imgcube21 = pygame.image.load("cube2.png")
 
        cubecollision22 = iscubeCollision22 (cx[22], cy[22], playerX, playerY)
        if cubecollision22:
          #add change the image
          imgcube22 = pygame.image.load("cube2.png")
 
        cubecollision23 = iscubeCollision23 (cx[23], cy[23], playerX, playerY)
        if cubecollision23:
          #add change the image
          imgcube23 = pygame.image.load("cube2.png")
 
        cubecollision24 = iscubeCollision24 (cx[24], cy[24], playerX, playerY)
        if cubecollision24:
          #add change the image
          imgcube24 = pygame.image.load("cube2.png")
 
        cubecollision25 = iscubeCollision25 (cx[25], cy[25], playerX, playerY)
        if cubecollision25:
          #add change the image
          imgcube25 = pygame.image.load("cube2.png")
 
 
 




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

    
    
    
    player(playerX, playerY)

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

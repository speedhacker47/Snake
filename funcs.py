import pygame
import sys

pygame.init()

def check_pressed_key():
    press , hold =  [False,False,False,False] , [False,False,False,False] #right , left , up , down
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                
                sys.exit()
        if event.type == pygame.KEYDOWN:  #check anyone pressed the key
            if event.key == pygame.K_UP:   #check for a specific Key
                press[2] = True
                
            elif event.key == pygame.K_DOWN:
                press[3] = True
            elif event.key == pygame.K_LEFT:
                press[1] = True
            elif event.key == pygame.K_RIGHT:
                press[0] = True
    return press

def hold_keys():
    hold = [False,False,False,False]
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
               sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
         hold[0] = True
    elif keys[pygame.K_LEFT]:
         hold[1] = True
    elif keys[pygame.K_UP]:
         hold[2] = True
    elif keys[pygame.K_DOWN]:
         hold[3] = True
    return hold 

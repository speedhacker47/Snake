import pygame
import sys

pygame.init()

def check_pressed_key():    # Self Explainatry             
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                
                sys.exit()
        if event.type == pygame.KEYDOWN:  #check anyone pressed the key
            if event.key == pygame.K_UP:   #check for a specific Key
                print("up")
                return 'u'
            elif event.key == pygame.K_DOWN:
                print('down')
                return 'd'
            elif event.key == pygame.K_LEFT:
                print('left')
                return 'l'
            elif event.key == pygame.K_RIGHT:
                print('right')
                return 'r'
            else:
                 return None

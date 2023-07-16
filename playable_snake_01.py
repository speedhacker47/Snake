import pygame
import sys
from funcs import check_pressed_key   # i put some functions in other python file so that actual code is less messy

#Variables
width , height , border = 500,500 ,50

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

win = pygame.display.set_mode((width,height)) # store window in a variable

FPS = 144
clock = pygame.time.Clock()
exit = False

dir = 'r'
speed = 50

class square():              #MAking class so i can assign properties to variables like snake haead and tail
    def __init__(self,x,y):
        self.x = x              # x,y are coordinate of square shape in 2D space , both value starts from zero from top left
        self.y = y

head = square(border,border)                  # snake head with innitial position

def draw():                
    win.fill(black)
    pygame.draw.rect(win,red,(head.x,head.y,20,20))              
    pygame.display.update()    #Update the drawing changes made since last time


def run_game():         # Head function to run the game
    while True:         #this loop will continue until you press exit , breaking this loop cause closing the window
        clock.tick(60)
        update_snake_pos()      #first we will update snake pos 
        draw()                  # Then draw it

        
def update_snake_pos():   # Update All whole snake's positions
    k = check_pressed_key()
    if k == 'r' and head.x < width-border : head.x += speed
    elif k == 'l' and head.x > border: head.x -= speed
    elif k == 'u' and head.y > border : head.y -= speed
    elif k == 'd' and head.y < height-border : head.y += speed  

run_game() #Run
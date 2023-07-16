import pygame
import sys
from funcs import check_pressed_key
from funcs import hold_keys   # i put some functions in other python file so that actual code is less messy

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

dim = 20 #snake dimension

dir = 'right'  #Initial Direction of head
speed = 5

class square():              #MAking class so i can assign properties to variables like snake haead and tail
    def __init__(self,x,y):
        self.x = x              # x,y are coordinate of square shape in 2D space , both value starts from zero from top left
        self.y = y

head = square(border,border)                  # snake head with innitial position

def draw():                
    win.fill(black)

    pygame.draw.rect(win,red,(head.x,head.y,dim,dim)) #Drawing Snake HEad

    pygame.draw.aaline(win,white,(border,-100),(border,height+100))  #Drawing Borders
    pygame.draw.aaline(win,white,(-100,border),(width+100,border))
    pygame.draw.aaline(win,white,(width-border,-100),(width-border,height+100))
    pygame.draw.aaline(win,white,(-100,height-border),(width+100,height-border))             

    pygame.display.update()    #Update the drawing changes made since last time


def run_game():         # Head function to run the game
    while True:         #this loop will continue until you press exit , breaking this loop cause closing the window
        clock.tick(60)
        check_head_direction()
        update_snake_pos()      #first we will update snake pos 
        draw()                  # Then draw it

        
def update_snake_pos():
    global dir
    print(dir)
    if dir == 'right' and head.x < width-border-dim : head.x += speed
    elif dir == 'left' and head.x > border: head.x -= speed
    elif dir == 'up' and head.y > border : head.y -= speed
    elif dir == 'down' and head.y < height-border-dim : head.y += speed  

def check_head_direction():
    global dir
    k = check_pressed_key()
    if k[0] : dir = 'right'
    elif k[1] : dir = 'left'
    elif k[2] : dir = 'up'
    elif k[3] : dir = 'down'

run_game() #Run
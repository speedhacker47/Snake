import pygame
import sys     # i put some functions in other python file so that actual code is less messy
from funcs import check_pressed_key,hold_keys,collision   
import random

#Variables
width , height , border = 600,600 ,40

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
speed = 20

class square():              #MAking class so i can assign properties to variables like snake haead and tail
    def __init__(self,x,y):
        self.x = x              # x,y are coordinate of square shape in 2D space , both value starts from zero from top left
        self.y = y

head = square(border,border)
food = square(random.randrange(border,width-border-dim,dim),random.randrange(border,height-border-dim,dim))                  # snake head with innitial position
tails = []

def draw_grid():
    block_size = dim
    for x in range(border,width-border,block_size):
        for y in range(border,height-border,block_size):
            pygame.draw.rect(win,(90,90,90),(x,y,block_size,block_size),1)

def draw():                
    win.fill(black)
    draw_grid()
    pygame.draw.rect(win,green,(head.x,head.y,dim,dim))
    pygame.draw.rect(win,red,(food.x,food.y,dim,dim))
    pygame.draw.rect(win,white,(border,border,width-2*border,height-2*border),1)

    for i in range(len(tails)):
        pygame.draw.rect(win,white,(tails[i].x,tails[i].y,dim,dim))

    pygame.display.update()

def run_game():         # Head function to run the game
    while True:         #this loop will continue until you press exit , breaking this loop cause closing the window
        pygame.time.delay(100)
        check_head_direction()
        update_tail_pos()
        update_snake_pos()
        update_food()      #first we will update snake pos 
        draw()                  # Then draw it

        
def update_snake_pos():
    global dir
    if dir == 'right' and head.x < width-border-dim : head.x += speed
    elif dir == 'left' and head.x > border: head.x -= speed
    elif dir == 'up' and head.y > border : head.y -= speed
    elif dir == 'down' and head.y < height-border-dim : head.y += speed  

def check_head_direction():
    global dir
    k = check_pressed_key()
    if k[0] and dir is not 'left': dir = 'right'
    elif k[1] and dir is not 'right': dir = 'left'
    elif k[2] and dir is not 'down': dir = 'up'
    elif k[3] and dir is not 'up': dir = 'down'

def update_food():
    while True:
        if collision(food,head):
            make_tails()
            food.x = random.randrange(border,width-border-dim,dim)
            food.y = random.randrange(border,height-border-dim,dim)
        if (food.x,food.y) != (head.x,head.y):
            break
    #make_tails()
t = 0

def make_tails():
    global t
    if t == 0 : globals()[f"tail_{t}"] = square(head.x,head.y)
    else: globals()[f"tail_{t}"] = square(tails[-1].x,tails[-1].y)
    tails.append(eval(f"tail_{t}"))
    t += 1
    print(len(tails))
    print(t)
    print(tails[0].x,tails[0].y)

def update_tail_pos():
    for i in range(len(tails)):
        print(i)
        if i == 0: tails[i].x,tails[i].y = head.x,head.y
        else: tails[-i].x , tails[-i].y = tails[-i-1].x , tails[-i-1].y
    



run_game() #Run
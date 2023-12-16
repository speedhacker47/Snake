import pygame
from pygame import mixer
import sys     # i put some functions in other python file so that actual code is less messy
from functions import check_pressed_key,hold_keys,collision   
import random
import os

mixer.init()
music_folder = os.path.dirname(os.path.realpath(sys.argv[0]))
game_over = mixer.Sound(os.path.join(music_folder,"game_over.mp3"))
food_sound = mixer.Sound("food.mp3")
mixer.music.set_volume(1.0)

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
speed_of_game = 100   # Less Value Faster Speed

dim = 20 #snake dimension

dir = 'right'  #Initial Direction of head
speed = 20

highest_score = 0

class square():              #MAking class so i can assign properties to variables like snake haead and tail
    def __init__(self,x,y):
        self.x = x              # x,y are coordinate of square shape in 2D space , both value starts from zero from top left
        self.y = y

head = square(border+dim,border+dim)  #Dont Start game with border position (Game Over bug)
food = square(random.randrange(border,width-border-dim,dim),random.randrange(border,height-border-dim,dim))                  # snake head with innitial position
tails = [head]

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
    create_and_draw_texts()

    for i in range(1,len(tails)):
        pygame.draw.rect(win,white,(tails[i].x,tails[i].y,dim,dim))
        pygame.draw.rect(win,blue,(tails[i].x,tails[i].y,dim,dim),1)  #tail border

def run_game():                 # Head function to run the game
    global speed_of_game         
    while True:                     # This loop will continue until you press exit , breaking this loop cause closing the window
        hold_speed_increase()         # Extra Feature
        pygame.time.delay(speed_of_game) 
        check_head_direction()
        update_tail_pos()
        update_snake_pos()
        update_food()      #first we will update snake pos 
        draw()              # Then draw it
        #create_and_draw_texts()
        check_game_over()
        speed_of_game = 100                  
        pygame.display.update() # Update the screen and make all changes since last update
        
def update_snake_pos():          # Update the snake position by seeing situation
    global dir
    if dir == 'right' and head.x <= width-border-dim : head.x += speed
    elif dir == 'left' and head.x >= border: head.x -= speed
    elif dir == 'up' and head.y >= border : head.y -= speed
    elif dir == 'down' and head.y <= height-border-dim : head.y += speed  

def check_head_direction():      #Controls direction of head i.e snake
    global dir
    global speed_of_game
    k = check_pressed_key()
    if k[0] and dir is not 'left': dir = 'right'
    elif k[1] and dir is not 'right': dir = 'left'
    elif k[2] and dir is not 'down': dir = 'up'
    elif k[3] and dir is not 'up': dir = 'down'

def update_food():       # Update food position if eaten food
    while True:
        if collision(food,head):
            mixer.Sound.play(food_sound)
            make_tails()
            food.x = random.randrange(border,width-border-dim,dim)
            food.y = random.randrange(border,height-border-dim,dim)
        if (food.x,food.y) != (head.x,head.y):
            break    
t = 1

def make_tails():      # Create tails
    global t
    globals()[f"tail_{t}"] = square(tails[-1].x,tails[-1].y) # make tails with name like tail_1,tail_2 etc. then.... 
    tails.append(eval(f"tail_{t}"))                          # ...put them in tails[] list every tail is of class square 
    t += 1

def update_tail_pos():              #Update all tails postitions 
    for i in range(1,len(tails)):
        tails[-i].x , tails[-i].y = tails[-i-1].x , tails[-i-1].y # gives all tail position of its previous one
    
def hold_speed_increase():  # Just Extra feature
    global speed_of_game
    global dir
    speed_of_game = 100
    get = hold_keys()
    if (dir == 'right' and get[0]) or (dir == 'left' and get[1]):
        speed_of_game = speed_of_game - 40
    elif (dir == 'up' and get[2]) or (dir == 'down' and get[3]):
        speed_of_game -= 40

def check_game_over():
    global tails ,t ,dir ,highest_score
    over = False

    for i in range(2,len(tails)):  #CHeck if head is touching any of tails
        if (head.x,head.y) == (tails[i].x,tails[i].y):
            over = True      

    if head.x <= border-dim or head.x >= width-border: #check snake is crossing border
        if dir == 'right' or dir == 'left':
            over = True
    elif head.y <= border-dim or head.y >= height-border:
        if dir == 'up' or dir == 'down':
            over = True

    if over :
        mixer.Sound.play(game_over)            # it does WHat happens if game over 
        font = pygame.font.SysFont('comicsans', 30, True)
        for q in [5,4,3,2,1]:
            draw()
            text_2 = font.render("GAME OVER", 1,red)
            win.blit(text_2,(width/3,height-40))
            text_3 = font.render(str(q), 1,white)
            win.blit(text_3,(width/2,0))
            pygame.display.update()
            pygame.time.delay(1000)

        if highest_score < len(tails): highest_score = len(tails)
        tails = [head]
        head.x = head.y = border+2*dim
        t = 1
        dir = 'right'

def create_and_draw_texts():            # WIll Handle texts on screen
    font = pygame.font.SysFont('comicsans', 15, True)
    text = font.render("Score "+str(len(tails)-1), 1,(255,255,255))
    win.blit(text, (10,0))
    text2 = font.render("Highest Score "+ str(highest_score), 1,(255,255,255))
    win.blit(text2, (10,20))

if __name__ == "__main__":
    run_game() #Run
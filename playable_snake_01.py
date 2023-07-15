import pygame

#Variables

width , height = 500 , 500

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (255,255,255)
white = (0,0,0)

win = pygame.display.set_mode((width,height)) # store window in a variable

FPS = 144
clock = pygame.time.Clock()
exit = False

def draw():                
    win.fill(black)              
    pygame.display.update()    #Update the drawing changes made since last time


def run_game():         # Head function to run the game
    global exit
    while exit == False:    #this loop will continue until you press exit , breaking this loop cause closing the window
        clock.tick(FPS)
        p = check_pressed_key()
        draw()
    pygame.quit()
        
def check_pressed_key():    # Self Explainatry
    global exit              
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit = True
        if event.type == pygame.KEYDOWN:  #check anyone pressed the key
            if event.key == pygame.K_UP:   #check for a specific Key
                print("double u")
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
run_game()

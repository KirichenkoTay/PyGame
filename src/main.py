import pygame                                 
import random
import os

from pygame import draw

WIDTH  = 1280                                                                                  
HEIGHT = 960                                                                                 
FPS    = 60                                                                                

# создаем игру и окно

COLOR               = (23, 233, 89)                                                         
SIZE_Y              = 120                                                                       
SIZE_X              = 240                                                                
LOWER_Y_BORDER      = 500                                                                     
X_PIVOT_OF_NEW_FLAT = 300                                                                    
Y_PIVOT_OF_NEW_FLAT = 180                                                           
CENTER              = 520                                                            
DOWN_MOVE           = 4                                                                       
xMOVE               = -10                                                        
BUILD_DOWN_MOVE     = 0.2                                                         

COORDS_Y_1_FLAT     = 620                                                                      
COORDS_Y_2_FLAT     = 740                                                                   
COORDS_Y_3_FLAT     = 860                                                                     

global x_current, y_current                                                                    
global img_size_x, img_size_y
global score

def CheckIvent ():                                                                          
    for event in pygame.event.get():                                                           
        if event.type == pygame.QUIT:                                       
            os.abort ()
        if event.type == pygame.KEYDOWN:                                                      
            if event.key == pygame.K_ESCAPE:    
                os.abort ()
            elif event.key == pygame.K_SPACE:                                                 
                return True
            elif event.key == pygame.K_r:                                                 
                return -1
            elif event.key == pygame.K_1:                                           
                pygame.mixer.music.pause()
            elif event.key == pygame.K_2:                                                   
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(0.5)  
            elif event.key == pygame.K_3:                                                    
                pygame.mixer.music.unpause()    
                pygame.mixer.music.set_volume(1)
    return False                                                                             

def FlatCut (coord_x_flat_1):                                                                 
    global x_current, img_size_x                                                        

    if x_current < coord_x_flat_1:                                                           
        img_size_x = img_size_x - (coord_x_flat_1 - x_current)                                
        return coord_x_flat_1
    elif x_current > coord_x_flat_1:                                                     
        img_size_x = img_size_x - (x_current - coord_x_flat_1)
        return x_current
    else:
        return x_current                                                           
    
def GameOver ():                                                                               
    game_is_vse = pygame.font.Font ("inc/Texts/CubicPixel.otf", 150)                      
    vse_surf  = game_is_vse.render (f"Game Over!", False, (255, 13, 10))                   

    over_score_text = pygame.font.Font ("inc/Texts/CubicPixel.otf", 100)
    text_surf  = over_score_text.render (f"Your score: {score}", False, (255, 255, 255))

    retry_text_surf = pygame.font.Font ("inc/Texts/CubicPixel.otf", 50)
    text_retry = retry_text_surf.render ("To play again press \"R\"", False, (255, 255, 255))

    screen.blit (backfront, (0, 0))                                                        

    screen.blit (vse_surf, (300, 300))                                                    
    screen.blit (text_surf, (350, 500))                                                                                             
    screen.blit (text_retry, (400, 700))                                                    

    pygame.display.flip ()                                                                    
    while True:                                                                             
        res = CheckIvent ()

        if res == -1:
            __main__ ()                                                                      
            return

def __main__ ():
    global x_current, y_current                                                        
    global img_size_x, img_size_y
    global score, xMOVE

    score = 0                                                                             

    score_text = pygame.font.Font ("inc/Texts/CubicPixel.otf", 75)                     
    text_surf  = score_text.render (f"Your score: {score}", False, (255, 255, 255))

    y_current   = Y_PIVOT_OF_NEW_FLAT                                                        
    x_current   = X_PIVOT_OF_NEW_FLAT                                                           

    img_size_x = SIZE_X                                                                    
    img_size_y = SIZE_Y                                                             

    pygame.mixer.music.load("inc/Sounds/Subway.mp3")                                   
    pygame.mixer.music.play(-1)                                                        

    flat1 = pygame.image.load ("inc/Imgs/flat.png").convert ()                             
    flat1 = pygame.transform.scale(flat1, (img_size_x, img_size_y))                       

    flat2 = pygame.image.load ("inc/Imgs/flat2.jpg").convert ()                             
    flat2 = pygame.transform.scale(flat2, (img_size_x, img_size_y))  

    flat3 = pygame.image.load ("inc/Imgs/flat3.jpg").convert ()                             
    flat3 = pygame.transform.scale(flat3, (img_size_x, img_size_y))             

    flat4 = pygame.image.load ("inc/Imgs/flat4.jpg").convert ()                             
    flat4 = pygame.transform.scale(flat4, (img_size_x, img_size_y))  

    flat5 = pygame.image.load ("inc/Imgs/flat5.jpg").convert ()                             
    flat5 = pygame.transform.scale(flat5, (img_size_x, img_size_y))  

    flat = flat1                                                                          

    key_pressed = False                                                                      
    go_down     = False                                                                    

    screen.blit (backfront, (0, 0))                                                            

    coord_y_flat_1 = COORDS_Y_1_FLAT                                                            
    coord_y_flat_2 = COORDS_Y_2_FLAT                                                         
    coord_y_flat_3 = COORDS_Y_3_FLAT                                                        

    coord_x_flat_1 = CENTER                                                                                                             
    coord_x_flat_2 = CENTER
    coord_x_flat_3 = CENTER

    screen_flat_1 = flat3                                                                     
    screen_flat_2 = flat1                                                                    
    screen_flat_3 = flat5

    screen.blit (screen_flat_1, (coord_x_flat_1, coord_y_flat_1))                              
    screen.blit (screen_flat_2, (coord_x_flat_2, coord_y_flat_2))
    screen.blit (screen_flat_3, (coord_x_flat_3, coord_y_flat_3))

    screen.blit (text_surf, (430, 100))                                                     

    while True:                                                                     
        if go_down:                                                                           
            if coord_y_flat_2 >= COORDS_Y_3_FLAT:                                             
                go_down       = False

                coord_x_flat_3 = coord_x_flat_2                                                 
                coord_x_flat_2 = coord_x_flat_1
                coord_x_flat_1 = new_x_coord_flat_1

                coord_y_flat_1 = COORDS_Y_1_FLAT                                               
                coord_y_flat_2 = COORDS_Y_2_FLAT
                coord_y_flat_3 = COORDS_Y_3_FLAT

                screen_flat_3 = screen_flat_2                                                
                screen_flat_2 = screen_flat_1

                screen_flat_1 = pygame.transform.scale(flat, (img_size_x, img_size_y))        

                y_current     = Y_PIVOT_OF_NEW_FLAT                                           
                x_current     = X_PIVOT_OF_NEW_FLAT

                num = random.randint (1, 5)                                                  

                if num == 1:
                    flat = pygame.transform.scale(flat1, (img_size_x, img_size_y))          
                elif num == 2:
                    flat = pygame.transform.scale(flat2, (img_size_x, img_size_y))
                elif num == 3:
                    flat = pygame.transform.scale(flat3, (img_size_x, img_size_y))
                elif num == 4:
                    flat = pygame.transform.scale(flat4, (img_size_x, img_size_y))
                elif num == 5:
                    flat = pygame.transform.scale(flat5, (img_size_x, img_size_y))

                continue                                                                       
            else:
                screen.blit (backfront, (0, 0))                                           

                screen.blit (screen_flat_1, (coord_x_flat_1, coord_y_flat_1))  
                screen.blit (screen_flat_2, (coord_x_flat_2, coord_y_flat_2))
                screen.blit (screen_flat_3, (coord_x_flat_3, coord_y_flat_3))

                screen.blit (flat, (new_x_coord_flat_1, y_current))                          

                screen.blit (text_surf, (430, 100))                                          

                coord_y_flat_1 += BUILD_DOWN_MOVE                                              
                coord_y_flat_2 += BUILD_DOWN_MOVE
                coord_y_flat_3 += BUILD_DOWN_MOVE
                y_current      += BUILD_DOWN_MOVE

                pygame.display.flip ()                                                         

                continue
        elif key_pressed == True:                                                               
            if y_current >= LOWER_Y_BORDER:                                                    
                key_pressed = False                                                             

                new_x_coord_flat_1 = FlatCut (coord_x_flat_1)                            

                if img_size_x <= 0:                                                           
                    GameOver ()
                    return 0
                
                flat = pygame.transform.scale (flat, (img_size_x, img_size_y))                  

                score = score + 1                                                     
                text_surf  = score_text.render (f"Your score: {score}", False, (255, 255, 255)) 

                screen.blit (flat, (new_x_coord_flat_1, y_current))                            

                go_down = True                                                                  

                continue                                                               
                
            y_current += DOWN_MOVE                                                            
        else:
            key_pressed = CheckIvent ()                                                     

        if key_pressed  == False:                                                           
            x_current += xMOVE        

        if x_current >= WIDTH - img_size_x:                                           
            xMOVE = -xMOVE
        elif x_current <= 0:
            xMOVE = abs (xMOVE) 

        screen.blit (backfront, (0, 0))                                                     

        screen.blit (screen_flat_1, (coord_x_flat_1, coord_y_flat_1))                    
        screen.blit (screen_flat_2, (coord_x_flat_2, coord_y_flat_2))
        screen.blit (screen_flat_3, (coord_x_flat_3, coord_y_flat_3))

        screen.blit (flat, (x_current, y_current))                                           

        screen.blit (text_surf, (430, 100))                                           
        
        pygame.display.flip ()                                                               

        clock.tick (FPS)                                                                        

pygame.init()                                                                           
pygame.mixer.init()                                                                      

screen = pygame.display.set_mode((WIDTH, HEIGHT))                                          

pygame.display.set_caption("Bild your home!")                                              

clock = pygame.time.Clock()                                                                  

backfront  = pygame.image.load("inc/Imgs/backgraund.png").convert ()                         

screen.blit (backfront, (0, 0))                                                              

__main__ ()                                                                               
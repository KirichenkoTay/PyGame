import pygame                                                                                   # Import libraries
import random
import os

from pygame import draw

WIDTH  = 1280                                                                                   # Width of the game window
HEIGHT = 960                                                                                    # Height of the game window
FPS    = 60                                                                                     # Frames per second

# Create the game and window

COLOR               = (23, 233, 89)                                                             # Color of the apartment
SIZE_Y              = 120                                                                       # Height of the apartment
SIZE_X              = 240                                                                       # Width of the apartment
LOWER_Y_BORDER      = 500                                                                       # Boundary where previous apartments stand
X_PIVOT_OF_NEW_FLAT = 300                                                                       # X coordinate where apartments appear
Y_PIVOT_OF_NEW_FLAT = 180                                                                       # Y coordinate where apartments appear
CENTER              = 520                                                                       # Coordinate where the building is centered
DOWN_MOVE           = 4                                                                         # Speed of downward movement
xMOVE               = -10                                                                       # Speed of movement along the X coordinate
BUILD_DOWN_MOVE     = 0.2                                                                       # Speed of the whole building moving down

COORDS_Y_1_FLAT     = 620                                                                       # Y coordinate of the 1st floor (the floor that is already in the building)
COORDS_Y_2_FLAT     = 740                                                                       # Y coordinate of the 2nd floor (the floor that is already in the building)
COORDS_Y_3_FLAT     = 860                                                                       # Y coordinate of the 3rd floor (the floor that is already in the building)

global x_current, y_current                                                                     # Declare variables as global, because otherwise you couldn't think of how to do it
global img_size_x, img_size_y
global score

def CheckIvent ():                                                                              # Function checks what the user pressed and if they pressed anything at all
    for event in pygame.event.get():                                                            # Iterate through each event, that is, each key pressed, mouse click
        if event.type == pygame.QUIT:                                                           # If the user entered QUIT, then exit
            os.abort ()
        if event.type == pygame.KEYDOWN:                                                        # If the user pressed Escape, then exit
            if event.key == pygame.K_ESCAPE:    
                os.abort ()
            elif event.key == pygame.K_SPACE:                                                   # If the user pressed space, return True, True is also = 1
                return True
            elif event.key == pygame.K_r:                                                       # If the user pressed "R", return -1
                return -1
            elif event.key == pygame.K_1:                                                       # If you press 1, it will pause the music
                pygame.mixer.music.pause()
            elif event.key == pygame.K_2:                                                       # If you press 2, it will unpause, lower the volume
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(0.5)  
            elif event.key == pygame.K_3:                                                       # If you press 3, it will unpause, increase the volume
                pygame.mixer.music.unpause()    
                pygame.mixer.music.set_volume(1)
    return False                                                                                # If none of the conditions fit, return False = 0

def FlatCut(coord_x_flat_1):                                                                    # Function that handles the falling floor
    global x_current, flat_size_x                                                               # Indicating that these variables are declared globally

    if x_current < coord_x_flat_1:
        flat_size_x = flat_size_x - (coord_x_flat_1 - x_current)                                # Determines where the house fell. If it's slightly closer to the start of the tower, this applies
        return coord_x_flat_1
    elif x_current > coord_x_flat_1:                                                            # If it's past the start of the tower, then this applies
        flat_size_x = flat_size_x - (x_current - coord_x_flat_1)
        return x_current
    else:
        return x_current                                                                        # Function returns the position on X
    
def GameOver():                                                                                 # Function that is called at the end of the game when the player loses
    game_is_vse = pygame.font.Font("inc/Texts/CubicPixel.otf", 150)                             # Initialize the font. The path 'inc' is the file path, the rest is the size
    vse_surf  = game_is_vse.render(f"Game Over!", False, (255, 13, 10))                         # Now set the text, antialiasing = False, color

    over_score_text = pygame.font.Font("inc/Texts/CubicPixel.otf", 100)
    text_surf  = over_score_text.render(f"Your score: {score}", False, (255, 255, 255))

    retry_text_surf = pygame.font.Font("inc/Texts/CubicPixel.otf", 50)
    text_retry = retry_text_surf.render("To play again press \"R\"", False, (255, 255, 255))

    screen.blit(backfront, (0, 0))                                                              # Clear the screen of everything that was there before

    screen.blit(vse_surf, (300, 300))                                                           # Render "Game Over" on the screen
    screen.blit(text_surf, (350, 500))                                                          # Render Score on the screen                                                         
    screen.blit(text_retry, (400, 700))                                                         # Render "To play press R" on the screen

    pygame.display.flip()                                                                       # Update the screen for the user

    while True:                                                                                 # Continuously check if the user pressed something
        res = CheckIvent()

        if res == -1:
            __main__()                                                                          # If pressed, call main where the game starts
            return

def __main__():
    global x_current, y_current                                                                 # Declare which variables are global
    global flat_size_x, flat_size_y
    global score, xMOVE

    score = 0                                                                                   # Player's score

    score_text = pygame.font.Font("inc/Texts/CubicPixel.otf", 75)                               # Text, as mentioned earlier
    text_surf  = score_text.render(f"Your score: {score}", False, (255, 255, 255))

    y_current   = Y_PIVOT_OF_NEW_FLAT                                                           # Variable that stores the current position on Y
    x_current   = X_PIVOT_OF_NEW_FLAT                                                           # Variable that stores the current position on X

    flat_size_x = SIZE_X                                                                        # Size of the flat image on X
    flat_size_y = SIZE_Y                                                                        # Size of the flat image on Y

    pygame.mixer.music.load("inc/Sounds/Subway.mp3")                                            # Loads audio
    pygame.mixer.music.play(-1)                                                                 # Loops the audio, as -1 is specified

    flat1 = pygame.image.load ("inc/Imgs/flat.png").convert ()                                  # Load images of flat variants
    flat1 = pygame.transform.scale(flat1, (flat_size_x, flat_size_y))                           # Set the initial size of each flat

    flat2 = pygame.image.load ("inc/Imgs/flat2.jpg").convert ()                             
    flat2 = pygame.transform.scale(flat2, (flat_size_x, flat_size_y))  

    flat3 = pygame.image.load ("inc/Imgs/flat3.jpg").convert ()                             
    flat3 = pygame.transform.scale(flat3, (flat_size_x, flat_size_y))             

    flat4 = pygame.image.load ("inc/Imgs/flat4.jpg").convert ()                             
    flat4 = pygame.transform.scale(flat4, (flat_size_x, flat_size_y))  

    flat5 = pygame.image.load ("inc/Imgs/flat5.jpg").convert ()                             
    flat5 = pygame.transform.scale(flat5, (flat_size_x, flat_size_y))  

    flat = flat1                                                                                # Our flat - it can change, so its skin is a variable

    key_pressed = False                                                                         # Boolean variable (can be only True = 1 or False = 0), indicates if the user has pressed a key
    go_down     = False                                                                         # Indicates if the entire column of flats is moving down, also a boolean

    screen.blit (backfront, (0, 0))                                                             # Clear the screen

    coord_y_flat_1 = COORDS_Y_1_FLAT                                                            # Initial coordinates of the highest flat in the tower on Y
    coord_y_flat_2 = COORDS_Y_2_FLAT                                                            # Initial coordinates of the middle flat in the tower on Y
    coord_y_flat_3 = COORDS_Y_3_FLAT                                                            # Initial coordinates of the lowest flat in the tower on Y

    coord_x_flat_1 = CENTER                                                                     # Initial coordinates of the corresponding flats on X                                              
    coord_x_flat_2 = CENTER
    coord_x_flat_3 = CENTER

    screen_flat_1 = flat3                                                                       # These are variables. They will change when your block falls
    screen_flat_2 = flat1                                                                       # The reason they have these values now is just the initial value set randomly
    screen_flat_3 = flat5

    # This is the function This is what is displayed These are the coordinates of what is displayed
    screen.blit (screen_flat_1, (coord_x_flat_1, coord_y_flat_1))                               # Render the flats on the screen
    screen.blit (screen_flat_2, (coord_x_flat_2, coord_y_flat_2))
    screen.blit (screen_flat_3, (coord_x_flat_3, coord_y_flat_3))

    screen.blit (text_surf, (430, 100))                                                         # Place the text

    while True:                                                                                 # Enter the loop
        if go_down:                                                                             # Marker for when your flat is falling
            if coord_y_flat_2 >= COORDS_Y_3_FLAT:                                               # If the coordinate of the second floor has become that of the third floor, then
                go_down       = False

                coord_x_flat_3 = coord_x_flat_2                                                 # Change 2 -> 3, 1 -> 2, the flat that is falling -> becomes the first floor
                coord_x_flat_2 = coord_x_flat_1
                coord_x_flat_1 = new_x_coord_flat_1

                coord_y_flat_1 = COORDS_Y_1_FLAT                                                # Align the Y coordinates of the flats
                coord_y_flat_2 = COORDS_Y_2_FLAT
                coord_y_flat_3 = COORDS_Y_3_FLAT

                screen_flat_3 = screen_flat_2                                                   # Change the values of the variables
                screen_flat_2 = screen_flat_1

                screen_flat_1 = pygame.transform.scale(flat, (flat_size_x, flat_size_y))        # Draw our new first floor on the screen

                y_current     = Y_PIVOT_OF_NEW_FLAT                                             # Reset the coordinates of the moving floor to the standard ones
                x_current     = X_PIVOT_OF_NEW_FLAT

                num = random.randint (1, 5)                                                     # Randomly choose a number from 1 to 5 to select a new skin for the floor

                if num == 1:
                    flat = pygame.transform.scale(flat1, (flat_size_x, flat_size_y))            # transform - changes the image size
                elif num == 2:
                    flat = pygame.transform.scale(flat2, (flat_size_x, flat_size_y))
                elif num == 3:
                    flat = pygame.transform.scale(flat3, (flat_size_x, flat_size_y))
                elif num == 4:
                    flat = pygame.transform.scale(flat4, (flat_size_x, flat_size_y))
                elif num == 5:
                    flat = pygame.transform.scale(flat5, (flat_size_x, flat_size_y))

                continue                                                                        # Next iteration of the loop
            else:
                screen.blit (backfront, (0, 0))                                                 # Update the screen

                screen.blit (screen_flat_1, (coord_x_flat_1, coord_y_flat_1))                   # Draw the floors
                screen.blit (screen_flat_2, (coord_x_flat_2, coord_y_flat_2))
                screen.blit (screen_flat_3, (coord_x_flat_3, coord_y_flat_3))

                screen.blit (flat, (new_x_coord_flat_1, y_current))                             # Our fallen floor

                screen.blit (text_surf, (430, 100))                                             # Display the score text on the screen

                coord_y_flat_1 += BUILD_DOWN_MOVE                                               # Move all floors slightly down the screen
                coord_y_flat_2 += BUILD_DOWN_MOVE
                coord_y_flat_3 += BUILD_DOWN_MOVE
                y_current      += BUILD_DOWN_MOVE

                pygame.display.flip ()                                                          # Show the result of this iteration to the user

                continue
        elif key_pressed == True:                                                               # If the user pressed the spacebar
            if y_current >= LOWER_Y_BORDER:                                                     # If our floor has already dropped to the level of the upper standing floor, enter if
                key_pressed = False                                                             # Remove the marker indicating the user pressed a key

                new_x_coord_flat_1 = FlatCut (coord_x_flat_1)                                   # Cut the image

                if flat_size_x <= 0:                                                            # If the size of the flat has become 0, the user loses
                    GameOver ()
                    return 0
                    
                flat = pygame.transform.scale (flat, (flat_size_x, flat_size_y))                # Otherwise change the size to the one that has been cut

                score = score + 1                                                               # +1 to the score
                text_surf  = score_text.render (f"Your score: {score}", False, (255, 255, 255)) # Display the score

                screen.blit (flat, (new_x_coord_flat_1, y_current))                             # Display the new floor of the flat on the screen

                go_down = True                                                                  # Indicate that our building will now be descending

                continue                                                                        # Next iteration
                
            y_current += DOWN_MOVE                                                              # If the flat has not yet reached the building, lower it down
        else:
            key_pressed = CheckIvent ()                                                         # If none of the above conditions are true, check what the user is inputting

        if key_pressed  == False:                                                               # If the user hasn't pressed any useful keys, move the flat horizontally
            x_current += xMOVE        

        if x_current >= WIDTH - flat_size_x:                                                    # If the flat has reached the edge of the screen, change the direction of movement
            xMOVE = -xMOVE
        elif x_current <= 0:
            xMOVE = abs (xMOVE) 

        screen.blit (backfront, (0, 0))                                                         # Clear the screen

        screen.blit (screen_flat_1, (coord_x_flat_1, coord_y_flat_1))                           # Redraw the building
        screen.blit (screen_flat_2, (coord_x_flat_2, coord_y_flat_2))
        screen.blit (screen_flat_3, (coord_x_flat_3, coord_y_flat_3))

        screen.blit (flat, (x_current, y_current))                                              # Draw the flat

        screen.blit (text_surf, (430, 100))                                                     # Write the text

        pygame.display.flip ()                                                                  # Output everything to the user

        clock.tick (FPS)                                                                        # Controls the number of FPS (frames per second, the number of screen updates per second)

pygame.init()                                                                                   # Initialize the game

pygame.mixer.init()                                                                             # Initialize sound

screen = pygame.display.set_mode((WIDTH, HEIGHT))                                               # Create the window

pygame.display.set_caption("Build your home!")                                                  # Title of the game

clock = pygame.time.Clock()                                                                     # To ensure the game runs at a specified frame rate

backfront  = pygame.image.load("inc/Imgs/background.png").convert ()                            # Load the background

screen.blit (backfront, (0, 0))                                                                 # Draw the background

__main__ ()                                                                                     # Start the game
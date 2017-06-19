# Import the required libraries
import pygame
import random 

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128,128,128) 
ORANGE = (255,165,0)
BLUE_1 = (102, 204, 255)
BLUE_2 = (0, 102, 204)

# Draws a spaceship!
def draw_spaceship(screen, x, y):
    # Main Body
    pygame.draw.rect(screen, GREY, [x , y, 50, 50])
    
    # Left Wing
    pygame.draw.polygon(screen, GREY, [[x,y+20],[x-25,y+50],[x,y+50]])
    
    # Right Wing
    pygame.draw.polygon(screen, GREY, [[x+50,y+20],[x+80,y+50],[x+50,y+50]])
    
    # Head
    pygame.draw.polygon(screen, GREY, [[x+25, y-25],[x,y],[x+50,y]])
    
    # Jet fire
    pygame.draw.ellipse(screen, ORANGE, [x,y+45,15,15])
    pygame.draw.ellipse(screen, ORANGE, [x+35,y+45,15,15])
    
# Draws a blue planet!
def draw_blue_planet(screen, x, y):
    # Outline
    pygame.draw.ellipse(screen, BLUE_1, [x,y,100,100])
                        
    # Main Body
    pygame.draw.ellipse(screen, BLUE_2, [x+8.5,y+9,85,85])
    
    # Details
    pygame.draw.ellipse(screen, BLUE_1, [x+14,y+19,30,30])
    
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("SPAAAAAACE")

# Create an empty array for stars
stars = []

# Loop until the user clicks the close button.
done = False

# Places stars in random areas
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    stars.append([x, y]) 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# Speed in pixels per frame
x_speed = 0
y_speed = 0    
# Initial position
x_coord = 10
y_coord = 10
    
# -------- Main Program Loop ----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
     
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0            
    # --- Game logic should go here
    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed    
    # Game logic
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]    
    
    # Checks to make sure the object does not go out of bounds
    if x_coord > 600:
        x_coord = 600
    if x_coord < 0:
        x_coord = 0
    if y_coord > 400:
        y_coord = 400
    if y_coord < 0:
        y_coord = 0
        
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for i in range(len(stars)):
        # Draw the stars
        pygame.draw.circle(screen, WHITE, stars[i], 2)  
        
    draw_spaceship(screen, x,y)
    draw_blue_planet(screen, x_coord, y_coord)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

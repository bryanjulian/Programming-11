import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 153, 255)
GREY = (217, 217, 217)
PI = 3.14159265359
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bryan's Drawing")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, (0, 153, 51), [0, 450, 700, 100])
    pygame.draw.rect(screen, WHITE, [0, 400, 700, 50])
    for y_offset in range(150, 400, 20):
        pygame.draw.ellipse(screen, GREY, [65, 50, 100, 70])
        pygame.draw.ellipse(screen, GREY, [30, 80, 100, 70])
        pygame.draw.ellipse(screen, GREY, [85, 75, 100, 70])  
        pygame.draw.line(screen, WHITE, [100, y_offset],[110, y_offset-10],4)
        pygame.draw.line(screen, WHITE, [110, y_offset],[100, y_offset-10],4)
    for y_offset in range(150, 400, 20):
        pygame.draw.ellipse(screen, GREY, [465, 50, 100, 70])
        pygame.draw.ellipse(screen, GREY, [430, 80, 100, 70])
        pygame.draw.ellipse(screen, GREY, [485, 75, 100, 70])  
        pygame.draw.line(screen, WHITE, [500, y_offset],[510, y_offset-10],4)
        pygame.draw.line(screen, WHITE, [510, y_offset],[500, y_offset-10],4)
    font = pygame.font.SysFont('Calibri', 50, True, False)
    text = font.render("SNOW!!", True, WHITE)
    screen.blit(text, [225, 150])
    pygame.draw.polygon(screen, WHITE, [[100, 350], [0, 450], [200, 450]])
    pygame.draw.ellipse(screen, WHITE, [445, 360, 140, 90])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
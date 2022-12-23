import pygame
from pygame.surface import Surface

# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 000, 255))


    # Draw a solid blue circle in the center
    b = Surface((61, 61), flags=pygame.SRCALPHA)
    b.fill((255, 255, 255, 0))
    pygame.draw.circle(b, (0, 255, 200), (30, 30), 30)

    screen.blit(b, (-100, -100))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
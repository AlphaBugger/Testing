import pygame
import sys
from Rects import Rect

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Your Pygame Title")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
myRect = Rect(400,300, 32, 32, BLACK)
myRects = (Rect(200,300, 32, 32, BLACK),Rect(100,150, 32, 32, BLACK),Rect(16,16, 32, 32, BLACK),Rect(30,300, 32, 32, BLACK))
platform = Rect(0, 600-32, 800,32, (255, 0, 0))
# Set up game variables
# Add any variables specific to your game here

# Main game loop
def main():
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update game state
        # Add any game state updates here

        # Draw everything
        window.fill(WHITE)  # Fill the window with white
        # Add any drawing code here
        myRect.update()
        for rects in myRects:
            rects.update()
            rects.draw(window)
        myRect.draw(window)
        platform.draw(window)
        # Update the display
        pygame.display.update()

        # Cap the frame rate
        pygame.time.Clock().tick(60)  # Adjust the argument to set the desired frame rate

if __name__ == "__main__":
    main()

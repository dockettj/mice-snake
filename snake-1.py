# Step 1: Imports
import pygame
import sys
import random
import time

# Step 2: Design the window
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

# Step 3: Make a mechanism for the game to exist
window.fill((225,225,225))
pygame.display.set_caption("Snake | Score : ")
pygame.display.flip()
fps.tick(15)

# Step 4: Test. Screen will flash, but nothing will show up.
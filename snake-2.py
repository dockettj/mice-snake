import pygame
import sys
import random
import time

# Step 1: Create our snake class and define the snakes head and body
class Snake():
	def __init__(self):
		self.position = [100,50]
		self.body = [[100,50],[90,50],[80,50]]
		self.direction = "RIGHT"
		self.changeDirectionTo = self.direction
	def getHeadPos(self):
		return self.position    
	def getBody(self):
		return self.body
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

# Step 2: Define the snake
snake = Snake()

# Step 3: Make a way to close the game
def gameOver():
	pygame.quit()
	sys.exit()

# Step 4: Make the game stay up until we close the game
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver() 
	window.fill((225,225,225))

	# Step 5: Draw the snake on the screen
	for pos in snake.getBody():
		pygame.draw.rect(window,(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
  
	pygame.display.set_caption("Snake | Score : ")
	pygame.display.flip()
	fps.tick(15)

# Step 6: Test. You will now have a screen with a grey background and green snake that does not move.

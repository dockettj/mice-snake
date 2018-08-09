import pygame
import sys
import random
import time

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

# Step 1: Create our Food Spawner class and designate where the food can go.
class FoodSpawner():
	def __init__(self):
		self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
		self.isFoodOnScreen = True

# Step 2: Add a piece of food if there is not one.
	def spawnFood(self):
		if self.isFoodOnScreen == False:
			self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
			self.isFoodOnScreen = True
		return self.position

	# Step 3: This will be used to determin whether or not food is on the screen
	def setFoodOnScreen(self,b):
		self.isFoodOnScreen = b

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

snake = Snake()

# Step 4: Define the Food Spawner
foodSpawner = FoodSpawner()

def gameOver():
	pygame.quit()
	sys.exit()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver() 

	# Step 5: Set foodPos to wherever the food was placed
	foodPos = foodSpawner.spawnFood()

	window.fill((225,225,225))
	for pos in snake.getBody():
		pygame.draw.rect(window,(0,225,0),pygame.Rect(pos[0],pos[1],10,10))

	# Step 6: Draw the food on the screen.
	pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1],10,10))
	
	pygame.display.set_caption("Snake | Score : ")
	pygame.display.flip()
	fps.tick(15)

# Step 7: Test. You will now have a screen with a grey background and green snake
#		  and a red food. Neither are interactive yet.
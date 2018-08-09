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

	# Step 1: Set the rules for how the snake can turn
	def changeDirTo(self,dir):
		if dir=="RIGHT" and not self.direction=="LEFT":
			self.direction = "RIGHT"
		if dir=="LEFT" and not self.direction=="RIGHT":
			self.direction = "LEFT"
		if dir=="UP" and not self.direction=="DOWN":
			self.direction = "UP"
		if dir=="DOWN" and not self.direction=="UP":
			self.direction = "DOWN"

	# Step 2: Set the rules for how the snake moves depending on it's direction
	def move(self,foodPos):
		if self.direction=="RIGHT":
			self.position[0] += 10
		if self.direction=="LEFT":
			self.position[0] -= 10
		if self.direction=="UP":
			self.position[1] -= 10
		if self.direction=="DOWN":
			self.position[1] += 10

		# Step 3: Add one to the snakes body if it hits a food 	
		self.body.insert(0,list(self.position))
		if self.position == foodPos:
			return 1
		else:
			self.body.pop()
			return 0

	def getHeadPos(self):
		return self.position    
	def getBody(self):
		return self.body

class FoodSpawner():
	def __init__(self):
		self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
		self.isFoodOnScreen = True

	def spawnFood(self):
		if self.isFoodOnScreen == False:
			self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
			self.isFoodOnScreen = True
		return self.position
	
	def setFoodOnScreen(self,b):
		self.isFoodOnScreen = b


window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

snake = Snake()
foodSpawner = FoodSpawner()

def gameOver():
	pygame.quit()
	sys.exit()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver()

		# Step 4: Make the snake move a direction based on key press
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				snake.changeDirTo("RIGHT")
			if event.key == pygame.K_s:
				snake.changeDirTo("DOWN")
			if event.key == pygame.K_a:
				snake.changeDirTo("LEFT")
			if event.key == pygame.K_w:
				snake.changeDirTo("UP")
	foodPos = foodSpawner.spawnFood()

	# Step 5: If the snake hits food and then create a new piece of food
	if(snake.move(foodPos)==1):
		foodSpawner.setFoodOnScreen(False)

	window.fill((225,225,225))
	for pos in snake.getBody():
		pygame.draw.rect(window,(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
	pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1],10,10))
	pygame.display.set_caption("Snake | Score : ")
	pygame.display.flip()
	fps.tick(15)

# Step 6: Test. The snake will now move and food will disappear when touched.
#			    The snake will get longer when it eats food.
#				The snake is able to go off the edge of the screen.
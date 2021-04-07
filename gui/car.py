import pygame
from pygame.math import Vector2

class Car(object):

	def __init__(self, game, position):

		#Init
		self.game = game
		self.size = (8,8)
		self.position = position
		self.velocity = Vector2(0, 0) # pixel per sec [p/s]
		self.acceleration = Vector2(0, 0) # pixel^2 per sec [p^2/s] 
		self.speed = 1
		
	def add_force(self, force):
		self.acceleration += force

	def tick(self):

		#Input
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_w]:
			self.add_force(Vector2(0, -self.speed))
		if pressed[pygame.K_s]:
			self.add_force(Vector2(0, self.speed))
		if pressed[pygame.K_a]:
			self.add_force(Vector2(-self.speed, 0))
		if pressed[pygame.K_d]:
			self.add_force(Vector2(self.speed, 0))

		# Phisics
		self.velocity *= 0.8
		self.velocity += self.acceleration
		old_position = self.position
		new_position = self.position + self.velocity
  
		print(new_position.x, new_position.y)
  
		if (self.game.map.board[int(new_position.x)][int(new_position.y)] != 1):
			self.position = old_position
		else:
			self.position = new_position
			
			
   
		self.position = Vector2(list(map(lambda x: round(x), self.position)))
		#print("VAULE: ", self.game.map.board[int(self.position.x) - 1][int(self.position.y) - 1])
		self.acceleration *= 0.0

  

	def draw(self):

		#Drawing
		rect = pygame.Rect(self.position.x, self.position.y, self.size[0], self.size[1])
		pygame.draw.rect(self.game.screen, (0, 0, 255), rect)

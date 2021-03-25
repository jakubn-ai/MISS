import pygame
from pygame.math import Vector2

class Car(object):

	def __init__(self, game):

		#Init
		self.game = game
		self.size = self.game.screen.get_size()
		self.position = Vector2(self.size[0]/2, self.size[1]/2) # pixel
		self.velocity = Vector2(0, 0) # pixel per sec [p/s]
		self.acceleration = Vector2(0, 0) # pixel^2 per sec [p^2/s] 
		self.speed = 1.3
		

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
		self.position += self.velocity
		self.acceleration *= 0

	def draw(self):

		#Drawing
		rect = pygame.Rect(self.position.x, self.position.y, 10, 10)
		pygame.draw.rect(self.game.screen, (0, 150, 255), rect)
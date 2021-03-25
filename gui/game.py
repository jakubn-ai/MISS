import random
import time
import threading
import pygame
import sys
from car import Car


class Game(object):

	def __init__(self, tps, res):

		# Config
		self.tps = tps
		self.res = res

		# Init
		pygame.init()
		self.screen = pygame.display.set_mode(self.res)
		self.tps_clock = pygame.time.Clock()
		self.tps_delta = 0.0
		self.cars = []
		self.add_car()

		while True:

			# Handle events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					sys.exit(0)

			# Ticking
			self.tps_delta += self.tps_clock.tick() / 1000.0
			while self.tps_delta > 1 / self.tps:
				self.tick()
				self.tps_delta -= 1 / self.tps

     		# Drawing
			self.screen.fill((0, 0, 0))
			self.draw()
			pygame.display.flip()


	def tick(self):
		list(map(lambda x: x.tick(), self.cars))
		#self.cars[0].tick()
		#for car in self.cars:
		#	car.tick()

	def draw(self):
		list(map(lambda x: x.draw(), self.cars))
		#self.cars[0].draw()
		#for car in self.cars:
		#	car.draw()

	def add_car(self):
		car = Car(self)
		self.cars.append(car)
        






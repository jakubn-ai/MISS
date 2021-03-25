import random
import time
import threading
import pygame
import sys
from car import Car
from road import Road


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
		self.road = Road(self)
		self.spawn_car(self.road.position_s4_line)

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

	def draw(self):
		self.road.draw()
		list(map(lambda x: x.draw(), self.cars))

	def spawn_car(self, position):
		car = Car(self, position)
		self.cars.append(car)
        






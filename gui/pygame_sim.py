import random
import time
import threading
import pygame
import sys
from Car import Car


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
		keys = pygame.key.get_pressed()
    	#if keys[pygame.K_d]:
    #		box[0].x += 1
    #	if keys[pygame.K_s]:
    #		box[0].y += 1
    #	if keys[pygame.K_a]:
    #		box[0].x += -1
    #	if keys[pygame.K_w]:
    #		box[0].y -= 1

	def draw(self):
		pygame.draw.rect(surface=self.screen, color=(0, 150, 255), rect=pygame.Rect(10, 10, 5, 5))
        






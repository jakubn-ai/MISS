import pygame
from pygame.math import Vector2

class Road(object):
    def __init__(self, game):
        self.game = game
        self.road_offset = 16
        self.road_width = 32
        
# DEFINING STREETS
        self.position_s1 = Vector2(self.game.screen.get_size()[0]/2 + self.road_offset, 0)
        self.position_s1_line = Vector2(self.game.screen.get_size()[0]/2 + self.road_offset + 4, 0)

        self.position_s2 = Vector2(self.game.screen.get_size()[0]/2 - self.road_offset, 0)
        self.position_s2_line = Vector2(self.game.screen.get_size()[0]/2 - self.road_offset + 4, 0)

        self.position_s3 = Vector2(0, self.game.screen.get_size()[1]/2 + self.road_offset)
        self.position_s3_line = Vector2(0, self.game.screen.get_size()[1]/2 + self.road_offset + 4)

        self.position_s4 = Vector2(0, self.game.screen.get_size()[1]/2 - self.road_offset)
        self.position_s4_line = Vector2(0, self.game.screen.get_size()[1]/2 - self.road_offset + 4)





# ROAD DRAWING        
    def draw(self):

    	
    	street1 = pygame.Rect(self.position_s1.x, self.position_s1.y, self.road_width, self.game.screen.get_size()[0])
    	street2 = pygame.Rect(self.position_s2.x, self.position_s2.y, self.road_width, self.game.screen.get_size()[0])
    	street3 = pygame.Rect(self.position_s3.x, self.position_s3.y, self.game.screen.get_size()[0], self.road_width)
    	street4 = pygame.Rect(self.position_s4.x, self.position_s4.y, self.game.screen.get_size()[0], self.road_width)


    	pygame.draw.rect(self.game.screen, (0, 150, 255), street1)
    	pygame.draw.rect(self.game.screen, (0, 150, 255), street2)
    	pygame.draw.rect(self.game.screen, (0, 150, 255), street3)
    	pygame.draw.rect(self.game.screen, (0, 150, 255), street4)


import pygame
from ui import TrafficLightUI
from ui import SettingsUI as S
import numpy as np


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, vehicleClass, direction_number, direction, idx, will_turn):
        pygame.sprite.Sprite.__init__(self)
        self.idx = idx
        self.vehicleClass = vehicleClass
        self.speed = S.speeds[vehicleClass]
        self.direction_number = direction_number
        self.direction = direction
        self.x = S.x[direction]
        self.y = S.y[direction]
        self.crossed = 0
        self.will_turn = will_turn
        self.turned = 0
        self.rotate_angle = 0
        S.vehicles[direction][0].append(self)
        self.index = len(S.vehicles[direction][0]) - 1
        self.crossed_index = 0
        path = "images/" + direction + "/" + vehicleClass + ".png"
        self.gap = np.random.randint(10, 25)
        self.orginal_image = pygame.image.load(path)
        self.image = pygame.image.load(path)
        self.to_delete = False

        if (len(S.vehicles[direction][0]) > 1 and S.vehicles[direction][0][
            self.index - 1].crossed == 0):  # if more than 1 vehicle in the lane of vehicle before it has crossed stop line
            if (direction == 'right'):
                self.stop = S.vehicles[direction][0][self.index - 1].stop - S.vehicles[direction][0][
                    self.index - 1].image.get_rect().width - self.gap  # setting stop coordinate as: stop coordinate of next vehicle - width of next vehicle - gap
            elif (direction == 'left'):
                self.stop = S.vehicles[direction][0][self.index - 1].stop + S.vehicles[direction][0][
                    self.index - 1].image.get_rect().width + self.gap
            elif (direction == 'down'):
                self.stop = S.vehicles[direction][0][self.index - 1].stop - S.vehicles[direction][0][
                    self.index - 1].image.get_rect().height - self.gap
            elif (direction == 'up'):
                self.stop = S.vehicles[direction][0][self.index - 1].stop + S.vehicles[direction][0][
                    self.index - 1].image.get_rect().height + self.gap
        else:
            self.stop = S.defaultStop[direction]

        # Set new starting and stopping coordinate
        if (direction == 'right'):
            temp = self.image.get_rect().width + self.gap
            S.x[direction] -= temp
        elif (direction == 'left'):
            temp = self.image.get_rect().width + self.gap
            S.x[direction] += temp
        elif (direction == 'down'):
            temp = self.image.get_rect().height + self.gap
            S.y[direction] -= temp
        elif (direction == 'up'):
            temp = self.image.get_rect().height + self.gap
            S.y[direction] += temp
        S.simulation.add(self)

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_to_delete(self, ):
        if self.direction == 'right':
            return self.x > S.screenWidth
        elif self.direction == 'down':
            return self.y > S.screenHeight
        elif self.direction == 'left':
            return self.x < 0
        else:
            return self.y < 0

    def toDelete(self):
        if self.direction == 'right':
            return self.x > S.screenWidth
        elif self.direction == 'down':
            return self.y > S.screenHeight
        elif self.direction == 'left':
            return self.x < 0
        elif self.direction == 'up':
            return self.y < 0

    def set_to_delete(self):
        self.to_delete = True

    def check_coords(self):
        if self.toDelete():
            self.set_to_delete()

    def move(self, tm):
        if self.direction == 'right':
            self.check_coords()
            if self.crossed == 0 and self.x + self.image.get_rect().width > S.stopLines[self.direction]:
                self.crossed = 1
                S.vehicles[self.direction]['crossed'] += 1
                if self.will_turn == 0:
                    S.vehiclesNotTurned[self.direction].append(self)
                    self.crossed_index = len(S.vehiclesNotTurned[self.direction]) - 1
            if self.will_turn == 1:
                if self.crossed == 0 or self.x + self.image.get_rect().width < S.stopLines[self.direction] + 40:
                    if ((self.x + self.image.get_rect().width <= self.stop or self.crossed == 1 or (
                            tm.currentGreen == 0 and tm.currentYellow == 0)) and (
                            self.index == 0 or self.x + self.image.get_rect().width < (
                            S.vehicles[self.direction][0][self.index - 1].x - self.gap) or
                            S.vehicles[self.direction][0][self.index - 1].turned == 1)):
                        self.x += self.speed
                else:
                    if self.turned == 0:
                        self.rotate_angle += S.rotationAngle
                        self.image = pygame.transform.rotate(self.orginal_image, self.rotate_angle)
                        self.x += 2.4
                        self.y -= 2.8
                        if self.rotate_angle == 90:
                            self.turned = 1
                            S.vehiclesTurned[self.direction].append(self)
                            self.crossed_index = len(S.vehiclesTurned[self.direction]) - 1
                    else:
                        if (self.crossed_index == 0 or (self.y > (
                                S.vehiclesTurned[self.direction][self.crossed_index - 1].y +
                                S.vehiclesTurned[self.direction][
                                    self.crossed_index - 1].image.get_rect().height + self.gap))):
                            self.y -= self.speed
            else:
                if self.crossed == 0:
                    if ((self.x + self.image.get_rect().width <= self.stop or (
                            tm.currentGreen == 0 and tm.currentYellow == 0)) and (
                            self.index == 0 or self.x + self.image.get_rect().width < (
                            S.vehicles[self.direction][0][self.index - 1].x - self.gap))):
                        self.x += self.speed
                else:
                    if ((self.crossed_index == 0) or (self.x + self.image.get_rect().width < (
                            S.vehiclesNotTurned[self.direction][self.crossed_index - 1].x - self.gap))):
                        self.x += self.speed

        elif self.direction == 'down':
            self.check_coords()
            if self.crossed == 0 and self.y + self.image.get_rect().height > S.stopLines[self.direction]:
                self.crossed = 1
                S.vehicles[self.direction]['crossed'] += 1
                if self.will_turn == 0:
                    S.vehiclesNotTurned[self.direction].append(self)
                    self.crossed_index = len(S.vehiclesNotTurned[self.direction]) - 1
            if self.will_turn == 1:
                if self.crossed == 0 or self.x + self.image.get_rect().height < S.stopLines[self.direction] + 50:
                    if ((self.y + self.image.get_rect().height <= self.stop or self.crossed == 1 or (
                            tm.currentGreen == 1 and tm.currentYellow == 0)) and (
                            self.index == 0 or self.y + self.image.get_rect().height < (
                            S.vehicles[self.direction][0][self.index - 1].y - self.gap) or
                            S.vehicles[self.direction][0][self.index - 1].turned == 1)):
                        self.y += self.speed
                else:
                    if self.turned == 0:
                        self.rotate_angle += S.rotationAngle
                        self.image = pygame.transform.rotate(self.orginal_image, self.rotate_angle)
                        self.x += 1.2
                        self.y += 1.8
                        if self.rotate_angle == 90:
                            self.turned = 1
                            S.vehiclesTurned[self.direction].append(self)
                            self.crossed_index = len(S.vehiclesTurned[self.direction]) - 1
                    else:
                        if (self.crossed_index == 0 or ((self.x + self.image.get_rect().width) < (
                                S.vehiclesTurned[self.direction][self.crossed_index - 1].x - self.gap))):
                            self.x += self.speed
            else:
                if self.crossed == 0:
                    if ((self.y + self.image.get_rect().height <= self.stop or (
                            tm.currentGreen == 1 and tm.currentYellow == 0)) and (
                            self.index == 0 or self.y + self.image.get_rect().height < (
                            S.vehicles[self.direction][0][self.index - 1].y - self.gap))):
                        self.y += self.speed
                else:
                    if ((self.crossed_index == 0) or (self.y + self.image.get_rect().height < (
                            S.vehiclesNotTurned[self.direction][self.crossed_index - 1].y - self.gap))):
                        self.y += self.speed

        elif self.direction == 'left':
            self.check_coords()
            if self.crossed == 0 and self.x < S.stopLines[self.direction]:
                self.crossed = 1
                S.vehicles[self.direction]['crossed'] += 1
                if self.will_turn == 0:
                    S.vehiclesNotTurned[self.direction].append(self)
                    self.crossed_index = len(S.vehiclesNotTurned[self.direction]) - 1
            if self.will_turn == 1:
                if self.crossed == 0 or self.x > S.stopLines[self.direction] - 70:
                    if ((self.x >= self.stop or (
                            tm.currentGreen == 2 and tm.currentYellow == 0) or self.crossed == 1) and (
                            self.index == 0 or self.x > (
                            S.vehicles[self.direction][0][self.index - 1].x + S.vehicles[self.direction][0][
                        self.index - 1].image.get_rect().width + self.gap) or S.vehicles[self.direction][0][
                                self.index - 1].turned == 1)):
                        self.x -= self.speed
                else:
                    if (self.turned == 0):
                        self.rotate_angle += S.rotationAngle
                        self.image = pygame.transform.rotate(self.orginal_image, self.rotate_angle)
                        self.x -= 1
                        self.y += 1.2
                        if (self.rotate_angle == 90):
                            self.turned = 1
                            S.vehiclesTurned[self.direction].append(self)
                            self.crossed_index = len(S.vehiclesTurned[self.direction]) - 1
                    else:
                        if (self.crossed_index == 0 or ((self.y + self.image.get_rect().height) < (
                                S.vehiclesTurned[self.direction][self.crossed_index - 1].y - self.gap))):
                            self.y += self.speed
            else:
                if self.crossed == 0:
                    if ((self.x >= self.stop or (tm.currentGreen == 2 and tm.currentYellow == 0)) and (
                            self.index == 0 or self.x > (
                            S.vehicles[self.direction][0][self.index - 1].x + S.vehicles[self.direction][0][
                        self.index - 1].image.get_rect().width + self.gap))):
                        self.x -= self.speed
                else:
                    if ((self.crossed_index == 0) or (self.x > (
                            S.vehiclesNotTurned[self.direction][self.crossed_index - 1].x +
                            S.vehiclesNotTurned[self.direction][
                                self.crossed_index - 1].image.get_rect().width + self.gap))):
                        self.x -= self.speed


        elif self.direction == 'up':
            self.check_coords()
            if self.crossed == 0 and self.y < S.stopLines[self.direction]:
                self.crossed = 1
                S.vehicles[self.direction]['crossed'] += 1
                if self.will_turn == 0:
                    S.vehiclesNotTurned[self.direction].append(self)
                    self.crossed_index = len(S.vehiclesNotTurned[self.direction]) - 1
            if self.will_turn == 1:
                if (self.crossed == 0 or self.y > S.stopLines[self.direction] - 60):
                    if ((self.y >= self.stop or (
                            tm.currentGreen == 3 and tm.currentYellow == 0) or self.crossed == 1) and (
                            self.index == 0 or self.y > (
                            S.vehicles[self.direction][0][self.index - 1].y + S.vehicles[self.direction][0][
                        self.index - 1].image.get_rect().height + self.gap) or S.vehicles[self.direction][0][
                                self.index - 1].turned == 1)):
                        self.y -= self.speed
                else:
                    if (self.turned == 0):
                        self.rotate_angle += S.rotationAngle
                        self.image = pygame.transform.rotate(self.orginal_image, self.rotate_angle)
                        self.x -= 2
                        self.y -= 1.2
                        if (self.rotate_angle == 90):
                            self.turned = 1
                            S.vehiclesTurned[self.direction].append(self)
                            self.crossed_index = len(S.vehiclesTurned[self.direction]) - 1
                    else:
                        if (self.crossed_index == 0 or (self.x > (
                                S.vehiclesTurned[self.direction][self.crossed_index - 1].x +
                                S.vehiclesTurned[self.direction][
                                    self.crossed_index - 1].image.get_rect().width + self.gap))):
                            self.x -= self.speed
            else:
                if self.crossed == 0:
                    if ((self.y >= self.stop or (tm.currentGreen == 3 and tm.currentYellow == 0)) and (
                            self.index == 0 or self.y > (
                            S.vehicles[self.direction][0][self.index - 1].y + S.vehicles[self.direction][0][
                        self.index - 1].image.get_rect().height + self.gap))):
                        self.y -= self.speed
                else:
                    if ((self.crossed_index == 0) or (self.y > (
                            S.vehiclesNotTurned[self.direction][self.crossed_index - 1].y +
                            S.vehiclesNotTurned[self.direction][
                                self.crossed_index - 1].image.get_rect().height + self.gap))):
                        self.y -= self.speed

    def pop_vehicles(self):
        S.vehicles[self.direction][0].pop(self.index)
        S.vehicles[self.direction]['crossed'] -= 1

    def update_indexes(self):
        for v in S.vehicles[self.direction][0]:
            v.index -= 1

        if self.will_turn == 0:
            S.vehiclesNotTurned[self.direction].pop(self.crossed_index)
            for v in S.vehiclesNotTurned[self.direction]:
                v.crossed_index -= 1
        else:

            S.vehiclesTurned[self.direction].pop(self.crossed_index)
            for v in S.vehiclesTurned[self.direction]:
                v.crossed_index -= 1

    def kill(self) -> None:
        self.pop_vehicles()
        self.update_indexes()
        super(Vehicle, self).kill()

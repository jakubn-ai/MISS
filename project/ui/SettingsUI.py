# Default values of signal timers
import pygame

signals = []

speeds = {'car': 2.25, 'bus': 1.8, 'truck': 1.8, 'bike': 5}  # average speeds of vehicles

# Coordinates of vehicles' start
x = {'right': 0, 'down': 727, 'left': 1400, 'up': 627}
y = {'right': 370, 'down': 0, 'left': 466, 'up': 800}

vehicles = {'right': {0: [], 'crossed': 0}, 'down': {0: [], 'crossed': 0},
            'left': {0: [], 'crossed': 0}, 'up': {0: [], 'crossed': 0}}

allowedVehicleTypes = {'car': True, 'bus': True, 'truck': True, 'bike': True}
allowedVehicleTypesList = []
vehiclesTurned = {'right': [], 'down':[], 'left': [],'up': []}
vehiclesNotTurned = {'right': [], 'down':[], 'left': [],'up': []}
rotationAngle = 3
mid = {'right': {'x':705, 'y':445}, 'down': {'x':695, 'y':450}, 'left': {'x':695, 'y':425}, 'up': {'x':695, 'y':400}}

vehicleTypes = {0: 'car', 1: 'bus', 2: 'truck', 3: 'bike'}
directionNumbers = {0: 'right', 1: 'down', 2: 'left', 3: 'up'}

# Coordinates of signal image, timer, and vehicle count

stopLines = {'right': 590, 'down': 330, 'left': 800, 'up': 535}
defaultStop = {'right': 580, 'down': 320, 'left': 810, 'up': 545}

screenWidth = 1400
screenHeight = 800
screenSize = (screenWidth, screenHeight)

pygame.init()
simulation = pygame.sprite.Group()
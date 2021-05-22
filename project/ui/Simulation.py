import random
import time
import threading
import pygame
import sys
from ui.VehicleUI import Vehicle
from ui.TrafficLightUI import TrafficSignal, TraficLightsManager
from ui import SettingsUI as S

TM = TraficLightsManager()


# Initialization of signals with default values

def initialize():
    TM.initialize_signals()
    repeat()


def repeat():
    while S.signals[TM.currentGreen].green > 0:  # while the timer of current green signal is not zero
        updateValues()
        time.sleep(1)
    TM.currentYellow = 1
    for vehicle in S.vehicles[S.directionNumbers[TM.currentGreen]][0]:
        vehicle.stop = S.defaultStop[S.directionNumbers[TM.currentGreen]]
    while (S.signals[TM.currentGreen].yellow > 0):  # while the timer of current yellow signal is not zero
        updateValues()
        time.sleep(1)
    TM.currentYellow = 0  # set yellow signal off

    # reset all signal times of current signal to default times
    S.signals[TM.currentGreen].green = TM.defaultGreen
    S.signals[TM.currentGreen].yellow = TM.defaultYellow
    S.signals[TM.currentGreen].red = TM.defaultRed

    TM.currentGreen = TM.nextGreen  # set next signal as green signal
    TM.nextGreen = (TM.currentGreen + 1) % 4  # set next green signal
    S.signals[TM.nextGreen].red = S.signals[TM.currentGreen].yellow + S.signals[
        TM.currentGreen].green  # set the red time of next to next signal as (yellow time + green time) of next signal
    repeat()


# Update values of the signal timers after every second
def updateValues():
    for i in range(0, 4):
        if (i == TM.currentGreen):
            if (TM.currentYellow == 0):
                S.signals[i].green -= 1
            else:
                S.signals[i].yellow -= 1
        else:
            S.signals[i].red -= 1


# Generating vehicles in the simulation
def generateVehicles():
    car_value = 0
    while len(S.vehicles['right'][0]) + len(S.vehicles['down'][0]) + len(S.vehicles['left'][0]) + len(S.vehicles['up'][0]) < 100:
        vehicle_type = 3
        will_turn = 0
        temp = random.randint(0,99)
        if temp < 40:
            will_turn = 1
        temp2 = random.randint(0, 99)
        direction_number = random.randint(0, 3)
        dist = [25, 50, 75, 100]
        if (temp2 < dist[0]):
            direction_number = 0
        elif (temp2 < dist[1]):
            direction_number = 1
        elif (temp2 < dist[2]):
            direction_number = 2
        elif (temp2 < dist[3]):
            direction_number = 3
        car_value += 1
        Vehicle(S.vehicleTypes[vehicle_type], 0, S.directionNumbers[direction_number],
                    car_value, will_turn)
        time.sleep(1)


class Main:
    thread1 = threading.Thread(name="initialization", target=initialize, args=())  # initialization
    thread1.daemon = True
    thread1.start()

    # Colours 
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Setting background image i.e. image of intersection
    background = pygame.image.load('images/intersection.png')

    screen = pygame.display.set_mode(S.screenSize)
    pygame.display.set_caption("SIMULATION")

    # Loading signal images and font
    redSignal = pygame.image.load('images/signals/red.png')
    yellowSignal = pygame.image.load('images/signals/yellow.png')
    greenSignal = pygame.image.load('images/signals/green.png')
    font = pygame.font.Font(None, 30)

    thread2 = threading.Thread(name="generateVehicles", target=generateVehicles, args=())  # Generating vehicles
    thread2.daemon = True
    thread2.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background, (0, 0))  # display background in simulation
        for i in range(0, 4):  # display signal and set timer according to current status: green, yello, or red
            if (i == TM.currentGreen):
                if (TM.currentYellow == 1):
                    S.signals[i].signalText = S.signals[i].yellow
                    screen.blit(yellowSignal, TM.signalCoods[i])
                else:
                    S.signals[i].signalText = S.signals[i].green
                    screen.blit(greenSignal, TM.signalCoods[i])
            else:
                if (S.signals[i].red <= 10):
                    S.signals[i].signalText = S.signals[i].red
                else:
                    S.signals[i].signalText = "---"
                screen.blit(redSignal, TM.signalCoods[i])
        signalTexts = ["", "", "", ""]

        # display signal timer
        for i in range(0, 4):
            signalTexts[i] = font.render(str(S.signals[i].signalText), True, white, black)
            screen.blit(signalTexts[i], TM.signalTimerCoods[i])
        # display the vehicles
        for vehicle in S.simulation:
            screen.blit(vehicle.image, [vehicle.x, vehicle.y])
            if vehicle.to_delete:
                vehicle.kill()
            vehicle.move(TM)
        pygame.display.update()


Main()

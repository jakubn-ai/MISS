import random
from statistics import mean
import matplotlib.pyplot as plt
import numpy

import simpy
import time

from model.Graph import Graph
from model.TrafficLightManager import TrafficLightManager
from model.Vehicle import Vehicle


def simulate(cars_no):
    # env = simpy.rt.RealtimeEnvironment()
    env = simpy.Environment()
    light_groups = [
        [13, 15],
        [17, 19],
        [12, 14],
        [16, 18]
    ]

    lightManager = TrafficLightManager(env, light_groups, 20)
    graph = Graph(lightManager)

    vehicles = []

    for c in range(cars_no):
        vehicle = Vehicle(env, c, random.choice(graph.start_nodes), random.choice(graph.end_nodes), graph,
                          max(numpy.random.normal(loc=20.0, scale=2.0), 20.0))
        vehicles.append(vehicle)

    env.run(until=60*60*2)

    return vehicles


def calculate_mean_times(cars):
    return {
        'travelTimeMean': mean([vehicle.data.get('travelTime') for vehicle in cars]),
        'waitOnRedTimeMean': mean([vehicle.data.get('waitOnRedLightTime') for vehicle in cars]),
        'distanceTraveledMean': mean([vehicle.data.get('distanceTraveled') for vehicle in cars]),
        'waitTimeMean': mean([vehicle.data.get('waitTime') for vehicle in cars]),
        'driveTimeMean': mean([vehicle.data.get('driveTime') for vehicle in cars])
    }


if __name__ == '__main__':
    vehiclesNo = []
    travelTimeMeans = []
    waitOnRedTimeMeans = []
    distanceTraveledMeans = []
    waitTimeMeans = []
    driveTimeMeans = []

    for vehicles_no in range(1, 100):
        print(vehicles_no)
        vehicles = simulate(vehicles_no)
        result = calculate_mean_times(vehicles)

        vehiclesNo.append(vehicles_no)
        travelTimeMeans.append(result['travelTimeMean'])
        waitOnRedTimeMeans.append(result['waitOnRedTimeMean'])
        distanceTraveledMeans.append(result['distanceTraveledMean'])
        waitTimeMeans.append(result['waitTimeMean'])
        driveTimeMeans.append(result['driveTimeMean'])

    plt.plot(vehiclesNo, driveTimeMeans, linestyle='dashed', marker='o')
    plt.xlabel('Number of cars')
    plt.ylabel('Average drive time [s]')
    plt.title('Average drive time vs number of cars')
    plt.savefig('drive.png')
    plt.show()

    plt.plot(vehiclesNo, waitTimeMeans, linestyle='dashed', marker='o')
    plt.xlabel('Number of cars')
    plt.ylabel('Average wait time [s]')
    plt.title('Average wait time vs number of cars')
    plt.savefig('wait.png')
    plt.show()

    plt.plot(vehiclesNo, distanceTraveledMeans, linestyle='dashed', marker='o')
    plt.xlabel('Number of cars')
    plt.ylabel('Average distance traveled [m]')
    plt.title('Average distance traveled vs number of cars')
    plt.savefig('distance.png')
    plt.show()

    plt.plot(vehiclesNo, travelTimeMeans, linestyle='dashed', marker='o')
    plt.xlabel('Number of cars')
    plt.ylabel('Average travel time [s]')
    plt.title('Average travel time vs number of cars')
    plt.savefig('travel.png')
    plt.show()

    plt.plot(vehiclesNo, waitOnRedTimeMeans, linestyle='dashed', marker='o')
    plt.xlabel('Number of cars')
    plt.ylabel('Average wait on red time [s]')
    plt.title('Average wait on red time vs number of cars')
    plt.savefig('wait_on_red.png')
    plt.show()

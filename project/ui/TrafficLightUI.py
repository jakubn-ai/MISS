from ui import SettingsUI as S

class TrafficSignal:
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        self.signalText = ""

class TraficLightsManager():
    def __init__(self):
        self.defaultGreen = 10
        self.defaultRed = 150
        self.defaultYellow = 5

        self.currentGreen = 0  # Indicates which signal is green currently
        self.nextGreen = (self.currentGreen + 1) % 4 # Indicates which signal will turn green next
        self.currentYellow = 0  # Indicates whether yellow signal is on or off
        self.signalCoods = [(530, 230), (810, 230), (810, 570), (530, 570)]
        self.signalTimerCoods = [(530, 210), (810, 210), (810, 550), (530, 550)]

    def initialize_signals(self):
        ts1 = TrafficSignal(0, self.defaultYellow, self.defaultGreen)
        S.signals.append(ts1)
        ts2 = TrafficSignal(ts1.red + ts1.yellow + ts1.green, self.defaultYellow, self.defaultGreen)
        S.signals.append(ts2)
        ts3 = TrafficSignal(self.defaultRed, self.defaultYellow, self.defaultGreen)
        S.signals.append(ts3)
        ts4 = TrafficSignal(self.defaultRed, self.defaultYellow, self.defaultGreen)
        S.signals.append(ts4)
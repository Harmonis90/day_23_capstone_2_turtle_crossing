from turtle import Turtle, Screen
import random
from car import Car

SPEED_INCREASE_FACTOR = 1.2
SPAWN_CAR_COUNT = 6

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.cars = []
        self.speed_multiplier = 0

    def spawn_car(self):
        new_car = Car()
        self.cars.append(new_car)

    def move_cars(self):

        for car in self.cars:
            speed = car.move_speed + self.speed_multiplier
            car.move(speed)

    def increase_car_speed(self):
        self.speed_multiplier += 5






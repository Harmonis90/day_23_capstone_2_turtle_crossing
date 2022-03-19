from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

SCREEN_TOP = int(600 / 2)
SCREEN_BOTTOM = int(-600 / 2)
SPRITE_SIZE = 20

SPAWN_XPOS = int(600 / 2) + (SPRITE_SIZE * 3)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.cars = []

    def spawn_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.goto(self.get_random_spawn_pos())
        self.cars.append(new_car)

    def get_random_spawn_pos(self):
        rand_ypos = random.randint(SCREEN_BOTTOM + SPRITE_SIZE, SCREEN_TOP - int(SPRITE_SIZE / 2))
        return (SPAWN_XPOS, rand_ypos)

    def move(self):
        new_xpos = self.xcor() - MOVE_INCREMENT
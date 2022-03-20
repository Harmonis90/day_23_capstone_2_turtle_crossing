from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
START_SPEED = 5
speed_delta = 0
SCREEN_TOP = int(600 / 2)
SCREEN_BOTTOM = int(-600 / 2)
SPRITE_SIZE = 20

SPAWN_XPOS = int(600 / 2) + (SPRITE_SIZE * 3)


def get_random_spawn_pos():
    rand_ypos = random.randint(SCREEN_BOTTOM + (SPRITE_SIZE * 3), SCREEN_TOP - int(SPRITE_SIZE * 2))
    return SPAWN_XPOS, rand_ypos


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.instantiate_car()
        self.move_speed = START_SPEED

    def instantiate_car(self):
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(get_random_spawn_pos())

    def move(self, speed_factor):
        new_xpos = self.xcor() - (self.move_speed + speed_factor)
        self.goto(new_xpos, self.ycor())





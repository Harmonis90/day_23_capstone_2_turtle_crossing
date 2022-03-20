import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
count_until_new_car = 6
sleep_speed = 0.1
car_width = 40
car_height = 20

turtle_width = 20
turtle_height = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

def on_collision():
    hit_distance = int(car_width / 2) + int(turtle_height / 2)
    for car in car_manager.cars:
        if car.distance(player.pos()) <= hit_distance:
            return True



game_is_on = True
while game_is_on:
    time.sleep(sleep_speed)
    screen.update()
    screen.listen()
    if player.has_reached_finish():
        player.reset_position()
        car_manager.increase_car_speed()
        sleep_speed -= 0.01
        scoreboard.add_to_score()
    if count_until_new_car <= 0:
        car_manager.spawn_car()
        count_until_new_car = 6
    else:
        count_until_new_car -= 1
    car_manager.move_cars()
    if on_collision():
        game_is_on = False

    screen.onkeypress(key="Up", fun=player.move_up)
    screen.onkeypress(key="Down", fun=player.move_down)

scoreboard.game_over()
screen.exitonclick()

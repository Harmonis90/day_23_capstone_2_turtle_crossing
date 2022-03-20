from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("#000000")
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move_up(self):
        new_ypos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_ypos)

    def move_down(self):
        if self.ycor() <= STARTING_POSITION[1]:
            pass
        else:
            new_ypos = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_ypos)

    def reset_position(self):
        self.goto(STARTING_POSITION)
        return True

    def has_reached_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset_position()
            return True

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
        if self.ycor() >= FINISH_LINE_Y:
            print("FINISH")
        else:
            new_ypos = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_ypos)

    def move_down(self):
        if self.ycor() <= STARTING_POSITION[1]:
            pass
        else:
            new_ypos = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_ypos)
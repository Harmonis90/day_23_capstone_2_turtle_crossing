from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Comic Sans", 34, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update_score()

    def add_to_score(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.reset()
        self.ht()
        self.penup()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.reset()
        self.ht()
        self.penup()

        self.write(f"GAME OVER! "
                   f"Score: {self.level}", align="center", font=GAME_OVER_FONT)
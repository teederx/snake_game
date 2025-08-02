from turtle import Turtle


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 12, "normal"))
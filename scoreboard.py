from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.score_board()

    def score_board(self):
        self.goto(-150, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.rewrite()

    def add(self):
        self.score += 1
        self.rewrite()

    def rewrite(self):
        self.clear()
        self.write(f"Score = {self.score}", False, "center", 12)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", False, "center", 12)
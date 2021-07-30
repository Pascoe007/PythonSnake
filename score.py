from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.write("Score: {}".format(self.score), move=False, align="center", font=("Arial", 30, "normal"))
    def IncreaseScore(self):
        self.clear()
        self.score+=1
        self.write("Score: {}".format(self.score), move=False, align="center", font=("Arial", 30, "normal"))
        
        
        
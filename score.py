from turtle import Turtle, update

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.UpdateScore()

    def IncreaseScore(self):
        self.score+=1
        self.UpdateScore()
        
    
    def UpdateScore(self):
        self.clear()
        self.write("Score: {} Highscore: {}".format(self.score, self.highScore), move=False, align="center", font=("Arial", 15, "normal"))

    def Reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highScore}")

        self.UpdateScore()
        self.score = 0

    # def GameOver(self):
    #     self.goto(0,0)
    #     self.write("Game Over.", move=False, align="center", font=("Arial", 30, "normal"))
        
        
        
        
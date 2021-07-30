from turtle import turtles
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        foodX = random.randrange(-280,280,20)
        foodY = random.randrange(-280,280,20)
        self.goto(foodX, foodY)
    def RandomLocation(self):
        self.foodX = random.randrange(-280,280,20)
        self.foodY = random.randrange(-280,280,20)
        self.goto(self.foodX, self.foodY)
        

        
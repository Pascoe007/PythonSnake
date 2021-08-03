from turtle import Turtle
import time
STARTINGPOS = [(0,0),(-20,0),(-40,0)]
MOVEDIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.snakeBody=[]
        self.CreateSnake()
        self.head = self.snakeBody[0]
        self.back = self.snakeBody[-1]
    def CreateSnake(self):
        for pos in STARTINGPOS:
            s = Turtle("square")
            s.penup()
            s.color("white")
            s.goto(pos)
            self.snakeBody.append(s)
    def IncreaseLenght(self):
        s = Turtle("square")
        s.penup()
        s.color("white")
        s.goto(self.back.pos())
        self.snakeBody.append(s)
    
    def Reset(self):
        for s in self.snakeBody:
            s.goto(1000,1000)
        self.snakeBody.clear()
        self.CreateSnake()
        self.head = self.snakeBody[0]

    def Move(self):
        for s in range(len(self.snakeBody)-1, 0, -1):
            self.snakeBody[s].goto(self.snakeBody[s-1].pos())
        self.head.fd(MOVEDIS)
    def Up(self):
        if self.head.heading() == DOWN:    
            pass
        else:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() == UP:    
            pass
        else:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading() == RIGHT:    
            pass
        else:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading() == LEFT:    
            pass
        else:
            self.head.setheading(RIGHT)
    
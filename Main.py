from turtle import Screen, Turtle, distance
import time
from snake import Snake
from food import Food
from score import Scoreboard
screen = Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()



screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")


gameRunning = True
while gameRunning:
    screen.update()
    time.sleep(0.1)
    snake.Move()
    if snake.head.distance(food) < 10:
        food.RandomLocation()
        snake.IncreaseLenght()
        score.IncreaseScore()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameRunning = False
        score.GameOver()
    for s in snake.snakeBody:
        if s == snake.head:
            pass
        elif snake.head.distance(s) < 10:
            gameRunning = False
            score.GameOver()


    

        



screen.exitonclick()
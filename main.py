from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time 


# Setting up screen
screen = Screen()
screen.setup(height=600 , width= 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food= Food()
scoreboard= ScoreBoard()

# Controlling Snake moment
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

game_is_on = True



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect colliosn

    if snake.head.distance(food)< 15 :
        food.refresh()
        scoreboard.score_increment()
        snake.extend()
    
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor() > 280 :
        game_is_on = False
        scoreboard.game_over()

    #detect self collision 
    for something in snake.segmemts:
        if something == snake.head:
            pass
        elif snake.head.distance(something) < 10 :
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

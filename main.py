import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

#--Screen setup--
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Snake Game')
#Stop animation
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key='Right', fun=snake.move_right)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)

game_is_on = True

while game_is_on:
    #Putting the update here makes it show the animation each
    # time all the segments of the snake has been moved
    screen.update()
    #Sleep for 0.5 seconds after each segment has been moved forward
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments:
        if  snake.head.distance(segment[1:]) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()
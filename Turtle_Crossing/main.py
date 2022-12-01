import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
loop = 0
while game_is_on:
    loop += 1
    time.sleep(0.1)
    screen.update()
    level = scoreboard.score

    car_manager.create_cars()
    car_manager.move(level=level)

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            player.reset()
            scoreboard.game_over()

    if player.ycor() == 280:
        player.reset()
        scoreboard.increase_score()

screen.exitonclick()
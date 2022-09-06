import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("The Cross Turtle")
player = Player()
car = CarManager()
screen.onkey(player.move_forward, "Up")
sb = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()


    for x in car.all_cars:
        if x.distance(player) < 20:
            game_is_on = False
            sb.game_over()

    if player.finish() == True:
        car.level_up()
        sb.score_tracking()



screen.exitonclick()
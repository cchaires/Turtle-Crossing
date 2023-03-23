import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

cars = CarManager()
carlitos = Player()
score_board = Scoreboard()

screen.onkey(carlitos.up, "Up")
screen.onkey(carlitos.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    # Detect collisions with cars
    for c in cars.car_list:
        if carlitos.distance(c) < 18:
            score_board.game_over()
            game_is_on = False

    # Increase score when the turtle cross the finish line
    if carlitos.is_in_finish_line():
        score_board.increase_score()
        cars.next_level()
        carlitos.go_to_start()








screen.exitonclick()

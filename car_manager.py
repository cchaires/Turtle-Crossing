from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            r_y = random.randint(- 250, 250)
            r_x = random.randint(280, 300)
            position = (r_x, r_y)
            color = random.choice(COLORS)
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(0.5, 1)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(color)
            new_car.goto(position)
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT





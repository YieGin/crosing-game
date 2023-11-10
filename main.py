from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.screensize(600, 600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    
    scoreboard.game_lvls()
    car_manager.create_car()
    car_manager.move_cars()
    
    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False
        
    #Detect successful crossing
    if player.ycor() > 350:
        player.next_lvl()
        scoreboard.next_lvl()


screen.exitonclick()

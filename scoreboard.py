from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Scoreboard (Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.color("black")
        self.score = 0
        self.hideturtle()
        
    def game_lvls (self):
        self.goto(-350, 360)
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)
        
    def next_lvl (self):
        self.score += 1
        self.clear()
        self.game_lvls()
    
    def game_over (self):
        self.goto(0, 0)
        self.write(f"Game Over ", align=ALIGN, font=FONT)

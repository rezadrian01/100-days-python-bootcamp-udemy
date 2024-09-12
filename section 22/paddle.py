from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__('square')
        self.color('white')
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
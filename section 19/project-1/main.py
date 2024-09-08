import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.forward(-10)

def turn_left():
    tim.setheading(tim.heading() + 10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_backwards, 's')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()
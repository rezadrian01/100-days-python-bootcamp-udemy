import turtle
import pandas

BASE_PATH = "section 25/us-states-game"
FONT = ('Courier', 10, 'normal')

screen = turtle.Screen()
image = f"{BASE_PATH}/blank_states_img.gif"
screen.addshape(image)
screen.title("U.S. State Game")
turtle.shape(image)

data = pandas.read_csv(f"{BASE_PATH}/50_states.csv")
all_state = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_state)}/50", prompt="Whats another state name").title()

    if answer_state == 'Exit':
        missing_state = [state for state in all_state if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv(f"{BASE_PATH}/states_to_learn.csv")
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(state_data.x.item(), state_data.y.item())
        new_turtle.write(state_data.state.item())




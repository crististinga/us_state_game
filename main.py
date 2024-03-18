import turtle
import pandas
import time

game_on = True
correct_answ = []
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()



while len(correct_answ) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answ)} / {len(states_list)} States Correct", prompt="What's another state's name")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        states_to_learn = [state for state in states_list if state not in correct_answ]
        print(states_to_learn)
        lear_file = pandas.DataFrame(states_to_learn)
        lear_file.to_csv("states_to_learn.csv")
        break

    for state in states_list:
        if answer_state == state:
            correct_answ.append(state)
            answer_on_screen = turtle.Turtle()
            answer_on_screen.hideturtle()
            answer_on_screen.penup()
            answer_on_screen.goto((int(data[data.state == state]["x"]), int(data[data.state == state]["y"])))
            answer_on_screen.write(state)


    print(answer_state)



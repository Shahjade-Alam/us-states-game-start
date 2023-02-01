import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
score = 0
Chance = 5
data = pandas.read_csv("50_states.csv")
states = (data['state'].to_list())
correct_answers = []
missed_answer = []

while Chance != 0:
    answer_state = screen.textinput(title=f"{(Chance)}/5", prompt="What's another state name").title()
    print(f"answer_state:{answer_state}")
    Chance -= 1
    print(f"Chance left:{Chance}")
    if answer_state == "Exit":
        break
    if answer_state in states:
        correct_answers.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        print(f"win:{answer_state}")
        x_cor = int(data[data['state'] == answer_state]['x'])
        y_cor = int(data[data['state'] == answer_state]['y'])
        t.goto(x_cor, y_cor)
        t.write(f"{answer_state}")
        score += 1
# print(correct_answers)
# print(missed_answer)
for state in states:
    if state not in correct_answers:
        missed_answer.append(state)
new_data = pandas.DataFrame(missed_answer)
new_data.to_csv("State_to_learn.csv")

# screen.exitonclick()

# self.goto(-250, 250)
# self.clear()
# self.write(f"LEVEL:{score}", align="left", font=FONT)

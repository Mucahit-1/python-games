from turtle import Turtle , Screen
import random

screen = Screen()
user_bet = screen.textinput(title="make your bet" , prompt="which turtle will win the race? enter a color :")
screen.setup(width=500 , height=400)
all_turtles = []
is_race_on = False
colors = ["red" , "orange" , "yellow" , "green" , "blue" , "purple" , "black"]

new_pos = 0

def turtle_pos():
    global new_pos
    racer.goto(x=-230, y=-80 + new_pos)
    new_pos += 40

for x in range(6):
    racer = Turtle(shape="turtle")
    racer.color(colors[x])
    racer.penup()
    turtle_pos()
    all_turtles.append(racer)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won! the {winning_color} turtle is the winner")
            else:
                print(f"you have lost! the {winning_color} turtle is the winner")

            is_race_on = False

        random_dis = random.randint(0 , 10)
        turtle.forward(random_dis)

screen.exitonclick()

from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(700, 600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle to win the race? Enter the color")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-250, -150, -50, 50, 150, 250]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # or we can make a new command for the shape like: tim.shape("turtle")
    new_turtle.pensize(4)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-330, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 330:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()

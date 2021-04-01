from turtle import Turtle, Screen
import random

race_on=False
screen=Screen()
screen.setup(width=500,height=400)
no_of_tur=screen.textinput(title="Turtle Race",prompt="Enter no. of turtles between 1 to 5")
all_turtle=[]

user_turtle=screen.textinput(title="Turtle Race",prompt="Select your turtle for race ")
colours=["red","blue","violet","indigo","orange","yellow"]
y_position=[-70,-30,10,50,90]
for index in range(0,int(no_of_tur)):
    t =Turtle(shape="turtle")
    t.color(colours[index])
    t.penup()
    t.goto(x=-230,y=y_position[index])
    all_turtle.append(t)

if user_turtle:
    race_on=True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_turtle:
                print(f"You won! Winner is {winning_color} turtle")
            else:
                print(f"You lost! Winner is {winning_color} turtle")
        d=random.randint(0,10)
        turtle.forward(d)


screen.exitonclick()
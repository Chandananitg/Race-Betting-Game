from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=900, height=600)
screen.colormode(255)
screen.title("Turtle Race Betting")
lines = Turtle()
lines.width(3)
lines.hideturtle()
lines.pencolor("sienna4")
lines.speed("fastest")
print_result = Turtle()
print_result.hideturtle()
print_result.penup()
print_result.goto(0, 250)


def draw_tracks():
    lines.width(2)
    lines.color("darkgreen")
    lines.penup()
    i = -227.5
    for _ in range(8):
        lines.goto(-360, i)
        lines.setheading(0)
        lines.pendown()
        lines.forward(720)
        lines.penup()
        i += 65


def draw_lines():
    lines.width(2)
    lines.penup()
    lines.goto(-360, -237.5)
    lines.setheading(90)
    lines.pendown()
    for _ in range(2):
        lines.forward(475)
        lines.right(90)
        lines.forward(720)
        lines.right(90)
    lines.end_fill()
    lines.penup()
    lines.goto(350, -237.5)
    lines.pendown()
    lines.width(3)
    lines.setheading(90)
    lines.forward(475)


user_bet = screen.textinput(title="Make your bet !",
                            prompt="Which colour turtle do you think will win? (VIBGYOR colours) Press enter to start the race").lower()
is_race_on = True
color_list = [(51, 0, 110), (37, 40, 128), (30, 122, 255), (0, 255, 0), (255, 255, 0), (255, 127, 0), (255, 0, 0)]
color_names = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtle_list = []
lines.color("yellowgreen")
lines.begin_fill()
draw_lines()
lines.end_fill()
lines.color("darkgreen")
draw_lines()
draw_tracks()
for colour in color_list:
    tim = Turtle("turtle")
    tim.penup()
    tim.speed("fastest")
    tim.color("black", colour)
    tim.shapesize(2)
    turtle_list.append(tim)
i = 195
for tim in turtle_list:
    tim.goto(-400, i)
    i -= 65

finish_xcor = 320
winner = Turtle()
winner.hideturtle()
while is_race_on:
    i = 0
    while i < 7:
        step = random.randint(1, 15)
        turtle_list[i].forward(step)
        if turtle_list[i].xcor() >= finish_xcor:
            is_race_on = False
            winner = turtle_list[i]
            i = 7
        i += 1

index = turtle_list.index(winner)
wincolour = color_names[index]
if user_bet == wincolour:
    print_result.write(f"{user_bet.upper()} won the race. You've won the bet!", align="center",
                       font=("Comic Sans", 15, "normal"))
else:
    print_result.write(f"{wincolour.upper()} won the race. You've lost the bet!", align="center",
                       font=("Comic Sans", 15, "normal"))
screen.exitonclick()

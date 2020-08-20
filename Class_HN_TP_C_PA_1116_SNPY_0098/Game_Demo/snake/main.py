

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0
move_status = False

# Set up the screen
wn = turtle.Screen()
wn.title("Game killing corona")
wn.setup(width=600, height=600)
# wn.bgpic("bg.gif")
wn.bgcolor("black")
wn.tracer(0)  # Turns off the screen updates

# Tải ảnh
turtle.register_shape("rc.gif")
# turtle.register_shape("seg2.gif")
turtle.register_shape("corona.gif")


# Đầu rắn
head = turtle.Turtle()
head.speed(0)
# head.shape("rc.gif")
head.shape("square")
head.color("white")
head.penup()
head.goto(100, 0)
head.direction = "stop"


# Snake food
number_of_food = 5

foods = []

for i in range(number_of_food):
    foods.append(turtle.Turtle())

for food in foods:
    food.shape("square")
    food.color("red")
    food.speed(0)
    food.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    food.goto(x, y)



segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    #if head.direction != "down":
        head.direction = "up"



def go_down():
    #if head.direction != "up":
        head.direction = "down"



def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"




def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        move_status = True

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        move_status = True

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        move_status = True

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        move_status = True


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        # for segment in segments:
        #     segment.hideturtle()
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("arial", 24, "normal"))

        # Check for a collision with the food
    for food in foods:
        if head.distance(food) < 24:

            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)

            food.goto(x, y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Điểm: {}  Kỉ Lục: {}".format(score, high_score), align="center", font=("arial", 24, "normal"))

            # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    # if  score == 0:
    #      wn.bgpic("bg1.gif")
    # else:
    #      wn.bgpic("bg2.gif")

    # Kiểm tra va cham thân
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("arial", 24, "normal"))


    time.sleep(delay)

wn.mainloop()
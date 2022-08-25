import turtle

# Setting up all the variable for turtle
b = turtle.Screen()
b.title("test")
b.bgcolor("white")
b.setup(width=800, height=600)
b.tracer(0)

a = turtle.Turtle()
a.shape("circle")
a.penup()
a.goto(-250, 0)
a.pendown()

c = turtle.Turtle()
c.shape("square")
c.shapesize(stretch_wid=1, stretch_len=2)
c.color("brown")
c.penup()
c.goto(-370, 280)
c.pendown()

c = turtle.Turtle()
c.shape("square")
c.shapesize(stretch_wid=1, stretch_len=2)
c.color("violet")
c.penup()
c.goto(-315, 280)
c.pendown()

c = turtle.Turtle()
c.shape("square")
c.shapesize(stretch_wid=1, stretch_len=2)
c.color("black")
c.penup()
c.goto(-260, 280)
c.pendown()

d = turtle.Turtle()
d.shape("square")
d.shapesize(stretch_wid=1, stretch_len=2)
d.color("yellow")
d.penup()
d.goto(-205, 280)
d.pendown()

e = turtle.Turtle()
e.shape("square")
e.shapesize(stretch_wid=1, stretch_len=2)
e.color("blue")
e.penup()
e.goto(-150, 280)
e.pendown()

f = turtle.Turtle()
f.shape("square")
f.shapesize(stretch_wid=1, stretch_len=2)
f.color("orange")
f.penup()
f.goto(-95, 280)
f.pendown()

g = turtle.Turtle()
g.shape("square")
g.shapesize(stretch_wid=1, stretch_len=2)
g.color("red")
g.penup()
g.goto(-40, 280)
g.pendown()

h = turtle.Turtle()
h.shape("square")
h.shapesize(stretch_wid=1, stretch_len=1)
h.color("black")
h.penup()
h.goto(0, 270)
h.pendown()
h.hideturtle()
h.write("lift", font=("curior", 14, "normal"))

j = turtle.Turtle()
j.shape("square")
j.shapesize(stretch_wid=1, stretch_len=1)
j.color("black")
j.penup()
j.goto(35, 270)
j.pendown()
j.hideturtle()
j.write("+", font=("curior", 14, "normal"))

k = turtle.Turtle()
k.shape("square")
k.shapesize(stretch_wid=1, stretch_len=1)
k.color("black")
k.penup()
k.goto(60, 270)
k.pendown()
k.hideturtle()
k.write("-", font=("curior", 14, "normal"))

l = turtle.Turtle()
l.shape("square")
l.shapesize(stretch_wid=1, stretch_len=2)
l.hideturtle()
l.penup()
l.goto(80, 260)
l.pendown()
l.write("     up       circle  =>\nle  do  ri   10 20",
        font=("curior", 14, "normal"))  # spaces for visual represntation


# add function to move initial position (10)

def up():
    a.sety(a.ycor() + 10)


def down():
    a.sety(a.ycor() - 10)


def left():
    a.setx(a.xcor() - 10)


def right():
    a.setx(a.xcor() + 10)


def black():
    a.color("black")


def orange():
    a.color("orange")


def blue():
    a.color("blue")


def yellow():
    a.color("yellow")


def red():
    a.color("red")


def white():
    a.color("white")


def change(x, y):
    print(x, y)
    if (-280 < x < -240) and (290 > y > 270):
        black()
    elif (-225 < x < -185) and (290 > y > 270):
        yellow()
    elif (-170 < x < -130) and (290 > y > 270):
        blue()
    elif (-115 < x < -75) and (290 > y > 270):
        orange()
    elif (-60 < x < -20) and (290 > y > 270):
        red()
    elif (0 < x < 20) and (290 > y > 270):
        white()
    elif (35 < x < 45) and (290 > y > 270):
        a.pensize(a.pensize() + 1)
    elif (55 < x < 65) and (290 > y > 270):
        a.pensize(a.pensize() - 1)
    elif (130 < x < 150) and (280 > y > 260):
        a.penup()
        a.goto(a.xcor() + 10, a.ycor())
        a.pendown()
    elif (105 < x < 125) and (300 > y > 280):
        a.penup()
        a.goto(a.xcor(), a.ycor() + 10)
        a.pendown()
    elif (105 < x < 125) and (279 > y > 265):
        a.penup()
        a.goto(a.xcor(), a.ycor() - 10)
        a.pendown()
    elif (75 < x < 95) and (280 > y > 260):
        a.penup()
        a.goto(a.xcor() - 10, a.ycor())
        a.pendown()
    elif (160 < x < 180) and (280 > y > 260):
        a.circle(10)
    elif (190 < x < 210) and (280 > y > 260):
        a.circle(20)
    elif (215 < x < 235) and (300 > y > 280):
        a.undo()
    elif x == a.xcor() and y == a.ycor():
        a.shapesize(stretch_wid=.5, stretch_len=.5)
    elif (-295 > x > -335) and (290 > y > 270):
        a.color("violet")
    elif (-350 > x > -390) and (290 > y > 270):
        a.color("brown")


def increase():
    a.pensize(a.pensize() + 1)


def decrease():
    a.pensize(a.pensize() - 1)


def dragging(x, y):
    a.ondrag(None)
    a.setheading(a.towards(x, y))
    a.goto(x, y)
    a.ondrag(dragging)


a.ondrag(dragging)
b.listen()
b.onkeypress(up, "w")
b.onkeypress(down, "s")
b.onkeypress(left, "a")
b.onkeypress(right, "d")
b.onclick(change)
b.onkeypress(black, "b")
b.onkeypress(orange, "o")
b.onkeypress(blue, "v")
b.onkeypress(yellow, "y")
b.onkeypress(increase, "i")
b.onkeypress(decrease, "l")

while True:
    b.update()

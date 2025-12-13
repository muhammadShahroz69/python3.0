import turtle

t = turtle.Turtle()
s = turtle.Screen()

colors = ['red', 'purple', 'blue', 'green', 'yellow']
s.bgcolor('black')

t.speed('fastest')
t.hideturtle()

for i in range(200):
    t.pencolor(colors[i % len(colors)])
    t.width(2)
    t.forward(i / 2)
    t.left(45)

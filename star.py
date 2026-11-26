import turtle
t = turtle.Turtle(); turtle.bgcolor("black"); t.speed(0)
colors = ["red", "orange", "yellow", "lime", "cyan", "blue", "violet", "magenta"]
for i in range(36):
    t.color(colors[i % len(colors)])
    for j in range(5):
        t.forward(150)
        t.left(144)
    t.left(10)
turtle.done()

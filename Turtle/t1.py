import turtle
t = turtle
t.speed(0)
t.pensize(2)
color_val=0.0
screen = turtle.Screen()
screen.setup(1920,1080)
t.color(0.5,1,color_val)
for x in range(0,360,5):
    color_val=x/360
    t.color=(0.5,0.5,color_val)
    t.setheading(x)
    t.circle(200)
screen.mainloop()

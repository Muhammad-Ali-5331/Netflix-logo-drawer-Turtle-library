from turtle import Turtle,Screen
def Teleport(x,y):
    t.penup();t.goto(x,y);t.pendown()
    
def draw_N_lines(x,y):
    Teleport(x,y)
    t.right(90)
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()
    t.setheading(0)
    
def draw_Middle_Line():
    t.right(68)
    t.begin_fill()
    t.forward(325)
    t.setheading(0)
    t.forward(50)
    t.left(112)
    t.forward(326)
    t.setheading(0);t.setheading(180)
    t.forward(50)
    t.end_fill()
    t.hideturtle()
        
t = Turtle();t.fillcolor("red");t.speed(5);scr = Screen();scr.bgcolor("black")
draw_N_lines(-100,150);draw_N_lines(20,150)
Teleport(-100,150)
draw_Middle_Line()

scr.exitonclick()

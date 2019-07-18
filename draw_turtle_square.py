import turtle

def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("classic")
    brad.color("yellow")
    brad.speed(3)

    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(3)
    angie.circle(100)

    css=turtle.Turtle()
    css.shape("circle")
    css.color("green")
    css.speed(3)
    for i in range(0,3):
        css.forward(100)
        css.right(120)
    
    window.exitonclick()

draw_art()

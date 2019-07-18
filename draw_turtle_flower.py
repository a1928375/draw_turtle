import turtle

def draw_rhombus(name):
    for i in range(0,2):
        name.forward(60)
        name.left(45)
        name.forward(60)
        name.left(135)
    
def draw_flower():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("triangle")
    brad.color("blue")
    brad.speed(0)

    for i in range(120):
        draw_rhombus(brad)
        brad.left(3)
        print i

    brad.right(90)
    brad.forward(300)
    

    window.exitonclick()

draw_flower()



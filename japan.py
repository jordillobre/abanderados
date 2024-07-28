import turtle as Turtle
import time

def draw_japan():

    Turtle.setup(700, 700)
    Turtle.bgcolor("Black")

    ancho_banda = 600
    alto_banda = 400
    color_rojo = "#FF0000"
    color_blanco = "#FFFFFF"
    diametro = 120

    Turtle.hideturtle()
    Turtle.penup()
    Turtle.goto(-ancho_banda / 2, -alto_banda/2)
    Turtle.pendown()
    Turtle.showturtle()

    Turtle.begin_fill()

    Turtle.color(color_blanco)
    Turtle.forward(ancho_banda)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.left(90)
    Turtle.forward(ancho_banda)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.end_fill()

    Turtle.penup()
    Turtle.left(90)
    Turtle.goto(0, -diametro)
    Turtle.pendown()

    Turtle.begin_fill()
    Turtle.color(color_rojo)
    Turtle.circle(diametro)
    Turtle.end_fill()

   
    Turtle.hideturtle()
    time.sleep(10)
    
    # Cerrar la ventana
    Turtle.bye()
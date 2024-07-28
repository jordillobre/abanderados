import turtle as Turtle
import time

def draw_italy():
    Turtle.setup(700, 700)
    Turtle.bgcolor("Black")

    ancho_banda = 600
    alto_banda = 400
    color_rojo = "#ce2b37"
    color_verde = "#009246"
    color_blanco = "#FFFFFF"

    Turtle.hideturtle()
    Turtle.penup()
    Turtle.goto(-ancho_banda/2, -alto_banda/2)
    Turtle.pendown()
    Turtle.showturtle()

    Turtle.begin_fill()

    Turtle.color(color_verde)
    Turtle.forward(ancho_banda/3)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.left(90)
    Turtle.forward(ancho_banda/3)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.end_fill()

    Turtle.penup()
    Turtle.left(90)
    Turtle.forward(ancho_banda/3)
    Turtle.pendown()

    Turtle.begin_fill()

    Turtle.color(color_blanco)
    Turtle.forward(ancho_banda/3)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.left(90)
    Turtle.forward(ancho_banda/3)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.end_fill()

    Turtle.penup()
    Turtle.left(90)
    Turtle.forward(ancho_banda/3)
    Turtle.pendown()

    Turtle.begin_fill()

    Turtle.color(color_rojo)
    Turtle.forward(ancho_banda/3)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.left(90)
    Turtle.forward(ancho_banda/3)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.end_fill()


     # Ocultar la tortuga y finalizar
    Turtle.hideturtle()
    time.sleep(10)
    
    # Cerrar la ventana
    Turtle.bye()
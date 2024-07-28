import turtle as Turtle
import time

def draw_france():

    Turtle.setup(700, 700)
    Turtle.bgcolor("Black")

    ancho_banda = 600
    alto_banda = 400
    color_rojo = "#FF0000"
    color_azul = "#002654"
    color_blanco = "#FFFFFF"

    Turtle.hideturtle()
    Turtle.penup()
    Turtle.goto(-ancho_banda/2, -alto_banda/2)
    Turtle.pendown()
    Turtle.showturtle()

    Turtle.begin_fill()

    Turtle.color(color_azul)
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
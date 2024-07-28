import turtle as Turtle
import time

def draw_benin():

    Turtle.setup(700, 700)

    ancho_banda = 600
    alto_banda = 400
    color_rojo = "#E8112D"
    color_amarillo = "#FCD116"
    color_verde = "#008751"

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

    Turtle.color(color_rojo)
    Turtle.forward((ancho_banda/3)*2)
    Turtle.left(90)
    Turtle.forward(alto_banda/2)
    Turtle.left(90)
    Turtle.forward((ancho_banda/3)*2)
    Turtle.left(90)
    Turtle.forward(alto_banda/2)
    Turtle.end_fill()

    Turtle.penup()
    Turtle.left(180)
    Turtle.forward(alto_banda/2)
    Turtle.pendown()

    Turtle.begin_fill()

    Turtle.color(color_amarillo)
    Turtle.forward(alto_banda/2)
    Turtle.right(90)
    Turtle.forward((ancho_banda/3)*2)
    Turtle.right(90)
    Turtle.forward(alto_banda/2)
    Turtle.right(90)
    Turtle.forward((ancho_banda/3)*2)
    Turtle.end_fill()

    # Ocultar la tortuga y finalizar
    Turtle.hideturtle()
    time.sleep(10)
    
    # Cerrar la ventana
    Turtle.bye()
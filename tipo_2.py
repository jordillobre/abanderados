import turtle

def dibujar(colores, fondo="white"):
    turtle.clearscreen()
    turtle.speed(3)
    turtle.setup(800, 800)
    turtle.bgcolor(fondo)
    turtle.clear()
    turtle.up()

    ancho_total = 640
    alto_total = 400
    anchura = ancho_total / len(colores)

    turtle.goto(-ancho_total / 2, alto_total / 2)
    turtle.down()

    for color in colores:
        turtle.color(color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(anchura)
            turtle.right(90)
            turtle.forward(alto_total)
            turtle.right(90)
        turtle.end_fill()
        turtle.up()
        turtle.forward(anchura)
        turtle.down()

    turtle.done()

import turtle
import spain
import france
import italy
import germany
import japan
import finland
import time
import benin

list_paises = ["españa", "francia", "italia", "alemania", "japon", "finlandia", "benin"]

def main():
    while True:
        pais = input("Ingrese el nombre de un país: ").lower()

        if pais in list_paises:
            if pais == "españa":
                spain.draw_spain()
            elif pais == "francia":
                france.draw_france()
            elif pais == "italia":
                italy.draw_italy()
            elif pais == "alemania":
                germany.draw_germany()
            elif pais == "japon":
                japan.draw_japan()
            elif pais == "finlandia":
                finland.draw_finland()
            elif pais == "benin":
                benin.draw_benin()
            break  
        elif pais == "salir":
            break 
        elif pais == "ayuda":
            ayuda = ', '.join([pais.capitalize() for pais in list_paises])
            print("Las banderas que puedo dibujar actualmente son:" , ayuda)
        else:
            print("El país ingresado no está en la lista. Inténtelo nuevamente.")

    print("Saliendo del programa.")
    time.sleep(1)

if __name__ == "__main__":
    main()
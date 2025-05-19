import turtle
import time
import tipo_1
import tipo_2
import tipo_3
import tipo_4
import tipo_5
from lista_paises import paises

dibujadores = {
    "tipo_1": tipo_1.dibujar,
    "tipo_2": tipo_2.dibujar
    # "tipo_3": tipo_3.dibujar,
    # "tipo_4": tipo_4.dibujar,
    # "tipo_5": tipo_5.dibujar
}

def buscar_pais(entrada):
    entrada = entrada.lower()
    for pais in paises:
        if entrada in pais["ids"]:
            return pais
    return None

def main():
    while True:
        entrada = input("Ingrese el nombre, ID o abreviación de un país (o 'ayuda' / 'salir'): ").lower()

        if entrada == "salir":
            break
        elif entrada == "ayuda":
            print("Puedo dibujar las siguientes banderas:\n")
            for p in paises:
                ids_str = ', '.join(p["ids"])
                print(f"{p['nombre']}: {ids_str}")
            print()  # línea extra de separación
        else:
            pais = buscar_pais(entrada)
            if pais:
                tipo = pais["tipo_bandera"]
                colores = pais["colores"]
                if colores:
                    dibujadores[tipo](colores, fondo=pais.get("fondo", "white"))
                else:
                    dibujadores[tipo](fondo=pais.get("fondo", "white"))
                break
            else:
                print("El país ingresado no está en la lista. Inténtelo nuevamente.")

    print("Saliendo del programa.")
    time.sleep(1)

if __name__ == "__main__":
    main()
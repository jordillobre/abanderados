El proyecto consiste en un programa que permite dibujar la bandera de un país determinado. Al ejecutarlo, lo primero que se solicita al usuario es el nombre de un país. Si el país introducido se encuentra en el listado de países disponibles, se generará una ventana donde se dibujará automáticamente su bandera con la ayuda de turtle. Una vez finalizado el dibujo, tras unos segundos, la ventana se cerrará y se dará por terminado el programa.

# Funcionalidades adicionales
* Si no se recuerda qué banderas están disponibles, se puede escribir `ayuda`, y el programa mostrará un listado con los países disponibles, junto con todos los identificadores válidos que se pueden usar para cada uno.
* No es necesario escribir el nombre completo del país. El programa también acepta identificadores alternativos como abreviaciones, códigos ISO o nombres simplificados. Por ejemplo, para España se puede introducir `España`, `es` o `esp`, y todos serán reconocidos como válidos.
* Si se introduce un nombre no reconocido, el programa mostrará un mensaje de error para que se pueda volver a intentar.
* En cualquier momento se puede escribir `salir` para cerrar el programa inmediatamente.


# Países disponibles actualmente
El proyecto es extensible, pero por ahora incluye banderas para los siguientes países:
* Alemania
* Armenia
* Austria
* Benín
* Bolivia
* Bulgaria
* España
* Estonia
* Etiopía
* Finlandia
* Gabón
* Hungría
* Indonesia
* Italia
* Japón
* Lituania
* Luxemburgo
* Mauricio
* Mónaco
* Países Bajos
* Polonia
* Rusia
* Sierra Leona
* Ucrania
* Yemen

# Estructura del código
Está dividido de la siguiente forma:
* **Archivo principal (main.py)**: gestiona la entrada del usuario, muestra las opciones disponibles (ayuda o salida), valida los datos introducidos y llama al módulo correspondiente para dibujar la bandera.
* **Listado de países (lista_paises.py)**: contiene una lista de diccionarios con todos los países disponibles. Cada entrada incluye el nombre del país, sus identificadores válidos (nombre, abreviaciones, códigos ISO), el tipo de diseño de su bandera, los colores (en formato hexadecimal), y el color de fondo más adecuado para visualizarla.
* **Módulos de dibujo (tipo_X.py)**: cada uno define cómo se dibujan banderas de una estructura específica (por ejemplo, tres franjas horizontales, verticales, una cruz, o combinaciones). Esto permite reutilizar la lógica de dibujo para múltiples países con banderas similares.

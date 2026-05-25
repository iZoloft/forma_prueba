# 🕹️ Ejercicio 3: Gestor de Homebrew Switch (Menú while)
# Desarrolla un sistema de gestión para la tarjeta SD de tu consola.

# Requisitos y Funcionalidades:

# Protección: Menú envuelto en su respectivo try/except.

# Variables Iniciales: Arrancas con espacio_sd = 256 (en GB) y apps_instaladas = 0.

# Menú Principal (while infinito):

# Instalar App / Juego Homebrew

# Formatear Tarjeta SD

# Apagar Consola

# Opción 1 (Instalar):

# Pide el peso de la App en GB.

# Validación (¡Acuérdate del else para el break!): El peso debe ser mayor a 0 y no puede superar el espacio_sd que te queda disponible.

# Camino Feliz: Resta el peso al espacio de la SD, suma 1 al contador de apps y muestra un mensaje de éxito.

# Opción 2 (Formatear - El Botón del Pánico):

# Esta opción no pide inputs. Simplemente reinicia la variable espacio_sd a 256, reinicia las apps_instaladas a 0 e imprime "Tarjeta SD formateada por completo".

# Opción 3 (Apagar):

# Imprime: "Consola apagada. Tienes {apps_instaladas} aplicaciones y te quedan {espacio_sd} GB libres."

# Rompe el ciclo del menú principal.

import os
os.system("cls")

menu = True
espacio_sd = 256
apps_instaladas = 0

while menu:
    print("=== Menú ===")
    print("1. Instalar app / Juego Homebrew")
    print("2. Formatear Tarjeta SD")
    print("3. Apagar consola")
    try:
        opcion = int(input("Ingrese opción: \n"))
        if opcion == 1:
            os.system("cls")
            print("1. Instalar app / Juego Homebrew")
            while True:
                peso = int(input("Ingrese peso de la app en GB \n"))
                if peso <= 0:
                    print("App debe pesar almenos 1gb")
                elif peso > espacio_sd:
                    print(f"No hay espacio suficiente. Te quedan {espacio_sd} GB libres.")
                else:
                    apps_instaladas = apps_instaladas + 1
                    espacio_sd = espacio_sd - peso
                    break
        elif opcion == 2:
            os.system("cls")
            print("2. Formatear Tarjeta SD")
            espacio_sd = 256
            apps_instaladas = 0
            print("Tarjeta SD formateada por completo")
        elif opcion == 3:
            os.system("cls")
            print(f"Consola apagada. Tienes {apps_instaladas} aplicaciones y te quedan {espacio_sd} GB libres.")
            menu = False
        else:
            os.system("cls")
            print("Opción no válida")
    except:
        os.system("cls")
        print("Valor debe ser numérico")
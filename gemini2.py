# Ejercicio 1: Gestión de la Habitación Terciopelo (Tipo "Estaciones de Trabajo")
# Desarrolla un programa en Python que permita a Igor gestionar el inventario de entidades a través de un menú interactivo. El sistema comienza con 20 espacios disponibles en el compendio.

# Interfaz del Programa:

# Mensaje inicial: "¡Bienvenido a la Habitación Terciopelo!"

# Menú principal:

# Espacios disponibles

# Reclutar Personas

# Fusionar Personas (Libera espacios)

# Registro de compendio

# Salir del Metaverso

# Requisitos y Funcionalidades:

# Protección General: El menú principal debe estar protegido con un try/except para evitar caídas si se ingresan letras.

# Opción 1 (Disponibles): Muestra cuántos espacios quedan actualmente vacíos en el inventario.

# Opción 2 (Reclutar): Pide la cantidad de Personas a registrar en el inventario (esto resta espacios disponibles).

# Validación 1: No puede ser 0 ni negativo (Mensaje: "Error: Debes reclutar al menos 1 Persona").

# Validación 2: No puede superar la cantidad de espacios vacíos disponibles (Mensaje: "Alerta: Capacidad insuficiente en el inventario").

# Opción 3 (Fusionar): Pide la cantidad de Personas que vas a fusionar (esto libera espacios y los devuelve al inventario).

# Validación 1: No puede ser 0 ni negativo.

# Validación 2: La suma de los espacios devueltos no puede hacer que el inventario supere su límite máximo original de 20 espacios.

# Opción 4 (Registro): Muestra un único contador llamado flujo_compendio que se incrementa al reclutar y disminuye al fusionar. (Imprime: "Flujo de actividad en el compendio: {flujo_compendio}").

# Opción 5 (Salir): Finaliza el ciclo e imprime "Cerrando conexión. Despierta, Trickster.".

import os, time
os.system("cls")

acceso = True
espacios_disponibles = 20
flujo_compendio = 0

print("Bienvenido a la Habitación Terciopelo!")
while acceso:
    print("=== Menú Principal ===")
    print("1. Espacios Disponibles")
    print("2. Reclutar Personas")
    print("3. Fusionar Personas (Liberar)")
    print("4. Registro Compendio")
    print("5. Salir del Metaverso")
    try:
        opcion = int(input("Ingrese opción: \n"))
        if opcion == 1:
            os.system("cls")
            print("1. Espacios Disponibles")
            print(f"Los espacios disponibles son {espacios_disponibles}")
            time.sleep(2)
        elif opcion == 2:
            os.system("cls")
            print("2. Reclutar Personas")
            while True:
                reclutar = int(input("Cuantas personas desea reclutar? \n"))
                if reclutar <= 0:
                    print("Debes reclutar almenos a una persona")
                elif reclutar > espacios_disponibles:
                    print("No hay suficientes personas")
                else:
                    espacios_disponibles = espacios_disponibles - reclutar
                    flujo_compendio = flujo_compendio + reclutar
                    break
        elif opcion == 3:
            os.system("cls")
            print("3. Fusionar Personas")
            while True:
                fusionar = int(input("Cuantas personas desea fusionar? \n"))
                if fusionar <= 0:
                    print("Debes fusionar almenos a una persona")
                elif (espacios_disponibles + fusionar) > 20:
                    print("Capacidad insuficiente en el inventario")
                else:
                    espacios_disponibles = espacios_disponibles + fusionar
                    flujo_compendio = flujo_compendio - fusionar
                    break   
        elif opcion == 4:
            os.system("cls")
            print(f"Registro de compendio: {flujo_compendio}")
            time.sleep(2)
        elif opcion == 5:
            os.system("cls")
            print("5. Salir del Metaverso")
            print("Cerrando conexión. Despierta, Trickster")
            time.sleep(2)
            acceso = False
        else:
            os.system("cls")
            print("Opción no es Válida")
    except:
        print("Valor debe ser numérico")
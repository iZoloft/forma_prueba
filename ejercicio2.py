# Ejercicio 2 (60 puntos)
# Construya un programa en Python que permita gestionar un sistema simple de estaciones de trabajo para un centro de cómputo por medio de un menú de opciones.
# El programa debe comenzar con 25 estaciones disponibles previamente cargadas.

# Interfaz del Programa
# Bienvenida
# ¡Bienvenido al sistema de gestión de estaciones del Centro de Cómputo!

# Menú Principal
# El programa debe mostrar el siguiente menú:

# === MENÚ PRINCIPAL ===
# 1.	Estaciones disponibles
# 2.	Asignar estación
# 3.	Liberar estación
# 4.	Historial de uso
# 5.	Salir

# Funcionalidades del Sistema
# 1. Estaciones Disponibles
# •	Mostrar la cantidad de estaciones disponibles en el centro.
# •	Este valor debe actualizarse conforme se realicen asignaciones o liberaciones.

# 2. Asignar Estación
# •	Permite asignar estaciones a usuarios.
# •	Se debe solicitar la cantidad de estaciones a asignar.
# •	Este número debe cumplir las siguientes validaciones:
# o	No puede ser menor o igual a 0.
# o	No debe superar la cantidad de estaciones disponibles.

# 3. Liberar Estación
# •	Permite liberar estaciones de usuarios.
# •	Se debe solicitar la cantidad de estaciones a liberar, validando que:
# •	Sea mayor a 0.
# •	No supere la capacidad máxima (25 estaciones).
# •	Esta acción incrementará el número de estaciones disponibles.

# 4. Historial de Uso
# •	Mostrar la cantidad de asignaciones realizadas durante la sesión.
# •	Las liberaciones disminuyen el historial.
# •	 Las asignaciones aumentan el historial.

# 5. Salir del Sistema
# •	Al seleccionar esta opción, el programa debe finalizar su ejecución mostrando el mensaje:
# "Gracias por utilizar nuestro software, hasta la próxima."

# Si el usuario desea asignar estaciones, se debe validar que haya suficiente capacidad dispo-nible. En caso de que no haya suficientes, debe informarse al usuario. La opción 4 debe mostrar el total de asignaciones realizadas durante la sesión (contador separado). El progra-ma debe repetirse hasta que el usuario elija salir.

import os, time
os.system("cls")

estaciones_disponibles = 25
historial_uso = 0
historial_liberar = 0
historial_asignar = 0
acceso = True

while acceso:
    print("=== Menú Principal ===")
    print("1. Estaciones Disponibles")
    print("2. Asignar Estación")
    print("3. Liberar Estación")
    print("4. Historial de uso")
    print("5. Salir")
    try:
        opcion = int(input("Ingrese opción \n"))
        if opcion == 1:
            os.system("cls")
            print("1. Estaciones Disponibles")
            print(f"Las estaciones disponibles son {estaciones_disponibles}")
            time.sleep(2)
        elif opcion == 2:
            os.system("cls")
            print("2. Asignar Estación")
            while True:
                asignar = int(input("Cuantas estaciones desea asignar?\n"))
                if asignar <= 0:
                    print("Valor debe ser mayor a 0")
                elif asignar > estaciones_disponibles:
                    print("No hay suficientes estaciones")
                else:
                    estaciones_disponibles = estaciones_disponibles - asignar
                    historial_uso = historial_uso + 1
                    historial_asignar = historial_asignar + asignar 
                    break
        elif opcion == 3:
            os.system("cls")
            print("3. Liberar Estación")
            while True:
                liberar = int(input("Cuantas estaciones desea liberar?\n"))
                if liberar <= 0:
                    print("Valor debe ser mayor a 0")
                elif (estaciones_disponibles + liberar) > estaciones_disponibles:
                    print("No puedes liberar mas estaciones de las que hay")
                else:
                    estaciones_disponibles = estaciones_disponibles + liberar
                    historial_uso = historial_uso + 1
                    historial_liberar = historial_asignar + liberar
                    break
        elif opcion == 4:
            os.system("cls")
            print(f"Se han asignado {historial_asignar} estaciones")
            print(f"Se han liberado {historial_liberar} estaciones")
            print(f"Se han usado {historial_uso} peticiones para estaciones")
            time.sleep(3)
        elif opcion == 5:
            os.system("cls")
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            acceso = False
        else:
            os.system("cls")
            print("Debes colocar una opción válida")
    except:
        print("Valor debe ser numérico")

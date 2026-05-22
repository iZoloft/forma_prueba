# 🍕 Ejercicio 2: Turno Nocturno en Melt Pizzas (Tipo "Menú + Strings")
# Desarrolla un programa en Python para gestionar los pedidos nocturnos de la sucursal. El sistema comienza el turno con un stock crítico de 25 masas disponibles.

# Interfaz del Programa:

# Mensaje inicial: "¡Iniciando turno nocturno!"

# Menú principal:

# Revisar Stock de Masas

# Ingresar Pedido (Chicken BBQ / Canadian Bacon)

# Registrar Merma (Masas defectuosas)

# Resumen y Cierre de Caja

# Requisitos y Funcionalidades:

# Protección General: El menú debe estar envuelto en un try/except.

# Opción 1 (Stock): Imprime "Masas disponibles en cocina: {masas}".

# Opción 2 (Pedido): * Pide la cantidad de pizzas a preparar en este pedido.

# Validación 1: Debe ser mayor a 0. (Mensaje: "Error: Debe ingresar al menos 1 pizza.")

# Validación 2: No puede superar el stock actual. (Mensaje: "Alerta: Stock de masas insuficiente.")

# Validación 3 (El Jefe de Local): Si logró pasar las validaciones de números, ahora el sistema debe pedir el Nombre del Cliente para la boleta. El nombre debe tener al menos 4 caracteres y NO debe contener espacios.

# Si el cliente no cumple la regla de texto, muestra: "Error: El nombre debe tener mínimo 4 letras y escribirse todo junto." (El programa debe insistir hasta que lo escriba bien).

# Camino Feliz: Si pasó los números y el texto, se restan las masas y se suma 1 a un contador de pedidos_exitosos.

# Opción 3 (Merma): Alguien botó masas al piso. Pide la cantidad de masas a desechar.

# Validación 1: Mayor a 0. (Mensaje: "Error: Ingrese una cantidad válida.")

# Validación 2: No puede superar las masas que quedan. (Mensaje: "Error: No puede mermar más masas de las que hay.")

# Camino Feliz: Resta las masas del inventario total.

# Opción 4 (Cierre): Rompe el ciclo del menú e imprime el mensaje: "Turno terminado. Total de pedidos despachados: {pedidos_exitosos}".\

import os
os.system("cls")

masas_disponibles = 25
menu = True
pedidos_exitosos = 0

print("¡Iniciando turno nocturno!")
while menu:
    print("1. Revisar stock de masas")
    print("2. Ingresar pedido (Chicken BBQ / Canadian Bacon)")
    print("3. Registrar Merma (Masas defectuosas)")
    print("4. Resumen y Cierre de Caja")
    try:
        opcion = int(input("Ingrese opción \n"))
        if opcion == 1:
            os.system("cls")
            print("1. Revisar stock")
            print(f"Masas disponibles en cocina: {masas_disponibles}")
        elif opcion == 2:
            os.system("cls")
            while True:
                print("2. Ingresar pedido (Chicken BBQ / Canadian Bacon)")
                cantidad = int(input("Ingrese cantidad de pizzas a preparar: \n"))
                if cantidad <= 0:
                    print("Error: Debe ingresar al menos 1 pizza.")
                elif cantidad > masas_disponibles:
                    print("Alerta: Stock de masas insuficiente.")
                else:
                    nombre = ""
                    while len(nombre) < 4 or " " in nombre:
                        nombre = input("Ingrese nombre del cliente: \n")
                        if len(nombre) < 4:
                            print("El nombre debe contener almenos 4 caracteres")
                        if " " in nombre:
                            print("El nombre no debe contener espacios")
                    pedidos_exitosos = pedidos_exitosos + 1
                    masas_disponibles = masas_disponibles - cantidad
                    break
        elif opcion == 3:
            os.system("cls")
            print("3. Registrar Merma (Masas defectuosas)")
            while True:
                merma = int(input("Ingrese cantidad de masas a desechar: \n"))
                if merma <= 0:
                    print("Error: Ingrese una cantidad válida.")
                elif merma > masas_disponibles:
                    print("Error: No puede mermar más masas de las que hay.")
                else:
                    masas_disponibles = masas_disponibles - merma
                    break
        elif opcion == 4:
            os.system("cls")
            print("4. Resumen y Cierre de Caja")
            print(f"Turno terminado. Total de pedidos despachados: {pedidos_exitosos}")
            menu = False
    except:
        print("Valor debe ser numérico")
# 🪖 Ejercicio 1: Despliegue en Battlefield 6 (Tipo "Menú + Strings")
# Desarrolla un sistema para gestionar los recursos de tu patrulla antes de entrar a la zona de guerra. El equipo comienza la partida con 500 Tickets de refuerzo.

# Interfaz del Programa:

# Mensaje inicial: "¡Bienvenido al centro de mando!"

# Menú principal:

# Revisar Tickets de Refuerzo

# Solicitar Vehículo Blindado

# Registrar Nuevo Soldado

# Desconectar del Servidor

# Requisitos y Funcionalidades:

# Protección: Todo el menú debe estar envuelto en un try/except general para evitar que explote si ingresan letras.

# Opción 1 (Tickets): Imprime "Tickets restantes en el servidor: {tickets}".

# Opción 2 (Vehículo):

# Pide la cantidad de tickets a gastar para desplegar el vehículo.

# Validación 1: El costo debe ser mayor a 0. (Mensaje: "Error: El costo del vehículo debe ser positivo.")

# Validación 2: El costo no puede superar los tickets actuales. (Mensaje: "Alerta: No hay suficientes tickets para este despliegue.")

# Camino Feliz: Si pasa las validaciones, resta los tickets del total e imprime "Vehículo desplegado en combate."

# Opción 3 (Soldado):

# Pide el Gamertag (nombre) del nuevo integrante de la patrulla.

# Validación (Ciclo while de texto): El nombre debe tener al menos 5 caracteres y NO debe contener espacios.

# Si falla el largo: "Error: El Gamertag debe tener al menos 5 caracteres."

# Si tiene espacios: "Error: El Gamertag no puede tener espacios."

# Camino Feliz: Suma 1 a un contador de soldados_registrados (que debe partir en 0 antes del menú principal) e imprime "Soldado registrado en la patrulla."

# Opción 4 (Salir): Imprime "Cerrando conexión. Soldados registrados hoy: {soldados_registrados}" y rompe el ciclo para terminar el programa.

import os
os.system("cls")

programa = True
tickets = 500
soldados_registrados = 0

print("¡Bienvenido al centro de mando!")
while programa:
    print("=== Menú Principal ===")
    print("1. Revisar Tickets de Refuerzo")
    print("2. Solicitar Vehículo Blindado")
    print("3. Registrar Nuevo Soldado")
    print("4. Desconectar del Servidor")
    try:
        opcion = int(input("Ingresar opción: \n"))
        if opcion == 1:
            os.system("cls")
            while True:
                print(f"Tickets restantes en el servidor: {tickets}")
                break
        elif opcion == 2:
            os.system("cls")
            while True:
                vehiculo = int(input("Ingrese tickets a gastar para solicitar vehículo \n"))
                if vehiculo <= 0:
                    print("Error: El costo del vehículo debe ser positivo.")
                elif vehiculo > tickets:
                    print("Alerta: No hay suficientes tickets para este despliegue.")
                else:
                    tickets = tickets - vehiculo
                    print("Vehículo desplegado en combate")
                    break
        elif opcion == 3:
            os.system("cls")
            gamertag = ""
            while len(gamertag) < 5 or " " in gamertag:
                gamertag = input("Ingrese su gamertag: \n")
                if len(gamertag) < 5:
                    print("Gamertag debe contener almenos 5 caracteres")
                if " " in gamertag:
                    print("Gamertag no debe contener espacios")
            soldados_registrados = soldados_registrados + 1
            os.system("cls")
            print("Soldado registrado en patrulla")
        elif opcion == 4:
            os.system("cls")
            print(f"Cerrando conexión. Soldados registrados hoy: {soldados_registrados}")
            programa = False
        else:
            os.system("cls")
            print("Opción no válida")
    except:
        os.system("cls")
        print("Valor debe ser numérico")
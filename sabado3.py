# 🐧 El Desafío Final: Administrador de Servidores CentOS (Menú while)
# Tal como pediste, cerramos la noche volviendo al menú infinito para no perder el hilo de esa estructura. Nos ponemos en modo SysAdmin para gestionar los recursos de un servidor.

# Requisitos y Funciones:

# Protección General: El menú completo protegido por su try/except.

# Variables de Preparación: El servidor arranca con ram_disponible = 128 (en GB) y un contador de vms_desplegadas = 0 (Máquinas Virtuales).

# Menú Principal (while infinito):

# Desplegar Máquina Virtual

# Registrar Usuario Administrador

# Cerrar Sesión

# Opción 1 (Desplegar VM):

# Pregunta: "¿Cuánta memoria RAM en GB desea asignar a la nueva máquina?"

# Validación 1: Debe ser mayor a 0.

# Validación 2: No puede superar la ram_disponible.

# Camino Feliz: Resta la RAM solicitada a la ram_disponible, suma 1 a las vms_desplegadas e imprime "Máquina Virtual desplegada con éxito".

# Opción 2 (Registrar Usuario - Strings):

# Pregunta: "Ingrese el nombre del nuevo usuario root: "

# Validación de texto: El nombre debe tener al menos 5 caracteres y NO debe tener espacios. Usa una jaula while para atraparlo si se equivoca, mostrándole mensajes de error específicos (igual que con el Gamertag de ayer).

# Camino Feliz: Imprime "Usuario {nombre} registrado con permisos de administrador."

# Opción 3 (Cerrar Sesión):

# Imprime:

# "--- Resumen del Servidor ---"

# "Máquinas Virtuales Activas: {vms_desplegadas}"

# "Memoria RAM restante: {ram_disponible} GB"

# Rompe el ciclo del menú principal.

import os
os.system("cls")

ram_disponible = 128
vms_desplegados = 0
menu = True

while menu:
    print("--- Menú ---")
    print("1. Desplegar Máquina Virtual")
    print("2. Registrar Usuario Administrador")
    print("3. Cerrar Sesión")
    try:
        opcion = int(input("Ingrese opción \n"))
        if opcion == 1:
            os.system("cls")
            while True:
                asignar_ram = int(input("¿Cuánta memoria RAM en GB desea asignar a la nueva máquina? \n"))
                if asignar_ram <= 0:
                    print("Debes asignar por lo menos 1GB de ram")
                elif asignar_ram > ram_disponible:
                    print("No puedes superar la ram disponible")
                else:
                    ram_disponible = ram_disponible - asignar_ram
                    vms_desplegados = vms_desplegados + 1
                    print("Máquina Virtual Desplegada con éxito")
                    break
        elif opcion == 2:
            os.system("cls")
            usuario = ""
            while len(usuario) < 5 or " " in usuario:
                usuario = input("Ingrese el nombre del nuevo usuario root: \n")
                if len(usuario) < 5:
                    print("Nombre de usuario root debe tener almenos 5 caracteres")
                if " " in usuario:
                    print("Nombre de usuario root no debe contener espacios")
            print(f"Usuario {usuario} registrado con permisos de administrador")
        elif opcion == 3:
            os.system("cls")
            print("--- Resumen del Servidor ---")
            print(f"Máquinas Virtuales Activas: {vms_desplegados}")
            print(f"Memoria RAM restante: {ram_disponible} GB")
            menu = False
        else:
            os.system("cls")
            print("Opción no válida")
    except:
        print("Valor debe ser numérico")
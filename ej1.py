# 🤠 Ejercicio 1: El Libro de Contabilidad del Campamento (Tipo "Menú de Gestión")
# Desarrolla un programa en Python que permita a Arthur Morgan gestionar los fondos de la banda de Van der Linde a través de un menú interactivo. El sistema comienza el día con $150 dólares en la caja fuerte.

# Interfaz del Programa:

# Mensaje inicial (antes del menú): "¡Bienvenido al libro de contabilidad del campamento!"

# Menú principal:

# Revisar caja fuerte

# Aportar fondos

# Comprar suministros

# Historial del libro

# Cerrar libro

# Requisitos y Funcionalidades:

# Protección General: El menú debe estar protegido con un try/except para evitar caídas si se ingresan letras en lugar de la opción o los montos.

# Opción 1 (Caja Fuerte): Muestra cuánto dinero hay actualmente. (Imprime: "Fondos actuales: ${caja_fuerte}").

# Opción 2 (Aportar): Pide la cantidad de dinero a donar a la caja (esto suma a los fondos).

# Validación 1: No puede ser 0 ni negativo. Si falla, el programa debe insistir mostrando el mensaje exacto: "Error: La donación debe ser un monto positivo."

# Opción 3 (Suministros): Pide la cantidad de dinero a gastar (esto resta de los fondos).

# Validación 1: No puede ser 0 ni negativo. Si falla, muestra: "Error: El gasto debe ser mayor a 0."

# Validación 2: No puede superar la cantidad de dinero que hay actualmente en la caja. Si falla, muestra: "Alerta: No hay suficientes fondos en la caja."

# Opción 4 (Historial): Muestra un único contador llamado transacciones que aumenta en 1 cada vez que alguien aporta fondos o compra suministros. (Imprime: "Total de movimientos en el libro: {transacciones}").

# Opción 5 (Cerrar): Finaliza el ciclo while del menú e imprime el mensaje final: "Cerrando el libro. ¡Buen trabajo, Arthur!"

import os
os.system("cls")

flag = True
caja_fuerte = 150
transacciones = 0

print("¡Bienvenido al libro de contabilidad del campamento!")
while flag:
    print("=== Menú Principal ===")
    print("1. Revisar Caja Fuerte")
    print("2. Aportar Fondos")
    print("3. Comprar suministros")
    print("4. Historial del Libro")
    print("5. Cerrar Libro")
    try:
        opcion = int(input("Ingrese opción \n"))
        if opcion == 1:
            os.system("cls")
            print(f"Fondos actuales: ${caja_fuerte}")
        elif opcion == 2:
            os.system("cls")
            while True:
                aportar = int(input("Cuanto dinero desea aportar? \n $ "))
                if aportar <= 0:
                    print("Error: La donación debe ser un monto positivo.")
                else:
                    caja_fuerte = caja_fuerte + aportar
                    transacciones = transacciones + 1
                    break
        elif opcion == 3:
            os.system("cls")
            while True:
                suministros = int(input("Cuanto va a gastar en suministros? \n $ "))
                if suministros <= 0:
                    print("Error: El gasto debe ser mayor a 0.")
                elif suministros > caja_fuerte:
                    print("Alerta: No hay suficientes fondos en la caja.")
                else:
                    caja_fuerte = caja_fuerte - suministros
                    transacciones = transacciones + 1
                    break
        elif opcion == 4:
            os.system("cls")
            print(f"Total de movimientos en el libro: {transacciones}")
        elif opcion == 5:
            os.system("cls")
            print("Cerrando el libro. ¡Buen trabajo, Arthur!")
            flag = False
        else:
            os.system("cls")
            print("Opción no valida, intente otra vez")
        
    except:
        print("Valor debe ser numérico")

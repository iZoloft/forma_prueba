# 🖥️ Ejercicio 4: Tienda de Hardware (Menú while + Strings)
# Requisitos y Funcionalidades:

# Variables Iniciales: Arrancas el día con stock_ryzen = 10 y stock_radeon = 5.

# Menú Principal (while infinito con try/except general):

# Vender Procesador (Ryzen 5 5600)

# Vender Tarjeta de Video (Radeon RX 9060 XT 16GB)

# Registrar Cliente Mayorista

# Cerrar Tienda

# Opción 1 y Opción 2 (Ventas):

# Ambas opciones funcionan con la misma lógica, pero cada una resta a su propia variable de stock.

# Pregunta: "¿Cuántas unidades desea comprar?"

# Validación: Usa tu jaula con else: break. La cantidad debe ser mayor a 0 y no puede superar el stock disponible del producto que están comprando. Muestra mensajes de error específicos para cada caso.

# Camino Feliz: Resta la cantidad al stock correspondiente e imprime "Venta realizada con éxito".

# Opción 3 (Registrar Cliente - Strings):

# Pregunta: "Ingrese el ID de Discord del cliente mayorista: "

# Validación de texto (Jaula while): El ID debe tener al menos 6 caracteres y NO debe tener espacios. Usa los if correspondientes para retar al usuario si se equivoca.

# Camino Feliz: Imprime "Cliente {id_discord} registrado como mayorista."

# Opción 4 (Cerrar):

# Imprime: "Stock final - Ryzen: {stock_ryzen} | Radeon: {stock_radeon}".

# Rompe el menú principal.

import os
os.system("cls")

stock_ryzen = 10
stock_radeon = 5
menu = True

while menu:
    print("=== Menú ===")
    print("1. Vender Procesador (Ryzen 5 5600)")
    print("2. Vender Tarjeta de Video (Radeon RX 9060 XT 16GB)")
    print("3. Registrar Cliente Mayorista")
    print("4. Cerrar Tienda")
    try:
        opcion = int(input("Ingrese opción: \n"))
        if opcion == 1:
            os.system("cls")
            print("1. Vender Procesador (Ryzen 5 5600)")
            while True:
                comprar_ryzen = int(input("¿Cuántas unidades desea comprar? \n"))
                if comprar_ryzen <= 0:
                    print("Debe comprar almenos una unidad")
                elif comprar_ryzen > stock_ryzen:
                    print(f"Stock insuficiente, quedan {stock_ryzen} unidades")
                else:
                    stock_ryzen = stock_ryzen - comprar_ryzen
                    print("Venta realizada con éxito")
                    break
        elif opcion == 2:
            os.system("cls")
            print("2. Vender Tarjeta de Video (Radeon RX 9060 XT 16GB)")
            while True:
                comprar_radeon = int(input("¿Cuántas unidades desea comprar? \n"))
                if comprar_radeon <= 0:
                    print("Debe comprar almenos una unidad")
                elif comprar_radeon > stock_radeon:
                    print(f"Stock insuficiente, quedan {stock_radeon} unidades")
                else:
                    stock_radeon = stock_radeon - comprar_radeon
                    print("Venta realizada con éxito")
                    break
        elif opcion == 3:
            os.system("cls")
            print("3. Registrar Cliente Mayorista")
            cliente = ""
            while len(cliente) < 6 or " " in cliente:
                cliente = input("Ingrese el ID de Discord del cliente mayorista \n")
                if len(cliente) < 6:
                    print("El ID debe tener un mínimo de 6 caracteres")
                if " " in cliente:
                    print("ID no debe contener espacios")
            print(f"Cliente {cliente} registrado como mayorista.")
        elif opcion == 4:
            os.system("cls")
            print("4. Cerrar Tienda")
            print(f"Stock final - Ryzen: {stock_ryzen} | Radeon: {stock_radeon}")
            menu = False
        else:
            os.system("cls")
            print("Opción no válida")
    except:
        os.system("cls")
        print("Valor debe ser numérico")
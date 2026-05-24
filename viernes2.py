# 💻 Ejercicio 2: El Taller de Hardware (El Jefe Final con for)
# Tal como pediste, dejamos el teleférico, las pizzas y los juegos atrás. Nos ponemos el delantal de servicio técnico para este último desafío que combina el menú infinito, las validaciones y el ciclo for.

# Interfaz del Programa:

# Mensaje inicial: "¡Bienvenido al sistema de diagnóstico de PC!"

# Menú principal:

# Vender Componentes

# Test de Estrés (Benchmark)

# Cerrar Taller

# Requisitos y Funcionalidades:

# Variables Iniciales: Arrancas el día con un stock_piezas = 30 y un contador de equipos_testeados = 0.

# Protección General: Menú envuelto en su respectivo try/except.

# Opción 1 (Vender):

# Pide la cantidad de componentes a comprar.

# Validación 1: Debe ser mayor a 0. (Mensaje: "Error: La cantidad debe ser al menos 1.")

# Validación 2: No puede superar el stock. (Mensaje: "Error: Solo nos quedan {stock_piezas} piezas en inventario.")

# Camino Feliz: Resta los componentes del inventario e imprime "Venta registrada con éxito."

# Opción 2 (Test de Estrés - El ciclo for):

# Pregunta al usuario: "¿Cuántos minutos durará el test de estrés?" (Asume que pondrá un número positivo).

# Usa un ciclo for y range() para que los minutos vayan desde el 1 hasta la cantidad exacta que pidió el usuario.

# Por cada minuto (vuelta), el sistema simula que la temperatura sube. La fórmula matemática es: temperatura = 40 + (minuto * 8) (donde 'minuto' es la variable de tu for).

# Imprime: "Minuto {minuto}: La temperatura del procesador es de {temperatura}°C".

# El Seguro Térmico: Justo después del print, revisa si la temperatura es mayor o igual a 90. Si es así, imprime "¡Peligro! Thermal Throttling detectado. Apagando equipo para evitar daños." y destruye el ciclo for con un break.

# Camino Feliz: Independiente de si el equipo sobrevivió o se apagó por seguridad, una vez que termina (o se rompe) el ciclo for, súmale 1 al contador de equipos_testeados.

# Opción 3 (Cerrar): Imprime "Taller cerrado. Total de equipos testeados hoy: {equipos_testeados}" y termina el programa.

import os
os.system("cls")

programa = True
stock_piezas = 30
equipos_testeados = 0

print("¡Bienvenido al sistema de diagnóstico de PC!")
while programa:
    print("=== Menú Principal ===")
    print("1. Vender Componentes")
    print("2. Test de Estrés (Benchmark)")
    print("3. Cerrar Taller")
    try:
        opcion = int(input("Ingrese opción: \n"))
        if opcion == 1:
            os.system("cls")
            while True:
                comprar = int(input("Ingrese cantidad de componentes a comprar: \n"))
                if comprar < 0:
                    print("Error: La cantidad debe ser al menos 1.")
                elif comprar > stock_piezas:
                    print(f"Error: Solo nos quedan {stock_piezas} piezas en inventario.")
                else:
                    print("Venta registrada con éxito!")
                    stock_piezas = stock_piezas - comprar
                    break
        elif opcion == 2:
            os.system("cls")
            test = int(input("¿Cuántos minutos durará el test de estrés? \n"))
            equipos_testeados = equipos_testeados + 1
            for x in range(1, test + 1):
                temperatura = 40 + (x * 8)
                print(f"Minuto {x}: La temperatura del procesador es de {temperatura}°C")
                if temperatura >= 90:
                    print("¡Peligro! Thermal Throttling detectado. Apagando equipo para evitar daños.")
                    break
        elif opcion == 3:
            print(f"Taller cerrado. Total de equipos testeados hoy: {equipos_testeados}")
            programa = False
        else:
            os.system("cls")
            print("Opción no válida")
    except:
        print("Valor debe ser numérico")
# 💻 Ejercicio 3: El Laboratorio del for (Benchmark de Hardware)
# Desarrolla un pequeño script para realizar un "stress test" (prueba de rendimiento) a una tarjeta de video.

# Requisitos y Funcionalidades:

# Variables Iniciales: La temperatura base de la GPU antes de empezar es de 40°C.

# Ingreso de datos: Pregunta al usuario: "¿Cuántos ciclos de prueba desea ejecutar?" (Nota: No te preocupes por validar este input, asume que el usuario pondrá un número positivo. Enfoquémonos 100% en el for).

# El Ciclo de Prueba: Utiliza un ciclo for y la herramienta range() para dar exactamente la cantidad de vueltas que pidió el usuario. Recuerda que los ciclos deben numerarse partiendo desde el 1.

# Por cada vuelta del ciclo, debe ocurrir lo siguiente en este orden:

# La temperatura de la tarjeta aumenta en 5°C.

# Imprime el reporte: "Ciclo {numero_ciclo}: La temperatura subió a {temperatura}°C".

# El Seguro Térmico: Inmediatamente después del print, el programa debe evaluar la temperatura. Si es mayor o igual a 85°C, debe imprimir "¡Peligro! Límite térmico alcanzado. Abortando benchmark." y destruir el ciclo for de forma anticipada para que la tarjeta no se queme.

import os
os.system("cls")

temperatura = 40

try:
    ciclos_prueba = int(input("¿Cuántos ciclos de prueba desea ejecutar? \n"))
    for x in range(1, ciclos_prueba + 1):
        temperatura = temperatura + 5
        print(f"Ciclo {x}: La temperatura subió a {temperatura}")
        if temperatura >= 85:
            print("¡Peligro! Límite térmico alcanzado. Abortando benchmark.")
            break
except:
    print("Valor debe ser numérico")
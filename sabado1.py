# 🎮 Ejercicio 1: Instalador de Archivos PKG (Ciclo for - Ingreso por Lote)
# Desarrolla un programa que gestione la instalación de una lista de respaldos (archivos PKG) en una consola modificada con HEN. El sistema debe clasificar los juegos según su peso y entregar un reporte final.

# Requisitos y Funcionalidades:

# Protección General: Todo el programa debe estar envuelto en un try/except para evitar caídas si el usuario teclea letras en vez de números.

# Variables de Preparación: Antes de empezar, crea contadores para juegos_indie, juegos_estandar y juegos_pesados. Crea también un acumulador para el almacenamiento_total (en GB).

# Definir el Límite (Jaula 1):

# El programa debe preguntar primero: "¿Cuántos archivos PKG desea instalar hoy?"

# Validación: Debe ser un número mayor a 0. Si ingresan 0 o negativo, muestra "Error: La cantidad de archivos debe ser mayor a 0." y vuelve a preguntar hasta que ingrese un número válido.

# El Motor Principal (Ciclo for):

# Usa un ciclo for y range() para dar exactamente la cantidad de vueltas que el usuario indicó en el paso anterior.

# Ingreso y Validación del Peso (Jaula 2 - Adentro del for):

# Por cada vuelta, pide el peso del archivo: "Ingrese el peso del PKG en GB: " (asume números enteros).

# Validación: El peso debe ser mayor a 0. Si es inválido, muestra "Error: El peso debe ser mayor a 0 GB." y atrápalo en la jaula hasta que lo ingrese bien.

# Clasificación (Adentro del for, camino feliz):

# Una vez que tienes un peso válido, súmalo inmediatamente al almacenamiento_total.

# Si el PKG pesa menos de 2 GB: Suma 1 a los juegos_indie.

# Si el PKG pesa entre 2 y 10 GB (inclusive): Suma 1 a los juegos_estandar.

# Si el PKG pesa más de 10 GB: Suma 1 a los juegos_pesados.

# Salida Final (Fuera del ciclo for):

# Al terminar todas las instalaciones, imprime el reporte:

# "--- Resumen de Instalación HEN ---"

# "Juegos Indie (< 2GB): {juegos_indie}"

# "Juegos Estándar (2-10GB): {juegos_estandar}"

# "Juegos Pesados (> 10GB): {juegos_pesados}"

# "Espacio total consumido: {almacenamiento_total} GB"

import os
os.system("cls")

juegos_indie = 0
juegos_estandar = 0
juegos_pesados = 0
almacenamiento_total = 0

try:
    archivos = 0
    while archivos <= 0:
        archivos= int(input("¿Cuántos archivos PKG desea instalar hoy? \n"))
        if archivos <= 0:
            print("Debe haber almenos un archivo")
    for x in range(1, archivos + 1):
        peso = 0
        while peso <= 0:
            peso = int(input("Ingrese el peso del PKG en GB \n"))
            if peso <= 0:
                print("El peso debe ser mayor a 0GB")
        almacenamiento_total = almacenamiento_total + peso
        print(f"El peso del archivo {x} es de {peso} GB")
        if peso < 2:
            juegos_indie = juegos_indie + 1
        elif peso >= 2 and peso <= 10:
            juegos_estandar = juegos_estandar + 1
        else:
            juegos_pesados = juegos_pesados + 1
    print("--- Resumen de Instalación HEN ---")
    print(f"Juegos Indie (< 2GB): {juegos_indie}")
    print(f"Juegos Estándar (2-10GB): {juegos_estandar}")
    print(f"Juegos Pesados (> 10GB): {juegos_pesados}")
    print(f"Espacio total consumido: {almacenamiento_total} GB")
except:
    print("Valor debe ser numérico")
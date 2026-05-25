# 🪖 Ejercicio 2: Polígono de Tiro en Battlefield 6 (Ciclo for libre)
# Estás calibrando armas en el campo de pruebas. El sistema evaluará tu precisión calculando el puntaje según la distancia de los objetivos abatidos.

# Requisitos y Funcionalidades:

# Protección: Todo envuelto en un try/except general.

# Preparación: Crea contadores inicializados en cero para bajas_cortas, bajas_medias y bajas_francotirador. Crea también un acumulador para el puntaje_total.

# Límite Inicial (Aduana 1): Pregunta "¿Cuántos objetivos aparecerán en esta ronda?".

# Validación del Límite: Debe ser mayor a 0.

# Motor Principal: Ciclo for según la cantidad exacta de objetivos.

# Aduana Interna (Adentro del for): Pregunta "Ingrese la distancia del objetivo abatido en metros:"

# Validación Interna: La distancia debe ser un número positivo (mayor a 0). Atrapa al usuario si ingresa cero o negativos.

# Clasificación y Puntaje (Adentro del for):

# Menos de 50 metros: Suma 1 a bajas_cortas y suma 10 puntos al puntaje_total.

# Entre 50 y 150 metros (inclusive): Suma 1 a bajas_medias y suma 25 puntos al puntaje_total.

# Más de 150 metros: Suma 1 a bajas_francotirador y suma 50 puntos al puntaje_total.

# Reporte Final (Fuera del for): Imprime un desglose mostrando cuántas bajas hubo por cada distancia y el puntaje total obtenido en la ronda.

import os
os.system("cls")

bajas_cortas = 0
bajas_medias = 0
bajas_franco = 0
puntaje_total = 0

try:
    while True:
        objetivos = int(input("¿Cuántos objetivos aparecerán en esta ronda? \n"))
        if objetivos <= 0:
            print("Debe colocar almenos un objetivo")
        else:
            break
    for x in range(1, objetivos + 1):
        while True:
            distancia = int(input("Ingrese la distancia del objetivo abatido en metros \n"))
            if distancia <= 0:
                print("Distancia debe ser mayor a 0 metros")
            else:
                break
        if distancia < 50:
            bajas_cortas = bajas_cortas + 1
            puntaje_total = puntaje_total + 10
        elif distancia >= 50 and distancia <= 150:
            bajas_medias = bajas_medias + 1
            puntaje_total = puntaje_total + 25
        else:
            bajas_franco = bajas_franco + 1
            puntaje_total = puntaje_total + 50
    print(f"Desglose Total")
    print(f"Bajas corta distancia: {bajas_cortas}")
    print(f"Bajas media distancia: {bajas_medias}")
    print(f"Bajas francotirador: {bajas_franco}")
    print(f"Puntaje Total: {puntaje_total}")
except:
    print("Valor debe ser numérico")
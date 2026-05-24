# 🌃 Ejercicio 2: Netrunner en Cyberpunk 2077 (Ciclo for - Ingreso por Lote)
# Desarrolla un programa para tu cyberdeck que gestione el hackeo de una red de cámaras de seguridad en Night City. El sistema te pedirá cuántas cámaras quieres intentar vulnerar y evaluará el resultado de cada intento según el nivel de seguridad ICE de cada una.

# Requisitos y Funciones:

# Protección General: Todo en un try/except para blindarte contra errores de tipeo.

# Variables Iniciales: Crea contadores para camaras_hackeadas y camaras_bloqueadas. Crea un acumulador para la memoria_ram_usada.

# La Aduana Inicial:

# Pregunta: "¿Cuántas cámaras hay en el perímetro?"

# Validación: Debe ser mayor a 0.

# El Motor Principal (Ciclo for):

# Ejecuta el ciclo por la cantidad exacta de cámaras ingresadas.

# La Aduana Interna (Adentro del for):

# Por cada vuelta, pregunta: "Ingrese el nivel de seguridad ICE de la cámara (1 al 5): "

# Validación: El nivel debe estar entre 1 y 5 inclusive. Si el usuario ingresa 0, 6 o números negativos, muestra un error y vuelve a preguntar.

# Clasificación del Hackeo (Adentro del for):

# Si el nivel ICE es 1 o 2: El hackeo es rápido. Suma 1 a camaras_hackeadas y suma 2 a la memoria_ram_usada.

# Si el nivel ICE es 3 o 4: El hackeo es complejo. Suma 1 a camaras_hackeadas y suma 4 a la memoria_ram_usada.

# Si el nivel ICE es 5: El firewall rechaza la conexión. Suma 1 a camaras_bloqueadas (no gasta memoria RAM).

# El Reporte Final (Fuera del for):

# Al terminar, imprime:

# "--- Reporte del Cyberdeck ---"

# "Cámaras vulneradas con éxito: {camaras_hackeadas}"

# "Cámaras que bloquearon el acceso: {camaras_bloqueadas}"

# "Memoria RAM total consumida: {memoria_ram_usada} unidades"

import os
os.system("cls")

camaras_hackeadas =  0
memoria_usada = 0
camaras_bloqueadas = 0

try:
    while True:
        camaras = int(input("¿Cuántas cámaras hay en el perímetro? \n"))
        if camaras <= 0:
            print("Debe haber almenos una camara")
        else:
            break
    for x in range(1, camaras + 1):
        while True:
            seguridad = int(input("Ingrese el nivel de seguridad ICE de la cámara (1 al 5): \n"))
            if seguridad <= 0:
                print("Valor debe ser mayor a 0")
            elif seguridad > 5:
                print("Valor debe ser como máximo 5")
            else:
                break
        if seguridad == 1 or seguridad == 2:
            camaras_hackeadas = camaras_hackeadas + 1
            memoria_usada = memoria_usada + 2
        elif seguridad == 3  or seguridad == 4:
            camaras_hackeadas = camaras_hackeadas + 1
            memoria_usada = memoria_usada + 4
        else:
            camaras_bloqueadas = camaras_bloqueadas + 1
    print("--- Reporte del Cyberdeck ---")
    print(f"Cámaras vulneradas con éxito: {camaras_hackeadas}")
    print(f"Cámaras que bloquearon el acceso: {camaras_bloqueadas}")
    print(f"Memoria RAM total consumida: {memoria_usada} unidades")
except:
    print("Valor debe ser numérico")
# 🤖 Ejercicio 4: Auditoría en CyberLife (El Jefe Final)
# Desarrolla el sistema de control maestro para una planta de ensamblaje de androides. Este código te exigirá combinar el menú infinito while, la jaula de validaciones y un ciclo for matemático. El sistema arranca con un contador de androides_registrados = 0.

# Interfaz del Programa:

# Mensaje inicial: "Sistema CyberLife Iniciado. Iniciando auditoría."

# Menú principal:

# Registrar Androide

# Escáner de Memoria (Diagnóstico)

# Apagar Sistema

# Requisitos y Funcionalidades:

# Protección General: El menú principal debe estar protegido con un try/except.

# Opción 1 (Registrar): Pide el nivel de batería inicial del nuevo androide.

# Validación (while interno): El nivel de batería debe ser un número que esté entre 1 y 100 inclusive. (Pista: usa or en la condición del while). Si el usuario ingresa un número menor a 1 o mayor a 100, muestra: "Error: Nivel de batería inválido. Ingrese un valor entre 1 y 100."

# Camino Feliz: Suma 1 a la variable androides_registrados e imprime "Androide registrado con éxito."

# Opción 2 (Escáner de Memoria - Ciclo for):

# Pregunta al usuario: "¿Cuántos sectores de memoria desea analizar?" (Asume que ingresará un número positivo, no necesitas validarlo con while).

# Usa un ciclo for y range() para recorrer desde el sector 1 hasta la cantidad exacta que pidió el usuario.

# Por cada vuelta, el programa debe simular un aumento de inestabilidad calculando: inestabilidad = sector * 15 (donde 'sector' es el número de la vuelta actual).

# Inmediatamente, imprime: "Analizando sector {sector}... Inestabilidad al {inestabilidad}%".

# El Seguro de Divergencia: Después del print, revisa si la inestabilidad es mayor o igual a 60. Si es así, el programa imprime "¡Alerta! Divergencia detectada. Deteniendo escáner." y destruye el ciclo for con un break.

# Opción 3 (Apagar): Imprime "Apagando sistema. Total de androides ensamblados hoy: {androides_registrados}" y termina el ciclo principal del menú.

import os
os.system("cls")

androides_registrados = 0
programa = True

print("Sistema CyberLife Iniciado. Iniciando auditoría.")
while programa:
    print("1. Registrar Androide")
    print("2. Escáner de Memoria")
    print("3. Apagar Sistema")
    try:
        opcion = int(input("Ingrese opción: \n"))
        if opcion == 1:
            os.system("cls")
            registrar = 0
            while registrar <= 0 or registrar > 100:
                registrar = int(input("Que nivel de batería tiene el androide? \n %"))
                if registrar < 1 or registrar > 100:
                    print("Error: Nivel de batería inválido. Ingrese un valor entre 1 y 100.")
                else:
                    androides_registrados = androides_registrados + 1
                    print("Androide registrado con éxito")
                    break
        elif opcion == 2:
            os.system("cls")
            sector = int(input("¿Cuántos sectores de memoria desea analizar? \n"))
            for x in range(1, sector + 1):
                inestabilidad = x * 15
                print(f"Analizando sector {x}... Inestabilidad al {inestabilidad} %")
                if inestabilidad >= 60:
                    print("¡Alerta! Divergencia detectada. Deteniendo escáner.")
                    break
        elif opcion == 3:
            os.system("cls")
            print(f"Apagando sistema. Total de androides ensamblados hoy: {androides_registrados}")
            programa = False
    except:
        print("Valor debe ser numérico")

# Ejercicio 1 (40 puntos)
# Desarrolla un programa en Python que administre los registros de proyectos recién asigna-dos a la Empresa de Consultoría Estratégica. El programa debe validar correctamente todos los datos ingresados. Por ejemplo, si se solicita el presupuesto asignado o la duración del proyecto, el usuario solo debe poder ingresar números enteros positivos.

# Requisitos del Sistema

# 1. Clasificación y Funcionalidades Principales
# El sistema deberá:
# •	Clasificar a los proyectos según su presupuesto asignado.
# •	Contabilizar cuántos son Estratégicos y cuántos Tácticos.
# •	Mostrar un resumen de registro al finalizar.

# 2. Cantidad de Proyectos
# El programa debe pedir al usuario cuántos proyectos desea registrar.
# •	Este valor debe ser un número entero positivo.
# •	Si el usuario ingresa un valor inválido, se debe mostrar el siguiente mensaje hasta re-cibir una entrada correcta:
# "¡Cantidad inválida! Ingresa un entero positivo para continuar."

# 3. Registro por Proyecto
# Código Proyecto
# •	Debe tener al menos 6 caracteres.
# •	No debe incluir espacios.
# •	Ejemplos válidos: PROJ001EX, TASKMAX9, WORKGOLD4.

# Presupuesto Asignado
# •	El usuario debe ingresar el presupuesto del proyecto (entero positivo).
# •	Si se ingresa un valor incorrecto, se mostrará el mensaje:
# "¡Error presupuestario! Ingresa un número entero positivo para el presupuesto."

# 4. Clasificación del Proyecto
# Dependiendo del presupuesto ingresado:
# •	Si el presupuesto es mayor a 80000, el proyecto será Estratégico.
# •	Si el presupuesto es menor o igual a 80, el proyecto será Táctico.

# 5. Contadores Automáticos
# El programa debe llevar un conteo durante el registro:
# •	Número total de Proyectos Estratégicos.
# •	Número total de Proyectos Tácticos.

# 6. Salida Final
# Al finalizar el registro, el programa mostrará un resumen con el total de proyectos registra-dos.
# Por ejemplo:

# "¡La empresa cuenta con 4 Proyectos Estratégicos y 5 Proyectos Tácticos! ¡Ejecución auto-rizada!"

contador_estrategico = 0
contador_tactico = 0
cont_proyectos = 0
acceso = True

while acceso:
    try:
        proyectos = int(input("Ingrese la cantidad de proyectos a realizar: \n"))
        if proyectos <= 0:
            print("Valor debe ser mayor a 0")
        while cont_proyectos < proyectos:
            nom_proyecto = ""
            while len(nom_proyecto) <=6:
                nom_proyecto = input("Ingrese el nombre de su proyecto: \n")
                if len(nom_proyecto) <= 6:
                    print("Nombre del proyecto debe tener almenos 6 carácteres")
            presupuesto_proyecto = int(input("Ingrese presupuesto del proyecto: \n$ "))
            while presupuesto_proyecto <= 0:
                print("Presupuesto debe ser entero positivo")
            if presupuesto_proyecto > 80000:
                contador_estrategico = +1
                cont_proyectos = +1
            elif presupuesto_proyecto > 0 and presupuesto_proyecto < 80000:
                contador_tactico = +1
                cont_proyectos = +1
            else:
                print("Valor debe ser positivo entero")
            if cont_proyectos == proyectos:
                acceso = False
        print(f"La empresa cuenta con {contador_estrategico} Proyectos Estratégicos y {contador_tactico} Proyectos Tácticos. Ejecución Autorizada")
    except:
        print("Valor debe ser numérico")

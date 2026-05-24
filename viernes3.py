# 📦 El Último Desafío: Registro Continuo de Envíos
# Desarrolla un programa para una sucursal de correos que registre los paquetes de los clientes uno por uno. El sistema no tiene menú, arranca directamente pidiendo datos y se detiene solo cuando el trabajador indica que no hay más clientes.

# Requisitos y Funcionalidades:

# Preparación (Fuera del ciclo): Crea contadores separados para envíos ligeros, medianos y pesados. Crea también un acumulador para el dinero total recaudado en el día.

# Ciclo Principal: Un while que mantenga el registro de paquetes funcionando continuamente. Envuélvelo en un try/except para que no explote si ingresan letras en el peso.

# Ingreso y Validación del Paquete: * Pide el peso del paquete en kilos (puede ser un número entero).

# Validación: El peso debe ser mayor a 0. Si ingresan 0 o negativo, muestra "Error: El peso debe ser mayor a 0" y vuelve a preguntar.

# Clasificación y Cobro (La lógica central):

# Si el paquete pesa menos de 2 kilos: Es categoría "Ligero", suma 1 a su respectivo contador y suma $3.000 al dinero total.

# Si el paquete pesa entre 2 y 5 kilos (inclusive): Es categoría "Mediano", suma 1 a su contador y suma $5.000 al dinero total.

# Si el paquete pesa más de 5 kilos: Es categoría "Pesado", suma 1 a su contador y suma $8.000 al dinero total.

# Condición de Salida (Validación de texto): * Al terminar de procesar un paquete, el sistema debe preguntar: "¿Desea registrar otro envío? (si/no): "

# Validación: Crea una pequeña jaula aquí para obligar al usuario a escribir estrictamente "si" o "no".

# Si escribe "no", el ciclo principal se rompe. Si escribe "si", el programa vuelve arriba a pedir el peso del siguiente paquete.

# Cierre de Caja (Fuera del ciclo principal): Cuando el ciclo se rompe, imprime un reporte exacto como este:

# "--- Resumen del Día ---"

# "Total paquetes ligeros: {ligeros}"

# "Total paquetes medianos: {medianos}"

# "Total paquetes pesados: {pesados}"

# "Dinero total recaudado: ${total_recaudado}"

import os
os.system("cls")

envio_ligero = 0
envio_mediano = 0
envio_pesado = 0
dinero_total = 0

try:
    peso = 0
    while peso <=0:
        peso = int(input("Ingrese peso del paquete en kilogramos \n"))
        if peso <= 0:
            print("Error: El peso debe ser mayor a 0")
        if peso < 2:
            dinero_total = dinero_total + 3000
            envio_ligero = envio_ligero + 1
        elif peso >= 2 and peso <= 5:
            dinero_total = dinero_total + 5000
            envio_mediano = envio_mediano + 1
        else:
            dinero_total = dinero_total + 8000
            envio_pesado = envio_pesado + 1
        otro = input("¿Desea registrar otro envío? (si/no): ").lower()
        if otro == "si":
            peso = 0
        elif otro == "no":
            break
        else:
            print("Respuesta debe ser si o no")
    print("--- Resumen del Día ---")
    print(f"Total paquetes ligero: {envio_ligero}")
    print(f"Total paquetes medianos {envio_mediano}")
    print(f"Total paquetes pesados {envio_pesado}")
    print(f"Dinero total recaudado: ${dinero_total}")
except:
    print("Valor debe ser numérico")
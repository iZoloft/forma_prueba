# 📘 Ejercicio 1: El Compendio de Velvet Room (Ciclo for por lote)
# Desarrolla un sistema para que Igor registre nuevas Personas en el Compendio.

# Requisitos y Funcionalidades:

# Protección: Todo el programa debe estar envuelto en un bloque try/except general.

# Preparación: Crea contadores inicializados en cero para rango_bajo, rango_medio y rango_alto.

# Límite Inicial (Aduana 1): Pregunta al usuario cuántas Personas desea registrar en el compendio hoy.

# Validación del Límite: Debe ser un número mayor a 0. Atrapa al usuario en un while si ingresa cero o negativos.

# Motor Principal: Configura un ciclo for que dé la cantidad exacta de vueltas que el usuario definió en el paso anterior.

# Aduana de Texto (Adentro del for): Pide el nombre de la Persona.

# Validación de Texto: El nombre debe tener al menos 4 caracteres y NO tener espacios (ejemplo válido: JackFrost). Si falla, muestra un error y atrapa al usuario en un ciclo hasta que lo escriba bien.

# Aduana de Números (Adentro del for): Pide el nivel de la Persona.

# Validación de Números: El nivel debe ser un número mayor a 0. Si falla, atrápalo hasta que ingrese un nivel válido.

# Clasificación (Adentro del for, Camino Feliz): Si el nivel está entre 1 y 20 (inclusive), suma 1 a rango_bajo. Si el nivel está entre 21 y 50 (inclusive), suma 1 a rango_medio. Si el nivel es mayor a 50, suma 1 a rango_alto.

# Reporte Final (Fuera del for): Imprime un resumen con el total de Personas registradas en cada rango y el mensaje "Registro del Compendio finalizado".

rango_bajo = 0
rango_medio = 0
rango_alto = 0

try:
    registrar = 0
    while registrar <= 0:
        registrar = int(input("Cuantas personas desea registrar en el compendio hoy? \n"))
        if registrar <= 0:
            print("Debe registrar almenos una persona")
    for x in range(1, registrar + 1):
        nombre = ""
        while len(nombre) < 4 or " " in nombre:
            nombre = input("Ingrese nombre de persona a registrar \n")
            if len(nombre) < 4:
                print("Nombre de persona debe tener almenos 4 caracteres")
            if " " in nombre:
                print("Nombre de persona no debe contener espacios")
        nivel = 0
        while nivel <= 0:
            nivel = int(input("Ingrese nivel de persona \n"))
            if nivel <= 0:
                print("Nivel debe ser mayor a 0")
        if nivel > 0 and nivel <= 20:
            rango_bajo = rango_bajo + 1
        elif nivel > 20 and nivel <= 50:
            rango_medio = rango_medio + 1
        else:
            rango_alto = rango_alto + 1
    print(f"Registro del compendio finalizado")
    print(f"Personas rango bajo {rango_bajo}")
    print(f"Personas rango medio {rango_medio}")
    print(f"Personas rango alto {rango_alto}")
except:
    print("Valor debe ser numérico")
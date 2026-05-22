# Ejercicio 2: Inventario Ripperdoc en Night City (Tipo "Registro de Proyectos")
# Construya un programa en Python que registre el nuevo cargamento de implantes cibernéticos para una clínica. El sistema debe validar estrictamente cada ingreso para evitar que la base de datos se corrompa.

# Requisitos del Sistema:

# Cantidad de Ingresos: Pregunta cuántos implantes se van a registrar.

# Debe ser mayor a 0. Si no, muestra: "¡Ingreso denegado! La cantidad debe ser un número positivo." (El programa debe insistir hasta que se ingrese bien).

# Registro Individual: Por cada implante, se debe pedir:

# Código de serie: Debe tener al menos 5 caracteres y no incluir espacios. Si falla, muestra: "Error en el escáner: El código debe tener 5 caracteres mínimo y no usar espacios."

# Costo en Eurodólares (ED): Debe ser un entero positivo mayor a 0. Si falla, muestra: "Error de sistema: El costo no puede ser negativo ni cero."

# Clasificación Automática:

# Si el costo es mayor a 50000, el implante se clasifica como Cromo Legendario.

# Si el costo es menor o igual a 50000, se clasifica como Cromo Estándar.

# Resumen Final: El sistema debe contar cuántos implantes de cada tipo se registraron. Al terminar el ciclo, debe imprimir obligatoriamente:

# "¡Base de datos actualizada! Se ingresaron {X} piezas de Cromo Legendario y {Y} de Cromo Estándar."

# ¡Tómate tu tiempo con las tabulaciones de los while y asegúrate de aplicar todo lo que vimos sobre el "Camino Feliz" (usar los else para ejecutar las matemáticas)! Cuando tengas uno listo, mándamelo y lo revisamos con lupa. 🚀💻

contador_implantes = 0
cromo_estandar = 0
cromo_legendario = 0

while True:
    try:
        implantes = 0
        while implantes <= 0:
            implantes = int(input("Ingrese la cantidad de implantes a registrar \n"))
            if implantes <= 0:
                print("La cantidad debe ser un número positivo")
        while contador_implantes < implantes:
            codigo_implante = ""
            while len(codigo_implante) < 5 or " " in codigo_implante:
                codigo_implante = input("Ingrese código del implante: \n")
                if len(codigo_implante) < 5 or " " in codigo_implante:
                    print("El código debe tener almenos 5 caracteres y no tener espacios")
            costo = 0
            while costo <= 0:
                costo = int(input("Ingrese el costo del implante: \n$ "))
                if costo <= 0:
                    print("Costo debe ser mayor a 0 Eurodolares")
            if costo <= 50000:
                cromo_estandar = cromo_estandar + 1
                contador_implantes = contador_implantes + 1
            else:
                cromo_legendario = cromo_legendario + 1
                contador_implantes = contador_implantes + 1
        print(f"¡Base de datos actualizada! Se ingresaron {cromo_legendario} piezas de Cromo Legendario y {cromo_estandar} de Cromo Estándar.")
        break
    except:
        print("Valor debe ser numérico")
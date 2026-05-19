# Ejercicio 2 (60 puntos)
# Construya un programa en Python que permita gestionar un sistema simple de estaciones de trabajo para un centro de cómputo por medio de un menú de opciones.
# El programa debe comenzar con 25 estaciones disponibles previamente cargadas.

# Interfaz del Programa
# Bienvenida
# ¡Bienvenido al sistema de gestión de estaciones del Centro de Cómputo!

# Menú Principal
# El programa debe mostrar el siguiente menú:

# === MENÚ PRINCIPAL ===
# 1.	Estaciones disponibles
# 2.	Asignar estación
# 3.	Liberar estación
# 4.	Historial de uso
# 5.	Salir

# Funcionalidades del Sistema
# 1. Estaciones Disponibles
# •	Mostrar la cantidad de estaciones disponibles en el centro.
# •	Este valor debe actualizarse conforme se realicen asignaciones o liberaciones.

# 2. Asignar Estación
# •	Permite asignar estaciones a usuarios.
# •	Se debe solicitar la cantidad de estaciones a asignar.
# •	Este número debe cumplir las siguientes validaciones:
# o	No puede ser menor o igual a 0.
# o	No debe superar la cantidad de estaciones disponibles.

# 3. Liberar Estación
# •	Permite liberar estaciones de usuarios.
# •	Se debe solicitar la cantidad de estaciones a liberar, validando que:
# •	Sea mayor a 0.
# •	No supere la capacidad máxima (25 estaciones).
# •	Esta acción incrementará el número de estaciones disponibles.

# 4. Historial de Uso
# •	Mostrar la cantidad de asignaciones realizadas durante la sesión.
# •	Las liberaciones disminuyen el historial.
# •	 Las asignaciones aumentan el historial.

# 5. Salir del Sistema
# •	Al seleccionar esta opción, el programa debe finalizar su ejecución mostrando el mensaje:
# "Gracias por utilizar nuestro software, hasta la próxima."

# Si el usuario desea asignar estaciones, se debe validar que haya suficiente capacidad dispo-nible. En caso de que no haya suficientes, debe informarse al usuario. La opción 4 debe mostrar el total de asignaciones realizadas durante la sesión (contador separado). El progra-ma debe repetirse hasta que el usuario elija salir.


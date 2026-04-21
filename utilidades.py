import time
from inventario import cargar_inventario, inventario

def Inicio_Programa():
    print("Bienvenido a la aplicación de inventarios.")
    print("1. Crear un archivo de inventario nuevo")
    print("2. Abrir un archivo de inventario existente")
    print("3. Salir")
    opcion = input()

    if opcion == "1":
        nombre = input("Ingrese el nombre del archivo (sin extensión): ") + ".json"
        cargar_inventario(nombre)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del archivo existente (sin extensión): ") + ".json"
        cargar_inventario(nombre)

    elif opcion == "3":
        print("Gracias por utilizar la aplicación.")
        time.sleep(2)
        exit()
    else:
        print("Opción no válida.")
        Inicio_Programa()

def Seleccionar_Decision(callback):
    print("¿Desea realizar otra acción?\n1. Sí\n2. No")
    eleccion = input()
    if eleccion == "1":
        callback()
    elif eleccion == "2":
        print("Gracias por utilizar la aplicación de inventarios")
        time.sleep(2)
        exit()
    else:
        print("Opción no válida.")
        Seleccionar_Decision(callback)

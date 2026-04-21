#Randall José Acosta Navarro
#Summy Vanessa Reyes Conejo

import json
import os
from validacion import validar_numero 

inventario = []
archivo_actual = None

def buscar_producto_por_codigo(codigo):
    codigo = str(codigo).strip()  
    for p in inventario:
        if p['codigo'].strip() == codigo:
            return p
    return None

def cargar_inventario(nombre_archivo):
    global inventario, archivo_actual
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as f:
            inventario = json.load(f)
        print(f"Inventario cargado desde {nombre_archivo}")
    else:
        inventario = []
        print(f"Archivo no existe. Se creará uno nuevo: {nombre_archivo}")
    archivo_actual = nombre_archivo

def guardar_inventario():
    if archivo_actual:
        with open(archivo_actual, 'w') as f:
            json.dump(inventario, f, indent=4)
        print("Cambios guardados en el archivo.")
    else:
        print("Error: No hay archivo de inventario cargado.")

def ingresar_producto(codigo):
    for producto in inventario:
        if producto['codigo'] == codigo:
            print(f"El producto ya existe: {producto['nombre']} (Cantidad actual: {producto['cantidad']})")
            cantidad = validar_numero(input("Ingrese la cantidad a agregar: "))
            producto['cantidad'] += cantidad
            guardar_inventario()
            print("Cantidad agregada correctamente.")
            return
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = validar_numero(input("Ingrese la cantidad de producto: "))
    minimo = validar_numero(input("Ingrese el mínimo de producto: "))
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "cantidad": cantidad,
        "minimo": minimo
    }
    inventario.append(producto)
    guardar_inventario()
    print("Producto agregado correctamente.")

def substraer_producto(producto, cantidad):
    while cantidad > producto['cantidad']:
        print("Error: No hay suficiente cantidad en inventario.")
        cantidad = validar_numero(input(f"Ingrese una cantidad válida para {producto['nombre']} (Disponible: {producto['cantidad']}): "))
    producto['cantidad'] -= cantidad
    guardar_inventario()
    print("Cantidad restada correctamente.")

def consultar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Estado del inventario:")
        for p in inventario:
            print(f"Código: {p['codigo']}, Producto: {p['nombre']}, Cantidad: {p['cantidad']}, Mínimo: {p['minimo']}")

def modificar_producto():
    codigo = input("Ingrese el código del producto a modificar: ")
    producto = next((p for p in inventario if p['codigo'] == codigo), None)

    if producto:
        print(f"Producto encontrado: {producto['nombre']} - Cantidad: {producto['cantidad']} - Mínimo: {producto['minimo']}")
        print("¿Qué desea modificar?\n1. Nombre\n2. Cantidad\n3. Mínimo")
        opcion = input()

        if opcion == "1":
            producto['nombre'] = input("Nuevo nombre: ")
        elif opcion == "2":
            producto['cantidad'] = validar_numero(input("Nueva cantidad: "))
        elif opcion == "3":
            producto['minimo'] = validar_numero(input("Nuevo mínimo: "))
        else:
            print("Opción no válida.")
            return

        guardar_inventario()
        print("Producto modificado con éxito!")
    else:
        print("Producto no encontrado.")

#Randall José Acosta Navarro
#Summy Vanessa Reyes Conejo
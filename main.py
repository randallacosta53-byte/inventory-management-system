#Randall José Acosta Navarro
#Summy Vanessa Reyes Conejo

from inventario import ingresar_producto, substraer_producto, consultar_inventario, modificar_producto, buscar_producto_por_codigo
from validacion import validar_numero
from utilidades import Inicio_Programa, Seleccionar_Decision


import time

def Ingresar_Una_Opcion():
    print("Ingrese una opción: ")
    print(f"\n1. Ingresar un producto")
    print(f"2. Substraer de un producto")
    print(f"3. Consultar estado de inventario")
    print(f"4. Modificar un producto")
    print(f"5. Salir")
    opcion = input()

    if opcion == "1":
        codigo = input(f"Ingrese el código del producto (único): ")
        ingresar_producto(codigo)
        print(f"Cambios guardados con éxito!")
        time.sleep(2)
        Seleccionar_Decision(Ingresar_Una_Opcion)
        
    elif opcion == "2":
        while True:
            codigo = input("Ingrese el código del producto: ").strip()
            producto_encontrado = buscar_producto_por_codigo(codigo)

            if not producto_encontrado:
                print("Producto no encontrado en el inventario. Intente con otro código.")
                continue 

            cantidad = validar_numero(input(f"Ingrese la cantidad a substraer de {producto_encontrado['nombre']} (Disponible: {producto_encontrado['cantidad']}): "))
            substraer_producto(producto_encontrado, cantidad)
            print("Cambios guardados con éxito!")
            time.sleep(2)
            Seleccionar_Decision(Ingresar_Una_Opcion)
            break

    elif opcion == "3":
        consultar_inventario()
        time.sleep(2)
        Seleccionar_Decision(Ingresar_Una_Opcion)

    elif opcion == "4":
        modificar_producto()
        time.sleep(2)
        Seleccionar_Decision(Ingresar_Una_Opcion)

    elif opcion == "5":
        print(f"Gracias por utilizar la aplicación de inventarios")
        time.sleep(3)
        exit()

    else:
        print(f"Opción no válida. Intente de nuevo.")
        Ingresar_Una_Opcion()

if __name__ == "__main__":
    Inicio_Programa()
    Ingresar_Una_Opcion()

#Randall José Acosta Navarro
#Summy Vanessa Reyes Conejo
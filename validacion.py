def validar_numero(entrada):
    while not entrada.isdigit():
        print("Por favor, ingrese un número válido.")
        entrada = input()
    return int(entrada)

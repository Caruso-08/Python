def verificar_numero():
    numero = float(input("Digite um número: "))

    if numero == 0:
        print("É ZERO")
    elif numero > 0:
        print(f"O número {numero} é positivo.")
    else:
        print(f"O número {numero} é negativo.")

verificar_numero()

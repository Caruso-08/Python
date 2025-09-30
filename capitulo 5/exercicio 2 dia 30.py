def quadrado_positivo():
    numero = float(input("Digite um número: "))

    if numero >= 0:
        quadrado = numero ** 2
        print(f"O quadrado do número é: {quadrado}")
    else:
        print("Número negativo não é permitido!")

quadrado_positivo()

def verificar_divisibilidade():
    # Lê um número inteiro
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0 and numero % 3 == 0:
        print(f"O número {numero} é divisível por 2 e 3.")
    elif numero % 2 == 0:
        print(f"O número {numero} é divisível apenas por 2.")
    elif numero % 3 == 0:
        print(f"O número {numero} é divisível apenas por 3.")
    else:
        print(f"O número {numero} não é divisível nem por 2 nem por 3.")


verificar_divisibilidade()

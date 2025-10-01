def calcular_media_pares():

    numeros = []
    for i in range(4):
        num = int(input(f"Digite o {i + 1}º número: "))
        numeros.append(num)

    numeros_pares = [num for num in numeros if num % 2 == 0]
    if len(numeros_pares) > 0:

        media = sum(numeros_pares) / len(numeros_pares)
        print(f"A média dos números pares é: {media}")
    else:
        print("Não há números pares.")

calcular_media_pares()

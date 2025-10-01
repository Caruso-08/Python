def contar_pessoas_21_anos():
    contador_21 = 0

    for i in range(5):
        idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
        if idade == 21:
            contador_21 += 1

    return contador_21

resultado = contar_pessoas_21_anos()
print(f"Existem {resultado} pessoa(s) com 21 anos.")

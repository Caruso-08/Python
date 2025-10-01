# Função para verificar se o número é divisível por 5 ou 3
def verificar_divisibilidade_5_ou_3(numero):
    if numero % 5 == 0 or numero % 3 == 0:
        return f"O número {numero} é divisível por 5 ou por 3."
    else:
        return f"O número {numero} NÃO é divisível por 5 ou por 3."

numero = int(input("Digite um número inteiro: "))

resultado = verificar_divisibilidade_5_ou_3(numero)
print(resultado)

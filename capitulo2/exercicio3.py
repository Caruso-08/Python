def soma(numero1, numero2):
    return numero1 + numero2
def subtracao(numero1, numero2):
        return numero1 - numero2

def multiplicacao(numero1, numero2):
        return numero1 * numero1
numero1 = int(input("Digite um numero inteiro!"))
numero2 = int(input("Digite um numero inteiro!"))

def divisao(numero1, numero2):
    return numero1 / numero2


ResultadoSoma = soma(numero1, numero2)
ResultadoSubtracao =  subtracao(numero1, numero2) #chamada da funcao
ResultadoMultiplicacao = multiplicacao(numero1, numero2)
ResultadoDivisao = divisao(numero1, numero2)
print("O resultado da funcao soma", ResultadoSoma)
print("O resultado da funcao subtracao", ResultadoSubtracao)
print("O resultado da funcao multiplicacao", ResultadoMultiplicacao)
print("O resultado da funcao divisao", ResultadoDivisao)



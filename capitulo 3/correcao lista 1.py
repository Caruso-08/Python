def adicao(numero, numero2):
    return numero + numero2

def subtracao(numero, numero2):
    return numero - numero2

def multiplicacao(numero, numero2):
    return numero * numero2

def divisao(numero, numero2):
    return numero / numero2

numero = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))

resultadoAdicao = adicao(numero, numero2)
resultadoSubtracao = subtracao(numero, numero2)
resultadoMultiplicacao = multiplicacao(numero, numero2)
resultadoDivisao = divisao(numero, numero2)

print("Adicao: ", resultadoAdicao)
print("Subtracao: ", resultadoSubtracao)
print("Multiplicacao: ", resultadoMultiplicacao)
print("Divisao: ", resultadoDivisao)
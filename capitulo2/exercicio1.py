numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))


soma = numero1 + numero2
produto = numero1 * numero2
diferenca = numero1 - numero2


if numero2 != 0:
    quociente = numero1 / numero2
else:
    quociente = "Indefinido (divisão por zero)"


print("Resultados:")
print("Soma: {soma}")
print("Produto: {produto}")
print("Diferença: {diferenca}")
print("Quociente: {quociente}")

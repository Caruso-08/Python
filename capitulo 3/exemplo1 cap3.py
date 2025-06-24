def right_justify(palavra, TamanhoPalavra):
    espaco = " " * (70 - TamanhoPalavra)
    return espaco + palavra
palavra = str(input("Digite uma palavra"))
TamanhoPalavra = len(palavra)
justificado = right_justify(palavra, TamanhoPalavra)

print(justificado)
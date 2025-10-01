def classificar_categoria(idade):
    if 5 <= idade <= 7:
        return "Infantil A (5 a 7 anos)"
    elif 8 <= idade <= 10:
        return "Infantil B (8 a 10 anos)"
    elif 11 <= idade <= 13:
        return "Juvenil A (11 a 13 anos)"
    elif 14 <= idade <= 17:
        return "Juvenil B (14 a 17 anos)"
    elif idade >= 18:
        return "Sênior (18 anos ou mais)"
    else:
        return "Idade inválida para classificação"
idade = int(input("Digite a idade do jogador: "))

categoria = classificar_categoria(idade)
print(f"A categoria do jogador é: {categoria}")

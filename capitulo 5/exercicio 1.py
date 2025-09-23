def apresentacao(nome, nomeMae, nomePai):
    print(f"Nome: {nome}")
    print(f"Nome da Mae: {nomeMae}")
    print(f"Nome do Pai: {nomePai}")

nome = str(input("Digite seu nome completo"))
nomeMae = str(input("Digite o nome completo da sua mãe"))
nomePai = str(input("Digite o nome completo do seu pai"))

apresentacao(nome, nomeMae, nomePai)
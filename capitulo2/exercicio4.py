populacao_atual = 8231613070  
taxa_crescimento = 0.0085     

print("Estimativa da População Mundial:")
for ano in range(1, 6):
    populacao_futura = populacao_atual * ((1 + taxa_crescimento) ** ano)
    print(f"Ano {ano}: {int(populacao_futura):,} pessoas")

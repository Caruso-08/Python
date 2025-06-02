# Dados iniciais
populacao_atual = 8231613070  # População em 2025
taxa_crescimento = 0.0085     # 0,85% ao ano

# Cálculo e exibição das projeções para os próximos 5 anos
print("Estimativa da População Mundial:")
for ano in range(1, 6):
    populacao_futura = populacao_atual * ((1 + taxa_crescimento) ** ano)
    print(f"Ano {ano}: {int(populacao_futura):,} pessoas")

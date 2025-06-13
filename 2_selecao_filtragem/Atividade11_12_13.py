import pandas as pda
url_frutas = "produtos_mercado.csv"
df_frutas = pda.read_csv(url_frutas)

# 11  Quais Frutas Têm Um Preco_Kg Superior A R$ 10,00?

df_frutas['Preco_Kg'] = pda.to_numeric(df_frutas['Preco_Kg'], errors='coerce')


produtos_caros = df_frutas[df_frutas["Preco_Kg"] >= 10]
print("Produtos Com Valor Acima De R$10.00 O Kg:")
print("")
print(produtos_caros)
print("")

# 12  Quais Produtos Foram Repostos No Dia '2024-06-01'?

produtos_repostos = df_frutas[df_frutas["Data_Ultima_Reposicao"] == "2024-06-01"]
print("Produtos Repostos No Dia 01-06-2024:")
print("")
print(produtos_repostos)
print("")

# 13  Quais Produtos São Fornecidos Pela 'Fazenda Sol Nascente' E São Da Categoria 'Fruta'?

Frutas = df_frutas[df_frutas['Categoria'] == 'Fruta']
print("Lista Completa Das Frutas:")
print("")
print(Frutas)
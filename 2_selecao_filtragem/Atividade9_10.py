import pandas as pda
url_frutas = "produtos_mercado.csv"
df_frutas = pda.read_csv(url_frutas)

# 9 Exiba Os Dados Do Produto Com ID_Produto Igual A 110 (Limão Tahiti)
ID_Produto = df_frutas.iloc[109]
print("Produto Solicitado:")
print(ID_Produto)
print("")

# 10 Quais São Os Produtos Da Categoria 'Verdura'?

Verduras = df_frutas[df_frutas['Categoria'] == 'Verdura']

print("Lista Completa Das Verduras Apenas:")
print("")
print(Verduras)
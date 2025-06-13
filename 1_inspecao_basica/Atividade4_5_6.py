import pandas as pda
url_frutas = "produtos_mercado.csv"
df_frutas = pda.read_csv(url_frutas)

# 4 Exiba Os 7 Primeiros Itens Do Dataframe.
print("Primeiras 7 Linhas Do Mercado:")
print("")
print(df_frutas.head(7))
print("")
# 5 Exiba Os 3 Ultimos Itens Do Dataframe.
print("Ultimas 3 Linhas Do Mercado:")
print("")
print(df_frutas.tail(3))
print("")
# 6 Obtenha Um Resumo Estátistico Das Colunas Numéricas (Como Preço E Estoque).

print("Resumo Descritivo Do Mercado:")
print("")
print(df_frutas.describe())
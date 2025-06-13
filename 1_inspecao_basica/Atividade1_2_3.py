import pandas as pda
url_frutas = "produtos_mercado.csv"
df_frutas = pda.read_csv(url_frutas)
# 1 E 2 | Quantas Linhas E Colunas Tem O Nosso DataFrame? | Quais São Os Nomes De Todas As Colunas?
print(f"O DataFrame Do Mercado Tem {df_frutas.shape[0]} Linhas E {df_frutas.shape[1]} Colunas")
print("")

# 3 Quais São Os Tipos De Dados De Cada Coluna? A Coluna 'Data_Ultima_Reposicao' Está No Formato Correto De Data? 

print("Informações Precisas Sobre O DataFrame Do Mercado:")
print("")
print(df_frutas.info())
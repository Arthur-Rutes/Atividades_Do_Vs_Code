import pandas as pda
url_frutas = "produtos_mercado.csv"
df_frutas = pda.read_csv(url_frutas)
# 7 E 8 | Selecione E Exiba Apenas A Coluna 'Produto'. | Selecione E Exiba As Colunas 'Produto', 'Categoria' E 'Preco_Kg'.

produto_selecionado = df_frutas[["Produto"]]
print("Produtos Disponiveis:")
print("")
print(produto_selecionado)
print("")

descricao_detalhada = df_frutas [["Produto", "Categoria", "Preco_Kg"]]
print("Descrição Mais Detalhada:")
print("")
print(descricao_detalhada)
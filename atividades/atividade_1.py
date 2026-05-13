import pandas as pd 

print(" Atividade 1: DataFrame de Frutas ")
dados_frutas = {
    "Fruta": ["Maçã", "Banana", "Morango", "Uva", "Abacaxi"],
    "Quantidade": [12, 15, 8, 20, 5],
    "Preco": [5.50, 3.20, 10.00, 7.50, 8.00]
}

df_frutas = pd.DataFrame(dados_frutas)
print(df_frutas)
print("\n")
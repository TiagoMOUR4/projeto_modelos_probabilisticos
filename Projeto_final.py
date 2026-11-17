import pandas as pd

# Lendo o arquivo CSV e transformando em um DataFrame
df = pd.read_csv('Dataset.csv', encoding='utf-8')

# Exibindo as primeiras linhas
print(df.head())


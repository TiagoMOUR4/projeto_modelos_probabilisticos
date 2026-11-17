#imports
import pandas as pd

data = pd.read_csv("../arquivos/Dataset.csv")

sumario = data.describe()
print(data.head())
print('\n')
print(sumario)
print('\n')

# Armazenando os dados completos, o número de valores distintos e as categorias/tipos de dado

variaveis = {}

for coluna in data.columns:
    variaveis[coluna] = {
        "dados": data[coluna],
        "num": len(set(data[coluna])),
        "cat": set(data[coluna])
    }


features = ['Nozzle', 'Orifice', 'Airspeed', 'Pressure', 'Orientation', 'Rep', 'Run']
targets = ['DV10', 'DV50', 'DV90', 'Less100', 'Less200']

for i in features:
    print(f"Há {variaveis[i]['num']} tipos de {i}")
 
print('\n')
print('os tipos de bico são:', variaveis['Nozzle']['cat'])

#separação por tipos de bico








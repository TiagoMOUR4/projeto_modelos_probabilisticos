
#importando dados
import pandas as pd
import pyvis
import pgmpy
import networkx as nx
from scripts.grafo1 import grafo1

G1 = grafo1()

# Lendo o arquivo CSV e transformando em um DataFrame
df = pd.read_csv('arquivos/Dataset.csv', encoding='utf-8')

# Exibindo as primeiras linhas e estatistica

print(df.head())
sumario = df.describe()
print(sumario)


# Executar o primeiro grafo
G1 = grafo1()

# Estatísticas estruturais
print("=== GRAFO 1 ===")
print("Nós:", G1.number_of_nodes())
print("Arestas:", G1.number_of_edges())
print("É um DAG?", nx.is_directed_acyclic_graph(G1))





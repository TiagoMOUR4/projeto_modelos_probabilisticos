
import networkx as nx
from graphviz import Digraph
from pathlib import Path


def grafo1():
    entradas = ["Orifice", "Airspeed", "Pressure", "Orientation"]
    saidas = ["DV10", "DV50", "DV90", "Less100", "Less200"]

    # Construção automática do grafo
    G = nx.DiGraph(
        (entrada, saida)
        for entrada in entradas
        for saida in saidas
    )

    # Visualização automática
    dot = Digraph(format="svg")
    dot.edges(G.edges())

    pasta = Path(__file__).resolve().parent.parent / "arquivos"
    dot.render(filename="grafo1", directory=pasta, cleanup=True)

    return G

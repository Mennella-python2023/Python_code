import networkx as nx
import matplotlib.pyplot as plt

def crea_grafo_diretto(nodi, archi):
    """
    Crea un grafo diretto con i nodi e archi specificati.
    
    :param nodi: lista di nodi (es. ['A', 'B', 'C'])
    :param archi: lista di tuple (origine, destinazione)
    :return: oggetto DiGraph
    """
    if not isinstance(nodi, (list, tuple)) or not isinstance(archi, (list, tuple)):
        raise TypeError("Nodi e archi devono essere liste o tuple.")

    G = nx.DiGraph()
    G.add_nodes_from(nodi)
    G.add_edges_from(archi)
    return G

def disegna_grafo(G):
    """
    Disegna un grafo diretto con frecce.
    """
    if not isinstance(G, nx.DiGraph):
        raise TypeError("L'oggetto deve essere un DiGraph di networkx.")

    pos = nx.spring_layout(G)  # Layout automatico
    plt.figure(figsize=(6, 4))
    nx.draw(
        G, pos, with_labels=True, node_color="lightblue",
        node_size=1500, font_size=12, font_weight="bold",
        arrows=True, arrowsize=20
    )
    plt.title("Grafo Diretto", fontsize=14)
    plt.show()

if __name__ == "__main__":
    # Esempio di utilizzo
    nodi = ["A", "B", "C", "D"]
    archi = [("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")]

    try:
        grafo = crea_grafo_diretto(nodi, archi)
        disegna_grafo(grafo)
    except Exception as e:
        print(f"Errore: {e}")

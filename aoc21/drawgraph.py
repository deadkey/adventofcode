import networkx as nx
import matplotlib.pyplot as plt

def draw(g, nodes):
    G=nx.DiGraph()
    G.add_nodes_from(nodes)
    for node in nodes:
        ns = g[node]
        for nb in ns:
            G.add_edge(node, nb)
    print('Nodes of graph', G.nodes())

    print('Efges of graph', G.edges())
    nx.draw_networkx(G,with_labels=True, node_color = 'red')
    plt.show()
            
def main():
    
    G=nx.path_graph(4)

    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())
    nx.draw(G)
    plt.savefig("path_graph1.png")
    plt.show()

if __name__ == '__main__':
    main()
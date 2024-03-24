"""
A project implementing PageRank and Betweenness Centrality measures for social network data.
"""

import networkx as nx
from  pagerank_centrality import *


def read_graph_data(edge_list):
    """
    Reads and builds a graph from data.

    Parameters:
        file: Path to plain text file where each line contains two integers separated by a single blank space character.
            Each line will represent an undirected edge from the node represented by the first integer to the node
            represented by the second integer.

    Returns:
        graph: NetworkX Graph object with nodes and edges from the edge list.
    """

    graph = nx.Graph()
    file = open(edge_list, 'r')

    # Loop through file and add edges into graph object
    while True:
        line = file.readline()

        if not line:
            break

        start_node, end_node = line.split()
        graph.add_edge(int(start_node), int(end_node))

    return graph


if __name__ == "__main__":
    graph = read_graph_data('data.txt')

    pagerank_vector = find_pagerank_centralities(graph)
    print(find_top_pagerank_nodes(pagerank_vector, 10))
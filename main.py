"""
A project implementing PageRank and Betweenness Centrality measures for social network data.
"""

import networkx as nx
from pagerank_centrality import *
from betweenness_centrality import find_betweenness_centrality, find_top_betweenness_nodes


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


def top_results_file(top_betweenness, top_pagerank, file_name='top_results.txt'):
    """
    Writes the top pagerank nodes and top betweenness centrality nodes to a file such that
    each line is separated by a space. The first line in the file will list the top nodes found by betweenness
    centrality and the second line in the file will be the top nodes found using ppagerank.

    Parameters:
        top_betweenness: List of top nodes found by betweenness centrality.
        top_pagerank: List of top nodes found by pagerank centrality.
        file_name: Name of results file.
    """
    file = open(file_name, "w")

    for i in range(len(top_betweenness)):
        file.write(str(top_betweenness[i]))
        if i != len(top_betweenness) - 1:
            file.write(" ")

    file.write("\n")

    for i in range(len(top_pagerank)):
        file.write(str(top_pagerank[i]))
        if i != len(top_pagerank) - 1:
            file.write(" ")

    file.close()


if __name__ == "__main__":
    graph = read_graph_data('data.txt')

    pagerank_vector = find_pagerank_centralities(graph)
    top_pagerank = find_top_pagerank_nodes(pagerank_vector, 10)

    betweenness_centralities = find_betweenness_centrality(graph)
    top_betweenness = find_top_betweenness_nodes(betweenness_centralities, 10)

    top_results_file(top_betweenness, top_pagerank)
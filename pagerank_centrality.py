"""
Code for calculating PageRank Centrality for social network nodes.
"""

from networkx import adjacency_matrix
import numpy as np


def find_pagerank_centralities(graph):
    """
    Calculates the PageRank centrality for all nodes in a graph.

    Parameters:
        graph: NetworkX graph object for which the PageRank centralities will be calculated for.

    Returns:
        pagerank_vector: Vector containing the corresponding PageRank centralities for each node in the graph.
    """
    alpha = 0.85
    beta = 0.15

    # Build adjacency matrix
    A = adjacency_matrix(graph).toarray()

    # Build inverse degree matrix
    D_inv = np.diag([1 / len(graph[i]) for i in graph.nodes])
    
    prev_pagerank_vector = np.zeros(len(graph.nodes()))
    pagerank_vector = np.ones(len(graph.nodes())) / len(graph.nodes())

    while np.sum(np.abs(prev_pagerank_vector - pagerank_vector)) > 0.0001:
        prev_pagerank_vector = pagerank_vector.copy()

        # Perform PageRank calculation
        pagerank_vector = np.matmul(np.matmul(alpha * A.T, D_inv), pagerank_vector) + beta * np.ones(len(graph.nodes()))
        pagerank_vector = pagerank_vector / np.sum(np.abs(pagerank_vector))

    return pagerank_vector


def find_top_pagerank_nodes(pagerank_centralities, num):
    """
    Finds the nodes with the greatest pagerank centralities.

    Parameters:
        pagerank_centralities: Vector containing the corresponding PageRank centralities for each node in the graph.
        num: Number of top nodes to find.

    Returns:
        Indices of nodes with the greatest PageRank centralities.
    """
    return np.argsort(pagerank_centralities)[-num:]
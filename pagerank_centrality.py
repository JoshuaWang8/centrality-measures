"""
Code for calculating PageRank Centrality for social network nodes.
"""

import numpy as np


def find_pagerank(graph):
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
    n = len(graph.nodes())
    A = np.zeros((n, n))

    # Populate the adjacency matrix
    for i in range(n):
        neighbor_list = list(graph.neighbors(i))
        for j in range(n):
            if j in neighbor_list:
                A[i][j] = 1

    # Build inverse degree matrix
    D_inv = np.linalg.inv(np.diag(A.sum(axis=1)))
    
    prev_pagerank_vector = np.zeros(n)
    pagerank_vector = np.ones(n) / n

    while np.sum(np.abs(prev_pagerank_vector - pagerank_vector)) > 0.001:
        prev_pagerank_vector = pagerank_vector

        # Perform PageRank calculation
        pagerank_vector = np.matmul(np.matmul(alpha * A.T, D_inv), pagerank_vector) + beta * np.ones(n)
        pagerank_vector = pagerank_vector / np.sum(np.abs(pagerank_vector))

    return pagerank_vector


def top_pagerank(pagerank_centralities, num):
    """
    Finds the nodes with the greatest pagerank centralities.

    Parameters:
        pagerank_centralities: Vector containing the corresponding PageRank centralities for each node in the graph.
        num: Number of top nodes to find.

    Returns:
        Indices of nodes with the greatest PageRank centralities.
    """
    return np.argsort(pagerank_centralities)[-num:]
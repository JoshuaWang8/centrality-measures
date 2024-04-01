"""
Code for calculating Betweenness Centrality for social network nodes.
"""


def breadth_first_search(graph, start):
    """
    Performs breadth first search given a graph and the starting node and finds the number of shortest paths and predecessors for each .

    Parameters:
        graph: NetworkX graph object for which search will be conducted on.
        start: Starting node.

    Returns:
        paths: Number of available shortest paths from start node.
        predecessors: Predecessors of each node that will be passed through during the shortest path.
    """
    paths = {node: 0 for node in graph.nodes()}
    paths[start] = 1
    predecessors = {node: [] for node in graph.nodes()}
    distances = {node: None for node in graph.nodes()}
    distances[start] = 0

    queue = [start]

    while len(queue) > 0:
        v = queue.pop(0)

        for w in graph.neighbors(v):
            if distances[w] == None:
                queue.append(w)
                distances[w] = distances[v] + 1
            
            if distances[w] == distances[v] + 1:
                predecessors[w].append(v)
                paths[w] += paths[v]

    return paths, predecessors


def find_betweenness_centrality(graph):
    """
    Calculates the node betweenness centrality for all nodes in a graph.

    Parameters:
        graph: NetworkX graph object for which betweenness centrality will be calculated for.

    Returns:
        centralities: Betweenness centrality measures for all nodes.
    """

    centralities = {node: 0 for node in graph.nodes()}

    for node in graph.nodes():
        stack = []
        sigma, pred = breadth_first_search(graph, node)
        delta = {node: 0 for node in graph.nodes()}
        stack.extend(graph.nodes())

        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != node:
                centralities[w] += delta[w]
    
    return centralities
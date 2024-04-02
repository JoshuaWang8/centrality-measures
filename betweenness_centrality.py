"""
Code for calculating Betweenness Centrality for social network nodes.
"""


def bfs(graph, start):
    """
    Performs breadth first search given a graph and the starting node and finds the number of shortest paths and predecessors for each .

    Parameters:
        graph: NetworkX graph object for which search will be conducted on.
        start: Starting node.

    Returns:
        paths: Number of available shortest paths from start node.
        predecessors: Predecessors of each node that will be passed through during the shortest path.
    """
    visited_nodes = []
    paths = {node: [] for node in graph.nodes()}
    path_counts = {node: 0  for node in graph.nodes()}
    path_counts[start] = 1
    distances = {node: None for node in graph.nodes()}
    distances[start] = 0

    queue = [start]

    while len(queue) > 0:
        v = queue.pop(0)
        visited_nodes.append(v)

        for w in graph.neighbors(v):
            if distances[w] == None:
                distances[w] = distances[v] + 1
                queue.append(w)
            
            if distances[w] == distances[v] + 1:
                path_counts[w] += path_counts[v]
                paths[w].append(v)

    return visited_nodes, paths, path_counts


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
        visited_nodes, paths, path_counts = bfs(graph, node)

        # Accumulation
        delta = {node: 0 for node in visited_nodes}

        while len(visited_nodes) > 0:
            w = visited_nodes.pop()

            for v in paths[w]:
                delta[v] += (path_counts[v] / path_counts[w]) * (1 + delta[w])

            if w != node:
                centralities[w] += delta[w]
    
    return centralities


def find_top_betweenness_nodes(betweenness_centralities, num):
    """
    Finds the nodes with the greatest betweenness centralities.

    Parameters:
        betweenness_centralities: Dictionary containing the corresponding betweenness centralities
            for each node in the graph.
        num: Number of top nodes to find.

    Returns:
        Nodes with the greatest betweenness centralities.
    """
    sorted_nodes = sorted(betweenness_centralities.items(), key = lambda x: x[1], reverse=True)
    top_nodes = [node for node, _ in sorted_nodes[:num]]

    return top_nodes
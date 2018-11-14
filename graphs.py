"""

This module features useful algorithms for graph problems.

"""

def form_adj_list(vertices, connection_test):
    """

    Form adjacency list for given vertices

    Args:
        vertices (list): List of vertices.
        connection_test (func): Function(vertex1,vertex2) to determine
                                if edge exists between two vertices

    Returns:
        list: Adjacency list of vertices

    """

    adj_list = {}

    for i, vertex1 in enumerate(vertices):

        adj_list[vertex1] = set()

        for j, vertex2 in enumerate(vertices):

            if j == i:
                continue

            if connection_test(vertex1, vertex2):
                adj_list[vertex1].add(vertex2)

    return adj_list

def bfs(adj_list, start_vertex):
    """

    Perform breadth first search to determine connectivity of graph.

    Args:
        adj_list (list): Adjacency list of graph given as
                         dictionary. Key type is agnostic.
                         Value type is Set.
        start_vertex: Start point of BFS

    Returns:
        list: shortest path from start point
        list: parent vertex from start point

    """

    from collections import deque

    parents = {}
    parents[start_vertex] = start_vertex

    levels = {}
    levels[start_vertex] = 0

    frontier = deque([start_vertex])

    while frontier:

        vertex1 = frontier.popleft()

        for vertex2 in adj_list[vertex1]:

            if vertex2 not in levels:
                levels[vertex2] = levels[vertex1] + 1
                parents[vertex2] = vertex1
                frontier.append(vertex2)

    return levels, parents

from itertools import chain, combinations, permutations


def calculate_shortest_paths(adjacency_matrix):
    # using floyd warshall algorithm to generate the shortest path between every pair of vertices
    n = len(adjacency_matrix)
    # start with a clone of the original adjacency matrix
    shortest_paths = [[x for x in y] for y in adjacency_matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if shortest_paths[i][k] + shortest_paths[k][j] < shortest_paths[i][j]:
                    shortest_paths[i][j] = shortest_paths[i][k] + shortest_paths[k][j]
    return shortest_paths


def has_negative_cycle(adjacency_matrix):
    """
    Calculates whether the given graph contains a negative cycle
    :param adjacency_matrix: The graph to search, given as an adjacency matrix
    :return: Whether a negative cycle exists
    """
    # using bellman ford just to detect if a negative cycle exists
    vertex_count = len(adjacency_matrix)
    # we'll assume 9999 is bigger than everything else (foot shooting inbound)
    distance = [9999] * vertex_count
    distance[0] = 0

    for _ in range(vertex_count - 1):
        for node in range(vertex_count):
            for neighbour in range(vertex_count):
                # If the distance between the node and the neighbour is lower than the current, store it
                distance[neighbour] = min(distance[node] + adjacency_matrix[node][neighbour], distance[neighbour])

    for node in range(vertex_count):
        for neighbour in range(vertex_count):
            if distance[neighbour] > distance[node] + adjacency_matrix[node][neighbour]:
                return True
    return False


def all_permutations(items):
    """
    Generates all combinations and permutations of the given list of items.
    The result comes in a specific order. Where the longer items come first,
    and items of the same length are sorted lexicographically.
    >>> all_permutations([1,2])
    >>> [
        (1,2),
        (2,1),
        (1,),
        (2,),
        ()
    ]
    :param items: The list of items to generate combinations for
    :return: All possible combinations and permutations, sorted
    """
    # generate the power set
    power_set = list(chain.from_iterable(combinations(items, r) for r in range(len(items) + 1)))
    # use a reduce (whist we still can :P) to also take every permutation of the power set
    with_permutations = reduce(lambda acc, x: acc + list(permutations(x)), power_set, [])

    def compare(a, b):
        # simple little sort function which returns the longest tuple first
        # and the lexicographically lower tuple when they have equal length
        if len(a) == len(b):
            return -1 if a < b else 1
        else:
            return len(b) - len(a)

    # return the sorted version using our custom comparator function
    return list(sorted(with_permutations, cmp=compare))


def find_most_bunnies(shortest_path_matrix, time_limit):
    """
    Given a matrix where each item is the shortest path between the vertexes.
    returns the maximal amount of bunnies that can be passed whist keeping below the time limit.
    :param shortest_path_matrix: The matrix representing the shortest path between every vertex
    :param time_limit: The maximum time limit
    :return: The list of bunny ID's which can be passes when travelling from the first to last index whilst keeping
    below the time limit,
    """
    bunny_count = len(shortest_path_matrix) - 2
    # we're going to brute force checking the total path cost of every permutation of bunnies
    for permutation in all_permutations(list(range(1, bunny_count + 1))):
        # create the full path by prepending the start and appending the bulkhead vertices
        path = (0,) + permutation + (len(shortest_path_matrix) - 1,)
        # turn our path into a list of edges. eg [1,2,4] -> [(1,2), (2,4)]
        edges = tuple((path[i - 1], path[i]) for i in range(1, len(path)))
        # turn the list of edges into the list of weights
        weights = tuple(shortest_path_matrix[edge[0]][edge[1]] for edge in edges)
        # grab the total weight
        total_path_weight = sum(weights)
        if total_path_weight <= time_limit:
            # if the total path length is less than the time limit,
            # take this path immediately as we're brute forcing in the best order
            # subtract 1 from each vertex as bunny ID's are 0 indexed, but start from vertex 1
            return [i - 1 for i in permutation]
    return []


def answer(adjacency_matrix, time_limit):
    # Okay, first we just want to see if there's a negative cycle.
    # if there is, we can theoretically keep the bulkhead open forever by cycling around the negative cycle.
    if has_negative_cycle(adjacency_matrix=adjacency_matrix):
        # all the bunnies can be saved! (-2 to disclude the start and bulkhead vertices)
        return list(range(0, len(adjacency_matrix) - 2))

    shortest_paths = calculate_shortest_paths(adjacency_matrix=adjacency_matrix)
    return find_most_bunnies(shortest_path_matrix=shortest_paths,
                             time_limit=time_limit)

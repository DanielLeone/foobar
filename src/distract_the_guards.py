def has_match(graph, u, matched_pairs, already_seen):
    """
    A depth first search that finds if a match for vertex u is possible.
    Mutates the map of matched vertices and the set of already seen vertices
    :param graph: The adjacency matrix
    :param u: The vertex to find if it's part of a matching par
    :param matched_pairs: A map of already matched pairs
    :param already_seen: A set of already visited vertices
    :return: Whether vertex u is part of a matching pair
    """
    for v in range(len(graph)):
        # for each potential matching vertex.
        # that is a vertex which can loop and has not already been seen
        if graph[u][v] and v not in already_seen:
            # mark it as seen
            already_seen.add(v)
            # if the potentially matched vertex isn't already matched,
            # or is it matched but there's another match available for it's match,
            # then mark it as a matched pair.
            # Note that checking if there's another match for the match to v won't come up with v
            # again as it's already been marked as seen in the above line
            if v not in matched_pairs or has_match(graph=graph,
                                                   u=matched_pairs[v],
                                                   matched_pairs=matched_pairs,
                                                   already_seen=already_seen):
                matched_pairs[v] = u
                return True
    return False


def max_pairs(graph):
    guard_count = len(graph)
    # a map to keep track of the matched pairs
    matched_pairs = {}
    # tracks the count of guards matched with someone
    result = 0
    # go through each guard (vertex)
    for guard_id in range(guard_count):
        seen = set()
        # ask if it belongs in a match, if so, increment count of matches!
        if has_match(graph=graph, u=guard_id, matched_pairs=matched_pairs, already_seen=seen):
            result += 1
    # bring the result down the closest even number
    return guard_count - 2 * (result / 2)


def will_loop(x, y):
    n = x + y
    n_tilde = n
    while n_tilde % 2 == 0:
        n_tilde = n_tilde / 2
    return (x % n_tilde) != 0


def generate_adjacency_matrix(banana_list):
    # creates an adjacency matrix for a graph of guards, where the edges are defined
    # by guards which will loop indefinitely
    return [[will_loop(x, y) for y in banana_list] for x in banana_list]


def answer(banana_list):
    g = generate_adjacency_matrix(banana_list=banana_list)
    return max_pairs(graph=g)

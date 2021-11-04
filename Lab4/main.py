def bfs(graph, s):
    visited = {s}
    to_explore = [s]

    result = list()

    while to_explore:
        u = to_explore.pop(0)
        result.append(u)
        print(u, end=" ")

        if u not in graph:
            graph[u] = []

        new_vertices = [i for i in graph[u] if i not in visited]
        to_explore.extend(new_vertices)
        visited.update(new_vertices)
    return result

if __name__ == '__main__':
    graph = {
        '0': ['1', '2'],
        '1': ['3', '4'],
        '2': ['5', '6'],
        '3': ['7', '8'],
        '4': ['9', '10']
    }
    bfs(graph, '0')



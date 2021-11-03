def bfs(graph, s):
    visited = {s}
    to_explore = [s]

    while to_explore:
        u = to_explore.pop(0)
        print(u, end=" ")

        if u not in graph:
            graph[u] = []

        new_vertices = [i for i in graph[u] if i not in visited]
        to_explore.extend(new_vertices)
        visited.update(new_vertices)


if __name__ == '__main__':
    graph = {
        '0': ['1', '2'],
        '1': ['3', '4'],
        '2': ['5', '6'],
        '3': ['7', '8'],
        '4': ['9', '10'],
        '5': ['11', '12'],
        '6': ['13', '14'],
        '7': ['15', '16'],
        '8': ['17', '18']
    }
    bfs(graph, '0')


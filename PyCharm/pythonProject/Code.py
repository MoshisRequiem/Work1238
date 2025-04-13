from collections import defaultdict, deque

MOD = 10 ** 9 + 7


def are_overlapping(r1, r2):
    return not (r1[1] < r2[0] or r2[1] < r1[0])


def build_graph(ranges):
    n = len(ranges)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if are_overlapping(ranges[i], ranges[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph


def find_connected_components(graph, n):
    visited = [False] * n
    components = []

    def bfs(start):
        queue = deque([start])
        component = []
        visited[start] = True
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component

    for i in range(n):
        if not visited[i]:
            component = bfs(i)
            components.append(component)

    return components


def find_number_of_ways(ranges):
    graph = build_graph(ranges)
    components = find_connected_components(graph, len(ranges))
    k = len(components)

    if k <= 1:
        return 0  # Only one component or no component, can't split into two non-empty groups

    result = pow(2, k, MOD) - 2  # 2^k - 2
    return result % MOD


if __name__ == '__main__':
    ranges_rows = int(input().strip())
    ranges = []

    for _ in range(ranges_rows):
        start, end = map(int, input().strip().split())
        ranges.append([start, end])

    result = find_number_of_ways(ranges)
    print(result)
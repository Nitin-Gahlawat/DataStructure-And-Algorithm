from collections import deque


def bfs(graph: list[list[int]], start):
    queue = deque()
    visited = [0 for i in range(len(graph))]
    queue.append(start)
    visited[start] = 1
    while len(queue) != 0:
        element = queue.popleft()
        print(element, end=" ")
        for j in range(0, len(graph)):
            if graph[element][j] == 1 and visited[j] == 0:
                visited[j] = 1
                queue.append(j)
    print()


def dfs(graph: list[list[int]], visited: list[int], vertex: int):
    if visited[vertex] != 1:
        visited[vertex] = 1
        print(vertex, end=" ")
        for i in range(0, len(graph[vertex])):
            if graph[vertex][i] == 1:
                dfs(graph, visited, i)


def input_graph() -> list[list[int]]:
    size = int(input("enter number of vertex"))
    mat: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]
    no_of_input = int(input("enter number of input"))
    for i in range(no_of_input):
        to_vertex, from_vertex = map(int, input().split())
        mat[to_vertex][from_vertex] = 1
        mat[from_vertex][to_vertex] = 1
    return mat


if __name__ == "__main__":
    graph = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
    ]

    visited = [0 for i in range(len(graph))]
    bfs(graph, 7)
    dfs(graph, visited, 7)
    print()

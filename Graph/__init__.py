from Graph.Traversal import bfs, dfs, input_graph


def introduction():
    print("\nGraph")
    print("-" * 120)
    print("This Module contains all the algorithm related to the Graph")
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
    print(f"Example of BFS and DFS in Graph G\n {graph}")

    print("BFS Traversal ")
    bfs(graph, 7)
    visited = [0 for i in range(len(graph))]
    print("DFS Traversal ")
    dfs(graph, visited, 7)
    print()

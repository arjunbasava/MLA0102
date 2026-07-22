import heapq

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['G'],
    'E': ['G'],
    'G': []
}

heuristic = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 1,
    'G': 0
}

def greedy_best_first(start, goal):
    visited = set()
    queue = []

    heapq.heappush(queue, (heuristic[start], start))
    path = []

    while queue:
        h, node = heapq.heappop(queue)

        if node not in visited:
            visited.add(node)
            path.append(node)

            if node == goal:
                print("Path:", " -> ".join(path))
                print("Goal Reached")
                return

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristic[neighbor], neighbor))

greedy_best_first('S', 'G')
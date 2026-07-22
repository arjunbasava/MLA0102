import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start))
    visited = set()

    while pq:
        f, g, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            print("Total Cost =", g)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor))

a_star('A', 'F')
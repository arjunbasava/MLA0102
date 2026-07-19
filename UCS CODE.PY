import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

def ucs(start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node == goal:
            print("Minimum Cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph[node]:
                heapq.heappush(queue, (cost + edge_cost, neighbor))

ucs('A', 'G')
import heapq
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 3,
    'G': 0
}
def astar(start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], 0, start, [start]))
    visited = set()
    while open_set:
        f_cost, g_cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g_cost
        visited.add(current)
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g_cost + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')
path, cost = astar('A', 'G')
print("A* Search Path:", path)
print("Total Cost:", cost)
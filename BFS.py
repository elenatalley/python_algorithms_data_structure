graphs = {
    'A':['B', 'C'],
    'B':['A'],
    'C':['D', 'E',],
    'D':['C'],
    'E':['C']
    }

visited = []
queue = []

def bfs(visited, graphs, node):
    visited.append(node)
    queue.append(node)
    while queue: # loop to visit each node
        current = queue.pop(0)
        print(current, end= " ")

        for neighbor in graphs[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("This is Breadth-First Search")
bfs(visited, graphs, 'B')
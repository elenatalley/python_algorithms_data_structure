"""
Проверка смежных вершин в графе
"""
roads = {
    "A":{"B","C"},
    "B":{"A","E","C"},
    "C":{"A","B","D"},
    "D":{"C"},
    "E":{"B"}
}

list_vertex = ["E"] # start node
set_visited = set() # Set to keep track of visited nodes.

while len(list_vertex)!=0:
    cur = list_vertex.pop()
    set_visited.add(cur)
    vertex_children = roads[cur]
    # list_vertex += list(set(vertex_children) - set_visited - set(list_vertex))
    # print(list_vertex)
    for item in vertex_children:
        if not item in set_visited:
            list_vertex.append(item)
    print(list_vertex)
# print(f"все посещенные {set_visited}")
# print(f"смежные вершины {list(set(vertex_children))}")
# print(f"лист вершин{list_vertex }")['B']







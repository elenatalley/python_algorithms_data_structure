with open('matrix.txt') as f:
    list_city = f.readline().split()
    dict_city = dict(zip(list_city, range(len(list_city))))
    matrix = []
    for line in f.readlines():
        matrix.append(list(map(int, line.split())))
print(*matrix, sep="\n")
start = 'A'
stack = [start]
list_visited = set()
while len(stack)>0:
    print(stack)
    v = stack.pop()
    print(v)
    list_visited.add(v)
    index_v = dict_city[v]
    list_children=[]
    for i in range(len(matrix[index_v])):
        if matrix[index_v][i]==1:
            list_children.append(list_city[i])
    list_children = set(list_children) - list_visited - set(stack)
    stack += list(list_children)

    
    

"""
map - подаем функцию и итерируемый объект для функции
filter - подаем функ ктр проверяет на True/False и итерируемый объект для фильтрации
"""

matrix = {'A' : ['B', 'D'],
          'B' : ['A','C'],
          'C' : ['B','A'],
          'D' : ['A']}

visited = [] # Set to keep track of visited nodes.
stack = ['A']
while len(stack) != 0:
    v = stack.pop()
    visited.append(v)
    children = matrix[v]
    a = filter(lambda i: i not in visited and i not in stack, children)
    stack += a
print(visited)







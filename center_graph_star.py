'''
конвертировать в сет каждый список отдельно и сделать пересчение
объеденить все списки в один общий
1. объединение с оставлением дубликатов
2. объединение без дубликатов
3. оставить только уникальные элеметнты от списков

'''

nodes_list = [[1,2],[2,3],[4,2]]
print(nodes_list[0][0])

temp = []
for nodes in nodes_list:
    temp.append(nodes[0])

n = [[8, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(my_lists):
  results = []
  for i1, x in enumerate(my_lists):
    print(i1,x)
    for i2, inner in enumerate(x):
        print(i2, inner)
        results.append(my_lists[i1][i2])
  return results

print(flatten(n))


# for sub_list in documents:
#     temp.append(sub_list[0])
# documents = temp
#documents = [sub_list[0] for sub_list in documents]
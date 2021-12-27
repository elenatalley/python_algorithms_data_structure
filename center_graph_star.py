import functools
'''
конвертировать в сет каждый список отдельно и сделать пересчение - &
объеденить все списки в один общий
1. объединение с оставлением дубликатов
2. объединение без дубликатов
3. оставить только уникальные элементы от списков
'''

# 1. объединение с оставлением дубликатов
spisok = [[1,2],[2,3],[4,2]]
# for element in range(len(spisok)):
#     spisok[element] = set(spisok[element])

# print(spisok)
result = set.intersection(*map(set, spisok))
print(result)
    # print(element)
    # for indexes_for_internal_lists in range(len(spisok[element])):
    #     print( spisok[element][indexes_for_internal_lists], end = ' ')
#
# result = set(spisok[0])
# for i in spisok:
#     d=set(i)
#     result&=d
#     print(d)
# result = functools.reduce(lambda a,b: a&set(b), spisok, set(spisok[0]))
# print(result)














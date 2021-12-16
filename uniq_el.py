file = open('input2.txt')
readed_data = file.readlines()
file.close()
new_lists = []
for i in readed_data:
    new_lists.append(i.split())
s1 = set(new_lists[0])
s2 = set(new_lists[1])
s3 = s1 & s2 # отбирает одинаковые значения в обоих множествах
s4 = s1 | s2 # объединение множеств
print(s1)
print(s2)
print(s3)
print(s4)
print(s4 - s3)
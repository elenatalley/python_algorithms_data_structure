"""
словарь = хэш таблица
словарь =  список с произвольными индексами (ключами)
ключи - любой тип данных (неизменяемый тип)
список - изменяемый тип => не может быть ключом
значение - любой тип данных, без ограничений в том числе м. б. список
"""
d = {}
d1 = dict()
d2 = {"name":"John","age":18, (0,5):"pre-school", (5,8):"unknown", (8,18):["school","footbol"]}
print(d2)
print(d2["name"])
print(d2[(8,18)])
print(d2[(8,18)][0])
a = 1,2,3,4,5
print(a)
# print(d2[8,18][0])

d2["name"] = "Adam"
print(d2)


for i in d2:
    print(i,d2[i])

for i in d2:
    d2[i] = "Secret"
print(d2)

"""
ключ = список, словарь
значение = словарь
"""
# key_list = {['first_name', 'last_name', 'dob']:['Ivan','Ivanov', 1977]} #TypeError: unhashable type: 'list'
# key_dict = {{'order':'pizza'}, {'price':2}} #TypeError: unhashable type: 'dict'
# print(key_list)

f={"name": {"m","n"}}
print(f)
"""
несколько пар танцоров
зрители оценивают: номер пары: голос
сколько голосов набрала каждая пара
"""

couples = ['couple_1', 'couple_2', 'couple_3']
# votes = list(input("Enter  points for couple1: "))
votes = [[1,2,3], [2,1,3], [1,1,3]]
sum_points =[]
for i in range(len(votes)):
    s = sum(votes[i])
    sum_points.append(s)
    d = dict(zip(couples, sum_points))
print(f"This is the total points for each couple: {d}")

max_val = max(d.values())

final_d = {k:v for k, v in d.items() if v == max_val}
print(f"This couple has most votes: {final_d}")

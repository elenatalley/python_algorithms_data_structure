"""
Given an array of integers nums and an integer
target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

list_num = [2,7,11,15]
target = 9
# for i in range(len(list_num)):
#     for j in range(len(list_num)):
#         if i!=j and list_num[i]+list_num[j]==target:
#             print(i,j)

# for i in range(len(list_num)):
#     check_i = target - list_num[i]
#     if check_i not in list_num:
#         list_num[i]+=1
#     else:
#         print(i, list_num.index(check_i))
#         break

# i - index, num  - element
d = {}
for i,num in enumerate(list_num):
    # print(d)
    needed = target - num
    if num in d:
        print(d[num], i)
        break
    d[needed] = i




"""
21. Merge Two Sorted Lists
"""
# list1 = [1,2,4]
# list2 = [1,3,4]
#
# l =list1 + list2
# print(l)
# s = sorted(l)
# print(s)
# new=[]
# for i in range(len(l)-1):
#     if s[i] <= s[i+1]:
#         new.append(i)
# print(new)








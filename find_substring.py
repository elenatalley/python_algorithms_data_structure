"""
find substring that can be found on every of these stings
"""
strs = ('A,B,C,E,D,C,S,G,A,B,D,D,K,L,A'
        'B,D,D,K,A,B,C,E,D,'
        'D,K,C,S,G,A,B,D,D,K,L,A'
        'A,B,D,D,K,L,B,D'
        )
str1 = ['A,B,C,E,D,C,S,G,A,B,D,D,K,L,A']
str2 = ['B,D,D,K,A,B,C,E,D,']
str3 = ['D,K,C,S,G,A,B,D,D,K,L,A']
str4 = ['A,B,D,D,K,L,B,D']

combinations = []
for i in str1:
    for j in str2:
        for k in str3:
            for l in str4:
                result = i + j + k + l
                combinations.append(result)
print(result)
a = input("Enter 3 numbers:  ").split()

for i in range(0,len(a)):
    a[i] = int(a[i])


while True:
    t = False
    for i in range(0,len(a) - 1):
        if a[i] > a[i + 1]:
            a[i + 1], a[i] = a[i], a[i + 1]
            t = True
    if t == False:
        break

print(a)






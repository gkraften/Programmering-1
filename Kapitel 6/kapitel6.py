for i in range(1, 10):
    for a in range(20 - 2*i - 2):
        print(end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    for k in range(i-1, 0, -1):
        print(k, end=" ")
    print()

for i in range(9, 0, -1):
    for j in range(18 - 2*i + 2 ):
        print(end=" ")
    for k in range(1, i):
        print(k, end=" ")
    print()
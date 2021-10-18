n1 = int(input())
n2 = int(input())
n3 = int(input())
d1 = int(input())
d2 = int(input())
d3 = int(input())
a1 = int(input())
a2 = int(input())
suppose = []
if d1 == a1 or d1 == a2:
    suppose.append(n1)
if d2 == a1 or d2 == a2:
    suppose.append(n2)
if d3 == a1 or d3 == a2:
    suppose.append(n3)
suppose.sort()
if len(suppose) != 0:
    for i in range(len(suppose)):
        if i == len(suppose) - 1:
            print(suppose[i])
            break
        print(suppose[i], end=",")
else:
    print(-1)


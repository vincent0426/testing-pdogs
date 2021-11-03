n, m = [int(x) for x in input().split(",")]

p = [int(x) for x in input().split(",")]
x = [int(x) for x in input().split(",")]
q = [int(x) for x in input().split(",")]

money = 0
for i in range(n):
    money += p[i] * x[i]

l = [0]

for i in range(m):
    length = len(l)
    for j in range(length):
        l.append(l[j] + q[i])

l = l.sort(reverse=True)
for i in range(len(l)):
    if l[i] > money:
        continue
    else:
        print(money - l[i])
        break

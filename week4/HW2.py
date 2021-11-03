n = int(input())

fire = [int(x) for x in input().split(",")]

max_total = 10000000

for i in range(n):
    temp = [float(x) for x in input().split(",")]
    total = 0
    for j in range(n):
        total += fire[j]*temp[j]
    if total < max_total:
        max_total = total
        index = i

if max_total == int(max_total):
    max_total = int(max_total)

print(index + 1, max_total, sep=",")

n = int(input())

x = [int(x) for x in input().split(",")]
p = [int(x) for x in input().split(",")]

tot = 0
for i in range(n):
    tot += x[i]*p[i]

tot_1 = str(tot).count("1")
print(tot, tot_1, sep=",")

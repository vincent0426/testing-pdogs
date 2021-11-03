m, n, Q, D = [int(x) for x in input().split(",")]

p = [int(x) for x in input().split(",")]

alltot = 0
for i in range(n):
    x = [int(x) for x in input().split(",")]
    tot = 0
    for j in range(m):
        tot += x[j] * p[j]
    if tot >= Q:
        tot -= D
        tot = max(tot, Q)
    alltot += tot
print(alltot)

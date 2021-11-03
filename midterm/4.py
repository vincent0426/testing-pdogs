T, ns, nl, qs, ql, rs, rl = [int(x) for x in input().split(",")]

ps = [float(x) for x in input().split(",")]
pl = [float(x) for x in input().split(",")]


maxtotal = -1

for i in range(T + 1):
    total = 0
    smaller = i
    larger = T - i
    Es = 0
    El = 0
    smaller_amount = smaller*qs
    larger_amount = larger*ql
    smaller_amount = min(ns, smaller_amount)
    larger_amount = min(nl, larger_amount)
    for i in range(smaller_amount + 1):
        Es += ps[i]*i

    for i in range(larger_amount + 1):
        El += pl[i]*i
    total += rs*Es + rl*El
    if total > maxtotal:
        maxtotal = total
print(int(maxtotal))

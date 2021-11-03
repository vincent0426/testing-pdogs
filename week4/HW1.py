n, m = [int(x) for x in input().split(",")]

price_l = [int(x) for x in input().split(",")]
x_l = [int(x) for x in input().split(",")]

total = 0
for i in range(n):
    total += price_l[i]*x_l[i]

m_l = [int(x) for x in input().split(",")]

for m in m_l:
    if total - m >= 0:
        total -= m

print(total)

n = int(input())
maxProfit = 0
maxPrice = 1000
curMaxPrice = 0
index = 0
for i in range(n):
    a = int(input())
    b = int(input())
    c = int(input())
    if c > a:
        continue
    p = 1
    curMaxProfit = 0
    while(a - b*p > 0):
        demand = max(a - b*p, 0)
        if demand == 0:
            break
        profit = demand*(p - c) 
        if profit >= curMaxProfit:
            curMaxProfit = profit
            curMaxPrice = p
        p += 1
    if curMaxProfit > maxProfit:
        maxProfit = curMaxProfit
        maxPrice = curMaxPrice
        index = i
print(index + 1, maxPrice, maxProfit, sep=",")

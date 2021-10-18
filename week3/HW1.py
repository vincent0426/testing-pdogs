n, c = [int(x) for x in input().split(",")]

price = [int(x) for x in input().split(",")]
demand = [int(x) for x in input().split(",")]

max_profit = demand[0]*(price[0] - c)
max_price = price[0]

for i in range(1, n):
    each_profit = price[i] - c
    total_profit = each_profit * demand[i]
    if total_profit > max_profit:
        max_index = i
        max_profit = total_profit
        max_price = price[i]
    elif total_profit == max_profit:
        if price[i] > price[max_index]:
            max_index = i
            max_profit = total_profit
            max_price = price[i]

print(max_price, max_profit, sep=",")

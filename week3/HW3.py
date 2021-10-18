n, B = [int(x) for x in input().split(",")]

weight = [int(x) for x in input().split(",")]
value = [int(x) for x in input().split(",")]
whether = [int(x) for x in input().split(",")]

total_weight = 0
total_value = 0

for i in range(n):
    if whether[i] == 1:
        total_weight += weight[i]
        total_value += value[i]
if total_weight <= B:
    print(total_weight, total_value, sep=",")
else:
    print("-1")

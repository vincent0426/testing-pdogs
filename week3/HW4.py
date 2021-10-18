n, B = [int(x) for x in input().split(",")]

weight = [int(x) for x in input().split(",")]
value = [int(x) for x in input().split(",")]

test = int(input())
max_value = -1000000000

for i in range(test):
    l = [int(x) for x in input().split(",")]
    id = l[0]
    whether = l[1:]
    total_weight = 0
    total_value = 0

    for i in range(n):
        if whether[i] == 1:
            total_weight += weight[i]
            total_value += value[i]

    if total_weight <= B and total_value >= max_value:
        if total_value == max_value:
            if id < max_index:
                max_index = id
                max_value = total_value
                max_weight = total_weight
        else:
            max_index = id
            max_value = total_value
            max_weight = total_weight


print(max_index, max_weight, max_value, sep=",")

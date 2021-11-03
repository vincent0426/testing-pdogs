n, k = [int(x) for x in input().split(",")]

fire = [int(x) for x in input().split(",")]

build = []
final_list = []
for i in range(n):
    build.append(0)

adj_mat = []

min_total = 10000000
for i in range(n):
    temp = [float(x) for x in input().split(",")]
    adj_mat.append(temp)
    total = 0
    for j in range(n):
        total += fire[j]*temp[j]
    if total < min_total:
        min_total = total
        index = i
build[index] = 1
final_list.append(index)
for i in range(k - 1):
    longer = -1
    for j in range(n):
        smaller = 10000000
        # 已經蓋的過就不跑
        if build[j] == 0:
            for z in range(n):
                if build[z] == 1:
                    if adj_mat[j][z] < smaller:
                        smaller = adj_mat[j][z]
                        # smaller_index = z
            if smaller > longer:
                longer = smaller
                longer_index = j
    build[longer_index] = 1
    final_list.append(longer_index)


max_total = 0

for i in range(n):
    if build[i] == 0:
        total = 1000000
        for j in range(n):
            if build[j] == 1 and fire[i]*adj_mat[i][j] < total:
                total = fire[i]*adj_mat[i][j]
        max_total += total


if max_total == int(max_total):
    max_total = int(max_total)

for i in range(len(final_list)):
    if i == len(final_list) - 1:
        print(final_list[i] + 1, end=";")
        print(max_total)
    else:
        print(final_list[i] + 1, end=",")

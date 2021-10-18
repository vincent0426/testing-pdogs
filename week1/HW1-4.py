x = input()
y = input()
A = 0
B = 0
for i in range(len(x)):
    cur = x[i]
    for j in range(len(y)):
        if cur == y[j] and i == j:
            A += 1
        elif cur == y[j] and i != j:
            B += 1
print(f"{A}A{B}B")

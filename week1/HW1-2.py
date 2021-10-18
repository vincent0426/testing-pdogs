x1 = int(input())
x2 = int(input())
r = int(input())
y = int(input())
if x1 >= y:
    x1 -= y
    x2 += r*y
else:
    x2 += r*x1
    x1 = 0
print(x1, x2, sep=",")
n = int(input())
x = int(input())
y = int(input())
r = int(input())

if n >= r:
    total = r * x
else:
    total = n*x + (r - n)*y

print(total)
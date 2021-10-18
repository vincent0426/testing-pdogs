n = int(input())
m = int(input())
x = int(input())
y = int(input())
b = int(input())
r1 = int(input())
r2 = int(input())
r3 = int(input())
r4 = int(input())
r5 = int(input())
r6 = int(input())
r7 = int(input())

total = r1 + r2 + r3 + r4 + r5 + r6 + r7
money = b if total >= m else 0

if n >= r1:
    money += r1* x
else:
    money += n*x + (r1 - n)*y
if n >= r2:
    money += r2* x
else:
    money += n*x + (r2 - n)*y
if n >= r3:
    money += r3* x
else:
    money += n*x + (r3 - n)*y
if n >= r4:
    money += r4* x
else:
    money += n*x + (r4 - n)*y
if n >= r5:
    money += r5* x
else:
    money += n*x + (r5 - n)*y
if n >= r6:
    money += r6* x
else:
    money += n*x + (r6 - n)*y
if n >= r7:
    money += r7* x
else:
    money += n*x + (r7 - n)*y

print(money)
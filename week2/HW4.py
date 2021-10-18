n = int(input())
t = int(input())
q1 = int(input())
q2 = int(input())

first_remain = 480
second_remain = 480

l = []
revenue = 0

for i in range(n):
    x = int(input())
    p = int(input())
    one_car = p / x
    if one_car < t:
        continue
    else:
        first_time =  x * q1
        second_time = x * q2
        if first_time <= first_remain and second_time <= second_remain:
            first_remain -= first_time
            second_remain -= second_time
            l.append(i+1)
            revenue += p

if len(l) == 0:
    print("-1")
else:
    for i in range(len(l)):
        if i == len(l) - 1:
            print(l[i])
            break
        print(l[i], end=",")
print(first_remain, second_remain, revenue, sep=",")
            
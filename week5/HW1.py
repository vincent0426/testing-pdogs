def mono_inc(inlist, k=3):
    ans = []
    temp = []
    ans.append(0)
    temp.append(inlist[0])
    for i in range(1, len(inlist)):
        if inlist[i] > temp[-1]:
            temp.append(inlist[i])
            if i == len(inlist) - 1 and len(temp) > k:
                ans.append(i)
                return ans
        else:
            if len(temp) > k:
                ans.append(i - 1)
                return ans
            ans[0] = i
            temp.clear()
            temp.append(inlist[i])
    return "None"


people = [int(x) for x in input().split(",")]

k = int(input())

ans = mono_inc(people, k) if k >= 3 else mono_inc(people)

if ans == "None":
    print(ans)
else:
    for i in range(2):
        print(ans[i])

def mono_inc_plus(inlist, k=3):
    final_list = []
    ans = []
    temp = []
    ans.append(0)
    temp.append(inlist[0])
    for i in range(1, len(inlist)):
        if inlist[i] > temp[-1]:
            temp.append(inlist[i])
            if i == len(inlist) - 1 and len(temp) > k:
                ans.append(i)
                final_list.append(ans)
                ans = []
        else:
            if len(temp) > k:
                ans.append(i-1)
                final_list.append(ans)
                ans = []
                ans.append(i)
                temp.clear()
                temp.append(inlist[i])
            else:
                ans[0] = i
                temp.clear()
                temp.append(inlist[i])
    return final_list


people = [int(x) for x in input().split(",")]

k = int(input())

ans_list = mono_inc_plus(people, k) if k >= 3 else mono_inc_plus(people)

if len(ans_list) == 0:
    print("None")
else:
    for i in range(len(ans_list)):
        print(ans_list[i][0], ans_list[i][1], sep=" ", end="")
        print("")

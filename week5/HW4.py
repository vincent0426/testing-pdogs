def printrec(records):
    for arec in records:
        print(f"{arec[0]}_{arec[1]:.2f}_{arec[2]:.2f}")


def apply_discount(records):
    total = 0
    dis = 0
    ans = []
    for i in range(len(records)):
        records[i][1] = float(records[i][1])
        records[i][2] = float(records[i][2])
        if records[i][2] > 0:
            total += records[i][2]
        elif records[i][2] < 0:
            dis += records[i][2]
    for i in range(len(records)):
        if records[i][2] < 0:
            continue
        temp = []
        temp.append(records[i][0])
        temp.append(records[i][1])
        before = records[i][2]

        after = (before + dis*(records[i][2] / total))
        if after < 0:
            temp.append(0)
        else:
            temp.append(after)
        ans.append(temp)
    return ans


l = []
while(True):
    s = input()
    if s == "RECORDSTOP":
        break
    l.append(s.split("_"))

ans = apply_discount(l)


printrec(ans)
print("---Original---")
printrec(l)

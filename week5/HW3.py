def my_hhi(ylist, htype="Original"):
    total = 0
    l = []
    for i in range(len(ylist)):
        ylist[i] = abs(ylist[i])
        total += ylist[i]
    for i in range(len(ylist)):
        l.append(ylist[i] / total)
    hhi = 0
    for i in range(len(ylist)):
        hhi += l[i]**2
    if htype == "Original":
        return hhi
    else:
        return (hhi - (1 / len(ylist))) / (1 - (1/len(ylist)))


def printresult(value):
    print(f"{value:.4f}")


rev = [float(x) for x in input().split(",")]
htype = input()

printresult(my_hhi(rev, htype))

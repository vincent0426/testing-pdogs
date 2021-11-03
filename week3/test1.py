"""
檢查背包_背包問題
"""
num_bagStr = input()  # 輸入物品數量+背包承重，物品重量，物品效用，是否攜帶
weightStr = input()
utilityStr = input()
bag_num = int(input())


num_bags = num_bagStr.split(",")  # 將list數據以逗號分開
weights = weightStr.split(",")
utilitys = utilityStr.split(",")

for i in range(2):  # 將分開的數據化為int
    num_bags[i] = int(num_bags[i])
for i in range(num_bags[0]):
    weights[i] = int(weights[i])
for i in range(num_bags[0]):
    utilitys[i] = int(utilitys[i])

now_utility = -1
now_weight = 0
for n in range(bag_num):  # 透過bag_num決定要幾組資料
    bagStr = input()
    bags = bagStr.split(",")
    for a in range(num_bags[0] + 1):  # 將分開的數據化為int
        bags[a] = int(bags[a])
    now_bag = bags[0]
    sum_weight = 0  # 設總重量
    sum_utility = 0  # 設總效能

    for k in range(1, num_bags[0]+1):  # 查看該物品是否要攜帶
        now_bag = bags[0]
        if bags[k] == 1:  # 若要攜帶則加總重量及效益    `
            sum_weight += weights[k-1]
            sum_utility += utilitys[k-1]

        else:
            continue

    # print(now_bag, sum_weight, sum_utility)
    if sum_weight <= num_bags[1]:
        if sum_utility > now_utility:
            best_bag = now_bag
            now_weight = sum_weight
            now_utility = sum_utility

        elif sum_utility == now_utility:
            if now_bag < best_bag:
                now_weight = sum_weight
                now_utility = sum_utility
                best_bag = now_bag
print(best_bag, now_weight, now_utility, sep=",")

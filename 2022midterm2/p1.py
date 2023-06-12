


nums_stores = int(input())
pos = []
for i in input().split(","):
    pos.append(int(i))

dis = []
for i in range(nums_stores):
    curr_dis = 0
    for j in range(nums_stores):
        curr_dis += abs(pos[j] - pos[i])
    dis.append(curr_dis)

mini = min(dis)
ans = []
for i in range(nums_stores):
    if dis[i] == mini:
        ans.append(i+1)
for i in range(len(ans)):
    if i < len(ans) - 1:
        print(ans[i], end=",")
    else:
        print(ans[i], end="")





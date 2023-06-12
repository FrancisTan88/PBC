station = [int(i) for i in input().split(",")]
capacity = int(input())
ans = []
while any(station):
    curr = []
    tmp = capacity
    for i in range(len(station)):
        if tmp <= station[i]:
            curr.append(tmp)
            station[i] -= tmp
            tmp = 0
        else:
            curr.append(station[i])
            tmp -= station[i]
            station[i] = 0
    ans.append(curr)
print(ans)

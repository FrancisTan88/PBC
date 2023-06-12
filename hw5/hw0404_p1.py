def find_troughs(inlist, k=2):
    ans = []
    n = len(inlist)
    for i in range(k, n-k):
        left, right = i-1, i+1
        not_bottom = False
        while left >= i-k and right <= i+k:
            if inlist[left] <= inlist[left+1] or inlist[right] <= inlist[right-1]:
                not_bottom = True
            left -= 1
            right += 1
        if not not_bottom:
            ans.append(i)
    return ans

water_lvl = [float(i) for i in input().split(",")]
k = int(input())
if k < 1:
    pos = find_troughs(water_lvl)
else:
    pos = find_troughs(water_lvl, k)
if len(pos) == 0:
    print("NA")
else:
    for idx in pos:
        print(idx)



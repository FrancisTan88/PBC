def find_troughs_wings(inlist, k=2):
    ans = []
    n = len(inlist)
    for i in range(k+1, n-k-1):
        left, right = i-1, i+1
        not_bottom = False
        while left >= i-k and right <= i+k:
            if inlist[left] <= inlist[left+1] or inlist[right] <= inlist[right-1]:
                not_bottom = True
            left -= 1
            right += 1
        if inlist[left] >= inlist[left+1] or inlist[right] >= inlist[right-1]:
            not_bottom = True
        if not not_bottom:
            ans.append(i)
    return ans

water_lvl = [float(i) for i in input().split(",")]
k = int(input())
if k < 1:
    ans = find_troughs_wings(water_lvl)
else:
    ans = find_troughs_wings(water_lvl, k)
if not ans:
    print("NA")
else:
    for idx in ans:
        print(idx)
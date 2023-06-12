def find_troughs(water, k1=2, k2=2):
    ans = []
    n = len(water)
    for i in range(k1, n-k2):
        bottom = True
        for j in range(i, i-k1, -1):
            if water[j-1] <= water[j]:
                bottom = False
        for k in range(i, i+k2):
            if water[k+1] <= water[k]:
                bottom = False
        if bottom:
            ans.append(i)
    if not ans:
        return None
    return ans


water_lvl = [float(i) for i in input().split(",")]
k1 = int(input())
k2 = int(input())
if k1 >= 1 and k2 >= 1:
    a = find_troughs(water_lvl, k1, k2)
elif k1 < 1 and k2 >= 1:
    a = find_troughs(water_lvl, 2, k2)
elif k1 >=1 and k2 < 1:
    a = find_troughs(water_lvl, k1, 2)
else:
    a = find_troughs(water_lvl, 2, 2)
if a == None:
    print("NA")
else:
    for i in a:
        print(i)

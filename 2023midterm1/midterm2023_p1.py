n1, n2 = [int(i) for i in input().split(",")]
works = [int(i) for i in input().split(",")]
pbc = [int(i) for i in input().split(",")]
m1 = 0
m2 = 0
for i in works:
    m1 += i
for i in pbc:
    m2 += i
m1 /= len(works)
m2 /= len(pbc)

if m1 > m2:
    print(1)
elif m1 < m2:
    print(2)
else:
    print(0)
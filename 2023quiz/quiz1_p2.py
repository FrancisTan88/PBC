n = int(input())
lst = [int(i) for i in input().split(",")]
divide = lst[0]
ans = []
count = 0
for i in range(1, len(lst)):
    if not lst[i] % divide:
        count += 1
    ans.append(lst[i] % divide)

if all(ans):
    print(1)
elif not any(ans):
    print(3)
elif count == 1:
    print(2)
else:
    print(4)
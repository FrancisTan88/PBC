m, n, c0 = [int(i) for i in input().split(",")]
probabilities = [int(i) for i in input().split(",")]
categories = [int(i) for i in input().split(",")]

choose = []
for i in range(len(categories)):
    if categories[i] == c0:
        choose.append(probabilities[i])
choose.sort()
length = len(choose)
ans = []
if length >= 3:
    for i in range(length-1, length-4, -1):
        ans.append(choose[i])
else:
    for i in range(length-1, -1, -1):
        ans.append(choose[i])
    for j in range(3 - len(ans)):
        ans.append(-1)
ans = list(map(str, ans))
print(",".join(ans))
    




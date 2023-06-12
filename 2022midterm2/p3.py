n, k, t = [int(i) for i in input().split(",")]
positive = ["good", "best", "awesome", "wonderful", "nice"]
ans = 0
# for x, y in input().split(","):
#     print(x)
#     print(y)
for i in range(n):
    score, comment = input().split(",")
    score = int(score)
    comment = comment.split(" ")
    if score >= k:
        nums_positive = 0
        for i in positive:
            nums_positive += comment.count(i)
        if nums_positive >= t:
            ans += 1
print(ans)
        





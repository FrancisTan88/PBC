target = input()
text = input()
target_split = []
idx = 0
while idx < len(target):
    if target[idx] == "?":
        target_split.append(target[:idx])
        what = ""
        while target[idx] == "?":
            what += "?"
            idx += 1
        target_split.append(what)
        target_split.append(target[idx:])
        break
    idx += 1
front, ques, end = target_split[0], target_split[1], target_split[2]
total_len = len(front) + len(ques) + len(end)
n = len(text)
ans = []
for i in range(n):
    if text[i] == front[0]:
        if i + total_len <= n:
            if front == text[i:i+len(front)] and end == text[i+len(front)+len(ques):i+len(front)+len(ques)+len(end)]:
                ans.append(text[i:i+total_len])
if not ans:
    print("^^^NOT_FOUND^^^")
else:
    for i in ans:
        print(i)

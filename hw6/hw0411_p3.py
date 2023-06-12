# read the input data
content = input()

# process the content
signs = {",", "%", "."}
idx1 = 0
ans = ""
while idx1 < len(content):
    if content[idx1].isdigit():
        idx2 = idx1
        while idx2 < len(content) and (content[idx2].isdigit() or content[idx2] in signs):
            idx2 += 1
        ans += f"<<{content[idx1:idx2]}>>"
        idx1 = idx2
        continue
    else:
        ans += content[idx1]
    idx1 += 1
print(ans)
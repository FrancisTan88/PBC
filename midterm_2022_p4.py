n = int(input())
work_times = [int(i) for i in input().split(",")]
ddl = [int(i) for i in input().split(",")]
orders = [i+1 for i in range(n)]

sorted_lst = sorted(zip(work_times, ddl, orders), key=lambda x: x[1])
total_time = 0
ans = []
ignore = []
for i in range(len(sorted_lst)):
    if total_time + sorted_lst[i][0] > sorted_lst[i][1]:
        ignore.append(sorted_lst[i][2])
    else:
        ans.append(sorted_lst[i][2])
        total_time += sorted_lst[i][0]
ans += ignore
ans = list(map(str, ans))
print(",".join(ans) + ";" + str(len(ignore)))


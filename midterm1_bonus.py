def helper(waiting_time, reserve_time, intervals):
    s, e = reserve_time[0], reserve_time[1]
    for iv in intervals:
        if e > iv[0] and s < iv[1]:
            waiting_time += iv[1] - s
            if waiting_time > 30:
                return -1, [None, None]
            reserve_time = [iv[1], iv[1]+e-s]
            s, e = reserve_time[0], reserve_time[1]
    if reserve_time[1] > 360:
        return -1, [None, None]
    return waiting_time, reserve_time

customers, masseur = [int(i) for i in input().split(",")]
serve_time = [int(i) for i in input().split(",")]
reserve_time = [int(i) for i in input().split(",")]
money = [int(i) for i in input().split(",")]

sort_arr = [(serve_time[i], reserve_time[i], i) for i in range(customers)]
sort_arr.sort()

ending_time_masseur = [[]for _ in range(masseur)]
people = 0
revenue = 0
for st, rt, number in sort_arr:
    if rt+st > 360: continue
    interval = [rt, rt+st]
    min_waiting_time = float("inf")
    min_number = -1
    min_interval = [None, None]
    for i in range(masseur):
        curr_waiting_time, curr_interval = helper(0, [rt, rt+st], ending_time_masseur[i])
        if curr_waiting_time != -1 and curr_waiting_time < min_waiting_time:
            min_waiting_time = curr_waiting_time
            min_number = i
            min_interval = curr_interval
    if min_number != -1:
        people += 1
        revenue += money[number]
        ending_time_masseur[min_number].append(min_interval)
        ending_time_masseur[min_number].sort()
print(f"{people},{revenue}")

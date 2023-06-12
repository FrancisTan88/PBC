def calculate(sick, normal):
    onverlap = 0
    if normal[0] <= sick[0]:
        if normal[1] <= sick[1]:
            onverlap = normal[1] - sick[0]
        else:
            onverlap = sick[1] - sick[0]
    elif normal[0] < sick[1]:
        if normal[1] <= sick[1]:
            onverlap = normal[1] - normal[0]
        else:
            onverlap = sick[1] - normal[0]
    if onverlap >= 10:
        return True
    return False
            

n = int(input())
data = []
for i in range(n):
    tmp_arr = input().split(",")
    data.append(tmp_arr)
sick_number, sick_enter, sick_leave, sick_building = input().split(",")
sick_enter = sick_enter.split(":")
sick_leave = sick_leave.split(":")
sick_interval = [60 * int(sick_enter[0]) + int(sick_enter[1]), 60 * int(sick_leave[0]) + int(sick_leave[1])]

ans = []
for id, enter, leave, building in data:
    if building == sick_building:
        id = int(id)
        enter = enter.split(":")
        leave = leave.split(":")
        time_interval = [60 * int(enter[0]) + int(enter[1]), 60 * int(leave[0]) + int(leave[1])]
        if calculate(sick_interval, time_interval):
            ans.append(id)
ans.sort()
print(",".join(list(map(str, ans))))

n = int(input())
k = int(input())
people = [int(i) for i in input().split(",")]

schedule = []
while any(people):
    curr_bus = []
    capacity = k
    for i in range(len(people)):
        if capacity >= people[i] and people[i] != 0:
            curr_bus.append((i+1, people[i]))
            capacity -= people[i]
            people[i] = 0
        else:
            if capacity > 0 and people[i] != 0:
                curr_bus.append((i+1, capacity))
                people[i] -= capacity
                capacity = 0
    schedule.append(curr_bus)
# schedule = [[[map(str, e) for e in schedule[x][y]] for y in schedule[x]] for x in schedule]
# print(schedule)
for i in range(len(schedule)):
    # for k in range(len(schedule[i])):
    #     schedule
    for j in range(len(schedule[i])):
        if j != len(schedule[i]) - 1:
            print(str(schedule[i][j][0])+","+str(schedule[i][j][1]), end=";")
        else:
            print(str(schedule[i][j][0])+","+str(schedule[i][j][1]))




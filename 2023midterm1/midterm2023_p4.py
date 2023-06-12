n, k = [int(i) for i in input().split(",")]
people = [int(i) for i in input().split(",")]
distance = [[int(i) for i in input().split(",")] for j in range(n+1)]

bus = 0
total_dis = 0
while any(people):
    curr_pos = 0
    bus += 1
    capacity = k
    while any(people) and capacity >= min(x for x in people if x != 0):
        min_dis = float("inf")
        target = -1
        for i in range(len(people)):
            if people[i] and capacity >= people[i] and distance[curr_pos][i+1] < min_dis:
                min_dis = distance[curr_pos][i+1]
                target = i+1
        total_dis += min_dis
        capacity -= people[target-1]
        curr_pos = target
        people[target-1] = 0
    total_dis += distance[curr_pos][0]
print(f"{bus},{total_dis}")







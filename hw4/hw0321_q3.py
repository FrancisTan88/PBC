# read the input data
categories, production_lines = [int(i) for i in input().split(",")]
production_time = [[int(i) for i in input().split(",")] for j in range(production_lines)]

# get the production order by sorting according to the descriptive priority
# production_order: List[List[total time, time by lines1,2,...,m, product order]]
production_order = []
for j in range(len(production_time[0])):
    total_time = 0
    time_by_lines = []
    for i in range(len(production_time)):
        total_time += production_time[i][j]
        time_by_lines.append(production_time[i][j])
    production_order.append([total_time] + time_by_lines + [j])
production_order = sorted(production_order, key=lambda x: [x[i] for i in range(len(production_order[0]))])
orders = [i[-1] for i in production_order]
hashmap = {val: idx for idx, val in enumerate(orders)}

# create a new production time in sorted production order
sorted_production_time = []
for i in range(len(production_time)):
    time_by_lines = []
    for j in range(len(production_time[0])):
        time_by_lines.append(production_time[i][orders[j]])
    sorted_production_time.append(time_by_lines)

# calculate the wasted time lines by lines, let's use some dynamic programming here
wasted_time = [[0] * categories]
for line in range(1, production_lines):
    base_production_time = 0
    curr_production_time = 0
    curr_wasted_time = [wasted_time[line-1][0] + sorted_production_time[line-1][0]]
    for types in range(1, categories):
        base_production_time += sorted_production_time[line-1][types] + wasted_time[line-1][types]
        curr_production_time += sorted_production_time[line][types-1]
        if base_production_time > curr_production_time:
            time_gap = base_production_time - curr_production_time
            curr_wasted_time.append(time_gap)
            curr_production_time += time_gap
        else:
            curr_wasted_time.append(0)
    wasted_time.append(curr_wasted_time)        

# calculate the complete time of each product ordered by sorted list
total_wasted_time = sum(sum(wasted_time, []))
complete_time = [production_order[0][0]]
for types in range(1, categories):
    complete_time.append(complete_time[types-1] + wasted_time[-1][types] + sorted_production_time[-1][types])

# print the answer
for i in range(categories):
    print(complete_time[hashmap[i]], end=",")
print(total_wasted_time)
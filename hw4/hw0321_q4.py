# read the input data
first_line = []
production_time = []
for i in input().split(","):
    first_line.append(int(i))
categories, production_lines = first_line[0], first_line[1]
for j in range(production_lines):
    tmp = []
    for i in input().split(","):
        tmp.append(int(i))
    production_time.append(tmp)

# Main Usage:
# an m*1 array to maintain the ending time of each production line
# an 1*n array to avoid duplicately visiting
# eventually, we will get (1)the complete time of each prodcut (2)the total idle time according to the order of production
end_time_base = []
for line in range(production_lines):
    end_time_base.append([0])
visited = [0] * categories
product_order = []
complete_time = []
total_idle_time = 0

# iterate until we have traversed all the products
while len(product_order) < categories:
    # maintain some values below of every round
    min_idle_time = 5001
    cache = [-1, -1]  # [the product's complete time(which has the minimum idle time so far), the product's order]
    min_end_time = []  # the ending time that has the minimum idle time
    for line in range(production_lines):
        min_end_time.append([0])

    # find the minimum idle time among those products that have not been scheduled
    for cate in range(categories):
        if not visited[cate]:
            # calculate the current product's idle time and its ending time of each production line
            end_time_tmp = []
            for line in range(production_lines):
                end_time_tmp.append([0])
            curr_idle_time = 0
            for line in range(production_lines):
                if line == 0:
                    end_time_tmp[line][0] = end_time_base[line][0] + production_time[line][cate]
                else:
                    end_time_tmp[line][0] = max(end_time_tmp[line-1][0], end_time_base[line][0]) + production_time[line][cate]
                if line + 1 < production_lines and end_time_tmp[line][0] > end_time_base[line+1][0]:
                    curr_idle_time += end_time_tmp[line][0] - end_time_base[line+1][0]
            # maintain the minimum idle time and its respective complete time, product order
            if curr_idle_time < min_idle_time:
                for line in range(production_lines):
                    min_end_time[line][0] = end_time_tmp[line][0]
                min_idle_time = curr_idle_time
                cache[0] = end_time_tmp[-1][0]
                cache[1] = cate

    # update the base ending time of each production line, total idle time, complete time, product order
    end_time_base = min_end_time
    total_idle_time += min_idle_time
    complete_time.append(cache[0])
    product_order.append(cache[1])
    visited[cache[1]] = 1

# print the answer
for cate in range(categories):
    print(complete_time[product_order.index(cate)], end=",")
print(total_idle_time)
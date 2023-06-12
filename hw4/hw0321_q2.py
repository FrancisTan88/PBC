# read the input data
categories = int(input())
assemble_time = [int(i) for i in input().split(",")]
package_time = [int(i) for i in input().split(",")]

# sort by the priority according to the problem, and for every element in the array: (complete time, assemble time, order)
sorted_arr = [(assemble_time[i] + package_time[i], assemble_time[i], i) for i in range(categories)]
sorted_arr = sorted(sorted_arr, key=lambda x: (x[0], x[1], x[2]))

# create the new assemble time and package time, and build up a hashmap to enable to print the answer in correct order later
sorted_assemble_time = []
sorted_package_time = []
hashmap = {}
idx = 0
for ct, at, order in sorted_arr:
    sorted_assemble_time.append(assemble_time[order])
    sorted_package_time.append(package_time[order])
    hashmap[order] = idx  
    idx += 1

# calculate the wasted time of each producing process
wasted_time = []
complete_time = [sorted_assemble_time[0] + sorted_package_time[0]]
accumulate_assemble, accumulate_package = 0, 0
for i in range(1, len(sorted_assemble_time)):
    accumulate_assemble += sorted_assemble_time[i]
    accumulate_package += sorted_package_time[i-1]
    if accumulate_assemble > accumulate_package:
        wasted_time.append(accumulate_assemble - accumulate_package)
        accumulate_package += accumulate_assemble - accumulate_package
    else:
        wasted_time.append(0)

# calculate the complete time of each product and add up the total wasted time
total_wasted = sorted_assemble_time[0]
for i in range(1, categories):
    complete_time.append(complete_time[i-1] + wasted_time[i-1] + sorted_package_time[i])
    total_wasted += wasted_time[i-1]

# print the answer
for i in range(categories):
    print(complete_time[hashmap[i]], end=",")
print(total_wasted)



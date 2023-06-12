# read the input data
categories = int(input())
assemble_time = [int(i) for i in input().split(",")]
package_time = [int(i) for i in input().split(",")]

# calculate the wasted time of each producing process
wasted_time = []
complete_time = [assemble_time[0] + package_time[0]]
accumulate_assemble, accumulate_package = 0, 0
for i in range(1, len(assemble_time)):
    accumulate_assemble += assemble_time[i]
    accumulate_package += package_time[i-1]
    if accumulate_assemble > accumulate_package:
        wasted_time.append(accumulate_assemble - accumulate_package)
        accumulate_package += accumulate_assemble - accumulate_package
    else:
        wasted_time.append(0)

# calculate the complete time of each product and add up the total wasted time
total_wasted = assemble_time[0]
for i in range(1, categories):
    complete_time.append(complete_time[i-1] + wasted_time[i-1] + package_time[i])
    total_wasted += wasted_time[i-1]

# print the answer
for i in range(categories):
    print(complete_time[i], end=",")
print(total_wasted)


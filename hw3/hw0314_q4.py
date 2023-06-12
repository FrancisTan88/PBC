# read the input data
categories, days, productivity_pineapple, productivity_yellow = [int(i) for i in input().split(",")]
pineapple_by_categories = [int(i) for i in input().split(",")]
yellow_by_categories = [int(i) for i in input().split(",")]
demands = [[int(i) for i in input().split(",")] for j in range(categories)]

# calculate the daily labors for two products
for i in range(days):
    pineapple, yellow = 0, 0
    # calculate the daily demands for two products
    for j in range(len(demands)):
        pineapple += pineapple_by_categories[j] * demands[j][i]
        yellow += yellow_by_categories[j] * demands[j][i]
    # if remainder exists, note that we have to plus one to get the correct labors because of the integer division operator
    labor_pineapple = pineapple // productivity_pineapple if not pineapple % productivity_pineapple \
        else pineapple // productivity_pineapple + 1
    labor_yellow = yellow // productivity_yellow if not yellow % productivity_yellow \
        else yellow // productivity_yellow + 1
    print(labor_pineapple + labor_yellow, end=",") if i < days - 1 else print(labor_pineapple + labor_yellow)
# read the input data
days, productivity_pineapple, productivity_yellow = [int(i) for i in input().split(",")]
cases_phoenix = [int(i) for i in input().split(",")]
cases_tradition = [int(i) for i in input().split(",")]

# calculate the daily labors for two products
for i in range(days):
    pineapple = 4 * cases_phoenix[i] + 3 * cases_tradition[i]
    yellow = 2 * cases_phoenix[i] + 3 * cases_tradition[i]
    # if remainder exists, note that we have to plus one to get the correct labors because of the integer division operator
    labor_pineapple = pineapple // productivity_pineapple if not pineapple % productivity_pineapple \
        else pineapple // productivity_pineapple + 1
    labor_yellow = yellow // productivity_yellow if not yellow % productivity_yellow \
        else yellow // productivity_yellow + 1
    print(labor_pineapple + labor_yellow, end=",") if i < days - 1 else print(labor_pineapple + labor_yellow)
# read the data
days, increment, phoenix_firstday, tradition_firstday, yellow_produced, pineapple_produced \
    = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
# The daily calculation are as follows:
# "the number of cases" -> "the number of products" -> "the labors required to produce products"
for i in range(days):
    cases_phoenix = phoenix_firstday + increment * i
    cases_original = tradition_firstday + increment * i
    nums_yellow = 2 * cases_phoenix + 3 * cases_original
    nums_pineapple = 4 * cases_phoenix + 3 * cases_original
    # if remainder exists, note that we have to plus one to get the correct labors because of the integer division operator
    labor_yellow = nums_yellow // pineapple_produced if not nums_yellow % pineapple_produced else nums_yellow // pineapple_produced + 1
    labor_pineapple = nums_pineapple // yellow_produced if not nums_pineapple % yellow_produced else nums_pineapple // yellow_produced + 1
    print(labor_pineapple, end=",")
    print(labor_yellow)
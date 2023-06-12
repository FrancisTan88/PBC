# read the number of producing days
n = int(input())
# load the producing plan
bread = [int(input()) for i in range(n)]
# check if the plan is feasible, and if not, print the day that fails
count = 0
for i in range(n):
    count += bread[i]
    if count < 0:
        print(i+1)
        break
# print the remaining amount
if count >= 0: print(count)
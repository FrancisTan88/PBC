nums_class, standard = [int(i) for i in input().split(",")]
nums_people = [int(i) for i in input().split(",")]
nums_fill = [int(i) for i in input().split(",")]
rates = [[int(i) for i in input().split(",")] for j in range(nums_class)]

rate_fill = []
for i in range(len(nums_people)):
    rate_fill.append(100 * nums_fill[i] / nums_people[i])

max_score = float("-inf")

order = -1
students = -1
total_score = -1
for i in range(nums_class):
    if rate_fill[i] >= standard:
        curr_score = 0
        for j in range(len(rates[i])):
            curr_score += rates[i][j]
        curr_mean = curr_score / nums_fill[i]
        if curr_mean > max_score:
            order = i+1
            students = nums_people[i]
            total_score = curr_score
            max_score = curr_mean
if order != -1:
    print(f"{order},{students},{total_score}")
else:
    print(-1)







# ans = []
# for i in range(nums_class):
#     tmp = []
#     curr_fillrate = nums_people[i] / nums_fill[i]
#     if 100*curr_fillrate >= standard:
#         total_score = 0
#         for j in range(len(rates[i])):
#             total_score += rates[i][j]
#         curr_mean = total_score / nums_fill[i]
#         tmp.append(curr_mean)
#         tmp.append(i+1)
#         tmp.append(nums_people[i])
#         tmp.append(total_score)
#         ans.append(tmp)

# if not ans: 
#     print(-1)
# else:
#     ans = sorted(ans, key=lambda x: x[0], reverse=True)
#     print_ans = [ans[0]]
#     max_mean, order = ans[0][0], ans[0][1]
#     for i in ans:
#         if i[0] == max_mean and i[1] < order:
#             print_ans = [i]
#             order = i[1]
#     print(f"{order},{nums_people[order-1]},{}")


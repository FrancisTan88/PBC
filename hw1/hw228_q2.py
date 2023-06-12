# read the test data
x1, x2, y1, y2, p1, p2 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

# calculate the number of products
yellow = 2 * x1 + 3 * x2
pineapple = 4 * x1 + 3 * x2
tmp1, tmp2 = yellow, pineapple  # store the answer to return later
label1_yellow, label1_pineapple, label2 = 0, 0, 0

# calculate the number of label1
label1_yellow += yellow // y1
yellow %= y1
label1_pineapple += pineapple // y2
pineapple %= y2

# post processing
if (yellow > 0 and pineapple > 0) and ((yellow / y1 + pineapple / y2) <= 1):
    label2 += 1
else:
    if yellow > 0:
        label1_yellow += 1
    if pineapple > 0:
        label1_pineapple += 1
print(f"{tmp1},{tmp2},{label1_yellow},{label1_pineapple},{label2},{p1*(label1_yellow+label1_pineapple)+p2*label2}")
    


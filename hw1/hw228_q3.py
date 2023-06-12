# read the test data
x1, x2, y1, y2, p1, p2, r1, r2 = int(input()), int(input()), int(input()), int(
    input()), int(input()), int(input()), int(input()), int(input())

# calculate the number of products to be produced
yellow = 2 * x1 + 3 * x2
pineapple = 4 * x1 + 3 * x2
tmp1, tmp2 = yellow, pineapple  # store the answers to return later
total_payment = 0

# calculate the number of type1 labels(as many as possible) and the respective payment
if y1 <= yellow:
    total_payment += yellow // y1 * p1
    yellow %= y1
if y2 <= pineapple:
    total_payment += pineapple // y2 * p1
    pineapple %= y2

# if both products are left, according to the problem, employing two "type1 labors" is impossible
if yellow > 0 and pineapple > 0:
    minimum = p2 if p2 < r1*yellow+r2*pineapple else r1*yellow+r2*pineapple
    if p1 + r1 * yellow < minimum:
        minimum = p1 + r1*yellow
    if p1 + r2 * pineapple < minimum:
        minimum = p1 + r2 * pineapple
    total_payment += minimum

# if one of them (or both) is finished, note that no "type2 labors" are employed
else:
    if yellow > 0:
        total_payment += p1 if p1 < r1 * yellow else r1 * yellow
    if pineapple > 0:
        total_payment += p1 if p1 < r2*pineapple else r2*pineapple

# print the answer
print(tmp1, end=",")
print(tmp2, end=",")
print(total_payment)

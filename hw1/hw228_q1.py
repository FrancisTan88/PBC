# read the test data
x1, x2, y1, y2 = int(input()), int(input()), int(input()), int(input())
# calculate the number of products
yellow = 2 * x1 + 3 * x2
pineapple = 4 * x1 + 3 * x2
people1, people2 = 1, 1
# if no orders 
if yellow == 0 or pineapple == 0:
    people1 -= 1
    people2 -= 1
# calculate the labors
count = y1
while y1 < yellow:
    people1 += 1
    y1 += count
count = y2
while y2 < pineapple:
    people2 += 1
    y2 += count
print(f"{yellow},{pineapple},{people1},{people2}")

# read the input data
n = int(input()) 
pineapple, yellow = 0, 0
demands = [int(input()) for i in range(n)] 
y1, y2 = int(input()), int(input()) 
# calculate the number of products that need to be produced
for i in range(n):
    pineapple += (i+3)*demands[i]
    yellow += (i+1)*demands[i]
# calculate the labors we need
labor1 = pineapple//y1 if not pineapple % y1 else pineapple//y1 + 1 
labor2 = yellow//y2 if not yellow % y2 else yellow//y2 + 1
# print the answer
print(f"{pineapple},{yellow},{labor1},{labor2}")
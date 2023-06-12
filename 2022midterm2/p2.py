



hm = {
    0: "A",
    1: "B",
    2: "C"
}
read = [s.strip() for s in input().split(",")]
two_d = []
two_d.append(read[:3])
two_d.append(read[3:6])
two_d.append(read[6:9])
# print(two_d)
for i in range(3):
    for j in range(3):
        if two_d[i][j] == "":
            ans = False
            if two_d[i].count("x") == 2:
                ans = True
        
            count = 0
            for k in range(3):
                if two_d[k][j] == "x":
                    count += 1
            if count == 2: 
                ans = True

            if (i, j) == (0, 0):
                if two_d[1][1] == "x" and two_d[2][2] == "x":
                    ans = True
            if (i, j) == (0, 2):
                if two_d[1][1] == "x" and two_d[2][0] == "x":
                    ans = True
            if (i, j) == (2, 0):
                if two_d[1][1] == "x" and two_d[0][2] == "x":
                    ans = True
            if (i, j) == (2, 2):
                if two_d[1][1] == "x" and two_d[0][0] == "x":
                    ans = True
            if ans:
                print(hm[i] + str((j+1)))
                exit()

for i in range(3):
    for j in range(3):
        if two_d[i][j] == "":
            ans2 = False
            if two_d[i].count("o") == 2:
                ans2 = True
            
            count = 0
            for k in range(3):
                if two_d[k][j] == "o":
                    count += 1
            if count == 2: 
                ans2 = True
                
            if (i, j) == (0, 0):
                if two_d[1][1] == "o" and two_d[2][2] == "o":
                    ans2 = True
            if (i, j) == (0, 2):
                if two_d[1][1] == "o" and two_d[2][0] == "o":
                    ans2 = True
            if (i, j) == (2, 0):
                if two_d[1][1] == "o" and two_d[0][2] == "o":
                    ans2 = True
            if (i, j) == (2, 2):
                if two_d[1][1] == "o" and two_d[0][0] == "o":
                    ans2 = True
            if ans2:
                print(hm[i] + str((j+1)))
                exit()
print(-1)
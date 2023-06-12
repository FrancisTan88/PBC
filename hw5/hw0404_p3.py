def to_adj_mat(edges, n):
    if not edges:
        if n == 0:
            return None
        else:
            adj_matrix = [[0] * n for _ in range(n)]
            return adj_matrix
    max_node = max(list(map(max, edges)))
    if n == 0:
        adj_matrix = [[0] * (max_node+1) for _ in range(max_node+1)]
    else:
        if max_node + 1 > n:
            return None
        else:
            adj_matrix = [[0] * n for _ in range(n)]
    
    for i in edges:
        adj_matrix[i[0]][i[1]] = 1
        adj_matrix[i[1]][i[0]] = 1
    return adj_matrix
    

n = int(input())
edges = []
while True:
    curr = input().split(",")
    if curr[0] == "STOP":
        break
    curr[0] = int(curr[0])
    curr[1] = int(curr[1])
    edges.append(curr)

ans = to_adj_mat(edges, n)
if ans == None:
    print(None)
else:
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if j < len(ans[i])-1: print(ans[i][j], end=",")  
            else: print(ans[i][j])
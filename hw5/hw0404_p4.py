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

def find_closest(adj_matrix, k):
    if k >= len(adj_matrix):
        return None
    nums_common_adj = [-1] * len(adj_matrix)
    for i in range(len(adj_matrix)):
        if i == k:
            continue
        count = 0
        for j in range(len(adj_matrix)):
            if j != i and j != k:
                if adj_matrix[i][j] and adj_matrix[k][j]:
                    count += 1
        nums_common_adj[i] = count
    return nums_common_adj                

n = int(input())
k = int(input())
edges = []
while True:
    curr = input().split(",")
    if curr[0] == "STOP":
        break
    curr[0] = int(curr[0])
    curr[1] = int(curr[1])
    edges.append(curr)

ans = to_adj_mat(edges, n)
if ans is None:
    print("None")
else:
    nums = find_closest(ans, k)
    if nums is None:
        print("None")
    else:
        themost = max(nums)
        idx = nums.index(themost)
        print(idx)
        print(themost)




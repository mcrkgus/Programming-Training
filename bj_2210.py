graph = []
for j in range(5) :
    a = list(input().split())
    graph.append(a)

numlist = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, num) :
    num += graph[x][y]
    if len(num) == 6 : 
        if num not in numlist :
            numlist.append(num)
        return 
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<5 and 0<=ny<5 :
            dfs(nx, ny, num)

num = ""
for i in range(5) :
    for j in range(5) :
        dfs(i, j, num)

print(len(numlist))

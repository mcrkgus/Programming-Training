import sys
sys.setrecursionlimit(10**5)

N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
normal_count = 0
disabled_count = 0
for _ in range(N):
    graph.append(list(input().rstrip()))
    
xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]

def dfs(x, y) :
    visited[x][y] = True
    color = graph[x][y]        
    for i in range(4) :
        nx = x + xx[i]  
        ny = y + yy[i]
        if (0 <=nx < N) and (0 <= ny < N) :
            if visited[nx][ny] == False :   
                if graph[nx][ny] == color : 
                    dfs(nx, ny)
                    
for i in range(N) :
    for j in range(N) :
        if visited[i][j] == False :
            dfs(i, j)
            normal_count += 1            
print(normal_count)

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 'G' :
            graph[i][j] = 'R'
            
visited = [[False] * N for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        if visited[i][j] == False :
            dfs(i, j)
            disabled_count += 1  
print(disabled_count)

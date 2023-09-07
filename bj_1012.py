import sys
sys.setrecursionlimit(10000)
T = int(input())

def dfs(x, y) :
    dx = [-1, 1, 0, 0]  
    dy = [0, 0, -1, 1]
    
    for i in range(4) :
        nx = x+dx[i]    
        ny = y+dy[i]   
        if (0<=nx<M) and (0<=ny<N) and graph[ny][nx] == 1 :
            graph[ny][nx] = 0   
            dfs(nx, ny) 
            

for _ in range(T) :
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    
    for _ in range(K) :
        a, b = map(int, input().split())
        graph[b][a] = 1
    for i in range(M) :
        for j in range(N) :
            if graph[j][i] == 1 :
                dfs(i, j)
                cnt += 1

    print(cnt)

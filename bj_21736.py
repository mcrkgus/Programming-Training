import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
campus = []


for i in range(N) :
    r = list(input().rstrip())
    for j in range(M) :
        if r[j] == 'I' :
            start = [i, j]
    campus.append(r)
    
    
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]
cnt = 0



def dfs(x, y) :
    global cnt 
    
    if 0<=x<N and 0<=y<M and not visited[x][y]:
        visited[x][y] = True
        if campus[x][y] == 'P' :
            cnt += 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]  
            if 0<=nx<N and 0<=ny<M :
                if campus[nx][ny] != 'X' and not visited[nx][ny] :
                    dfs(nx, ny)
dfs(start[0], start[1])
            
      

if cnt > 0 : 
    print(cnt)
else :
    print('TT')

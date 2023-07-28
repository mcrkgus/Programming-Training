from collections import deque

M, N, K = map(int, input().split())
graph= [[0] * M for _ in range(N)]
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K) :
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx) :
        for j in range(ly, ry) :
            graph[i][j] = 1
            
def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1 
    area = 1
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if (-1<nx<N)  and (-1<ny<M) and (graph[nx][ny]) == 0 :
                graph[nx][ny] = 1
                queue.append((nx, ny))
                area += 1
    result.append(area)
    
    


for i in range(N) :
    for j in range(M) :
        if graph[i][j] ==  0 :
            bfs(i, j)


print(len(result))
result.sort()
for i in result:
    print(i, end=' ')

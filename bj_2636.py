from collections import deque
M, N = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(map(int,input().split())))

cheese = []
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]


def bfs() :
    queue = deque()
    queue.append([0, 0])
    

    visited[0][0] = True
    cnt = 0 

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<M) and (0<=ny<N) and visited[nx][ny] == 0 :
                if graph[nx][ny] == 0 : 
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                elif graph[nx][ny] == 1 :
                    graph[nx][ny] = 0   
                    cnt += 1
                    visited[nx][ny] = 1
    cheese.append(cnt)
    return cnt            
time = 0
while True :
    time += 1
    visited = [[0] * N for _ in range(M)]
    cnt = bfs()
    if cnt == 0 : break
print(time-1)
print(cheese[-2])

N = int(input())
graph = []
result = []
count = 0

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

xx = [0, 0, 1, -1]
yy = [1, -1, 0, 0]

def dfs(x, y) :
    
    global count
    if x < 0 or x >= N or y < 0 or y >= N:
       return 
    
    if graph[x][y] == 1 :
        count += 1
        graph[x][y] = 0
        for i in range(4) :
            nx = x + xx[i]
            ny = y + yy[i]
            dfs(nx, ny)

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()
print(len(result))
for i in result :
    print(i)

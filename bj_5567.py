
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
peer = []
cnt = 0
for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
for i in graph[1] :
    if not visited[i] :
        visited[i] = 1
        cnt += 1
    for j in graph[i] :
        if not visited[j] : 
            visited[j] = 1
            cnt += 1
print(cnt)

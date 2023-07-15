from collections import deque


N, M, V = map(int, input().split())
graph = {}
for i in range(N):
    graph[i+1] = []
for i in range(M) :
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    graph[a].append(b)
    
    if b not in graph:
        graph[b] = []
    graph[b].append(a)

for key in graph:
    graph[key].sort()


def BFS(graph, start, visited) :
    queue = deque([start])
    
    visited[start-1] = True
    
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i-1] :
                queue.append(i)
                visited[i-1] = True  
          
visited = [False] * N



visit = [False] * N
def DFS(graph, v, visit) :
    visit[v-1] = True
    print(v, end=' ')
    
    for i in graph[v] :
        if not visit[i-1] :
            DFS(graph, i, visit)



DFS(graph, V, visit)
print()
BFS(graph, V, visited)

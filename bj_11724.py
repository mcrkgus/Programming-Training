from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
def bfs(s) :
    queue = deque([s])
    visited[s] = True
    
    while queue : 
        v = queue.popleft()
        for i in graph[v] :
            if visited[i] == False :
                visited[i] = True 
                queue.append(i)
                
count = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1
    
print(count)

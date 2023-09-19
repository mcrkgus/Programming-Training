from collections import deque
cnt = 0
computer = int(input())
pair = int(input())
graph = [[] for i in range(computer+1)]

for i in range(pair) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    


visited = [False for _ in range(computer+1)]
visited[1] = True
    
def bfs(s) :
    global cnt 
    queue = deque([s])
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                cnt += 1 
                queue.append(i)
                visited[i] = True
bfs(1)
print(cnt)

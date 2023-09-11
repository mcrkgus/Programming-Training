import math

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
        
                 
N = int(input())
parent = [i for i in range(N+1)]

graph = []
for _ in range(N) :
    x, y = map(float, input().split())
    graph.append((x, y))
    

res = []
for i in range(N-1) :
    for j in range(i+1, N) :
        distance = math.sqrt((graph[i][0] - graph[j][0])**2 + (graph[i][1] - graph[j][1])**2)
        res.append((distance, i, j))
res.sort() 

sum = 0
for i in res :
    c, a, b = i
    if find(a) != find(b) :
        union(a, b)
        sum += c
sum = round(sum, 2)
print(sum)

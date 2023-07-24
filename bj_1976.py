import sys
def find(x) :
    if x == parent[x] :
        return x
    parent[x] =find(parent[x])  
    return parent[x]

def union(x, y) :
    x = find(x)
    y = find(y)
    if x == y :
        return 
    else : 
        parent[y] = x

N = int(input())
M = int(input())
parent = [0] * (N+1)

for i in range(1, N+1) :
    parent[i] = i

for i in range(1, N+1) :
    graph = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(graph)+1) :
        if graph[j-1] == 1 :
            union(i, j)
tour = list(map(int, sys.stdin.readline().split()))
res = set([find(i) for i in tour])

if len(res) == 1 :
    print("YES")
else :
    print("NO")
            

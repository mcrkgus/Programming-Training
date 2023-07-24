def find(x):
    if x == parent[x]:
      return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y :
        parent[y] = x
    else :
        parent[x] = y
        
N = int(input())
M = int(input())
arr = []
res = 0
parent =[i for i in range(N+1)]

for i in range(M) :
    a, b, c = map(int, input().split())
    arr.append((c, a, b))
    
arr.sort()

for i in arr :
    c, a, b = i
    if find(a) != find(b) :
        union(a, b)
        res += c
        
print(res)

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
    #그래프로 표현
    graph = list(map(int, sys.stdin.readline().split()))
    #현재 도시와 연결되어 있는 도시를 확인
    for j in range(1, len(graph)+1) :
        if graph[j-1] == 1 :
            union(i, j) #두 개의 도시를 합집합으로 표현
#여행 계획
tour = list(map(int, sys.stdin.readline().split()))
#set()함수를 통해 합집합을 찾는다. 즉, 모든 도시가 연결되어 있는 지 확인
res = set([find(i) for i in tour])
if len(res) == 1 :
    print("YES")
else :
    print("NO")
            

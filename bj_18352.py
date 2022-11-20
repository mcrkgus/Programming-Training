from collections import deque
res = 0
N, M, K, X = map(int, input().split())
#N:도시의 개수 / M:도로의 개수 / K:거리 정보 / X:출발 도시 번호
load = [[] for _ in range(N+1)]

for i in range(M) :
    A, B = map(int, input().split())    #A에서 B로 이동
    load[A].append(B)
    
m = [-1] * (N+1) #모든 load -1로 초기화
m[X] = 0     #출발 지점 0으로   
queue = deque([X])  #X == start
print(queue)
while queue :
    v = queue.popleft()
    for i in load[v] :
        if m[i] == -1 :
            m[i] = m[v] + 1   #현재에서 +1 거리 증가 
            queue.append(i)
            
if K in m : #최댠 거리가 m안에 있다면
    for i in range(1, N+1) :
        if m[i] ==  K :
            res = i       #i값 그대로 출력
else :
    res = -1   #없으면 -1 출력
        
    
print(res)

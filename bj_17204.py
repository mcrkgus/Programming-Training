from collections import deque

N, K = map(int, input().split())
graph = [int(input()) for _ in range(N)]

def bfs(x) :
    q = deque([x])
    cnt = 0
    for _ in range(N) : #사람의 수만큼 반복해서 지목한 사람을 확인
        target = q.popleft()    
        cnt += 1
        
        if graph[target] ==  K :    #보성이면 cnt return 
            return cnt
        q.append(graph[target]) #지목한 번호를 다시 큐에 추가해서 반복
        
    return -1   #보성이가 없다면 -1 
   
    
print(bfs(0))

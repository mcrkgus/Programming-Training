
from collections import deque

def bfs() :
    queue = deque()
    queue.append(home)
    while queue :
        x, y = queue.popleft()
        if abs(x - destination_x) + abs(y - destination_y) <= 1000 : 
            print("happy")
            return 
        else :
            for i in range(n) :
                if visited[i] == False :
                    nx, ny = market[i]
                    if abs(x - nx) + abs(y - ny) <= 1000 :
                        queue.append(market[i])
                        visited[i] = True
    print("sad")
    return 

 
t = int(input())

for _ in range(t) :
    n = int(input())
    home = list(map(int, input().split()))
    market = []
    for _ in range(n) :
        x, y = map(int, input().split())
        market.append((x, y))
    destination_x, destination_y = map(int, input().split())
    visited = [False for _ in range(n+1)]
    bfs()    
                

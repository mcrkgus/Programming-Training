from collections import deque
def solution(n, wires):
    answer = -1
    tree = [[] for _ in range(n+1)]

  # 연결된 간선 정보 tree리스트에 넣기 
    for a, b in wires :
        tree[a].append(b)
        tree[b].append(a)
        
    def bfs(s) :
        visited = [False] * (n+1)
        queue = deque([s])
        visited[s] = True
        cnt = 1
        while queue : 
            s = queue.popleft()
            for i in tree[s] :
                if not visited[i] :
                    visited[i] = True
                    queue.append(i)
                    cnt += 1
        return cnt
    
    res = n

    for a, b in wires :
        # 연결된 간선을 일단 하나 지우고 
        tree[a].remove(b)
        tree[b].remove(a)

        # 송전탑의 개수 (절대값) 중에서 최소값을 계속 갱신하기
        res = min(abs(bfs(a)-bfs(b)), res)

        # 끊었던 간선을 다시 이어 붙이기 
        tree[a].append(b)
        tree[b].append(a)

    return res

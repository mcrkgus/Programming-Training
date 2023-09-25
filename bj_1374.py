import sys
import heapq
input = sys.stdin.readline


N = int(input())
c = []
for i in range(N) :
    num, s, e = map(int, input().split())
    c.append([num, s, e])
    
c.sort(key=lambda x : (x[1], x[2]))

classroom = []

cnt = 0
for i in c:
    while classroom and classroom[0] <= i[1]:  # 가장 일찍 끝나는 시간보다 시작 시간이 크면
        heapq.heappop(classroom)       # classroom에서 가장 작은 원소 pop & return
    heapq.heappush(classroom, i[2])    # classroom에 i[2]=끝나는 시간을 추가
    cnt = max(cnt, len(classroom))

print(cnt)

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T) :
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    p.sort()
    
    t = 0
    cnt = 1
    
    for x in range(1, N) :
        if (p[x][1] < p[t][1]) :
            t = x
            cnt += 1
    print(cnt)

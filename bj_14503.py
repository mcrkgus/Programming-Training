N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = []
for _ in range(N) :
    room.append(list(map(int, input().split())))
    
visited = [[False]*M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

room[r][c] = -1
cnt = 1
while room[r][c] != 1 :
    flag = False
    for _ in range(4) :
        d -= 1
        if d == -1 :
            d = 3  
        nr = r + dr[d]
        nc = c + dc[d]
        if room[nr][nc] == 0 : 
            r = nr
            c = nc
            room[r][c] = -1
            cnt += 1
            flag = True
            break
    if not flag :
        r += dr[d-2]
        c += dc[d-2]
        
print(cnt)

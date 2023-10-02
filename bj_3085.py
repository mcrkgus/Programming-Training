def candy_count() :
    cnt, max_cnt = 1, 1
    res = 0 
    
    #행 기준 탐색
    for i in range(N) :
        cnt = 1
        for j in range(1, N) :
            if board[i][j] == board[i][j-1] :   #인접한 보드와 색이 같다면 
                cnt += 1
            else :
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    
    #열 기준 탐색 
        for j in range(1, N) :
            if board[j][i] == board[j-1][i] :   #인접항 보드와 색이 같다면 
                cnt += 1
            else :
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    
    res = max(max_cnt, cnt)
    return res   


N = int(input())
board = [list(input()) for _ in range(N)]

res = 1
for i in range(N) :
    for j in range(N-1) :
        if j+1 < N and board[i][j] != board[i][j+1] :
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            res = max(res, candy_count())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i+1 < N and board[i][j] != board[i+1][j] :
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            res = max(res, candy_count())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            
        
print(res)

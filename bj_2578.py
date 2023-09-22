bingo = [list(map(int, input().split())) for _ in range(5)]
mc = []
for i in range(5) :
    mc+= list(map(int, input().split()))


def check () :
    cnt = 0
    #가로
    for i in bingo :
        if i.count(0) == 5 :
            cnt += 1
            
    #세로
    for i in range(5) :
        y = 0
        for j in range(5) :
            if bingo[j][i] == 0 :
                y += 1
        if y == 5 : cnt += 1
    
    #오른쪽 대각선
    right = 0
    for i in range(5) :
        if bingo[i][i] == 0 :
            right += 1

    if right == 5 :
        cnt += 1
    
    #왼쪽 대각선
    left = 0
    for i in range(5) :
        if bingo[i][4-i] == 0 :
            left += 1
    
    if left == 5 :
        cnt += 1
    
    
    return cnt


count = 0 
for i in range(25) :
    for j in range(5) :
        for k in range(5) :
            if mc[i] == bingo[j][k] :
                bingo[j][k] = 0     #사회자에게 불리면 0으로 바꾸고 
                count += 1
    if count >= 12:
        result = check()
        
        if result >= 3 :
            print(i+1)
            break

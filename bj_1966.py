TC = int(input()) 

for i in range(TC) :
    N, M = map(int, input().split())    
    important = list(map(int, input().split())) 
    index_paper = [i for i in range(N)]   
    cnt = 0
    
    while True :
        if important[0] == max(important) : 
            cnt += 1    
            if index_paper[0] == M :    
                print(cnt) 
                break 
            else : 
                del important[0]    
                del index_paper[0]
        else : 
            important.append(important[0])  
            del important[0]
            index_paper.append(index_paper[0])
            del index_paper[0]
            
    

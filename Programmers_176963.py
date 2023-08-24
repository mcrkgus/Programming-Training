def solution(name, yearning, photo):
    score = 0
    score_list = []
    info = {}
    for i in range(len(name)) :
        info[name[i]] = yearning[i] 
        #info를 딕셔너리로 하고 name과 yearning을 넣음
    
    for i in range(len(photo)) :
        score = 0
        for j in range(len(photo[i])) :
            if photo[i][j] in info :  #photo에 있는 사람의 이름이 info에 있으면
                score += info[photo[i][j]]  #info의 yearning 값을 score에 저장
        score_list.append(score)    #list형태로 저장 
    return score_list
            

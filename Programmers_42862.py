def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    # for i in reserve : 
    #     if i in lost :
    #         reserve.remove(i)
    #         lost.remove(i)
    new_lost = []
    for x in lost:
        if x in reserve:    # lost의 원소 x가 reserve에 있다면
            reserve.remove(x)
        else:
            new_lost.append(x)
    lost = new_lost

    
    for i in reserve :
        if (i-1) in lost : 
            lost.remove(i-1)

        elif (i+1) in lost :
            lost.remove(i+1)

    answer = n - len(lost)
    return answer

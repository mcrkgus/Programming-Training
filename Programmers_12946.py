def solution(n):
    answer = []
    def hanoi(n, start, end, mid) :
        #start:시작 기둥 / end:보낼기둥 / mid:중간에 보조로 사용할 기둥
        if n == 1 : 
            answer.append([start, end])
            return answer
        hanoi(n-1, start, mid, end)
        answer.append([start, end])
        hanoi(n-1, mid, end, start)
    hanoi(n, 1, 3, 2)

    return answer 

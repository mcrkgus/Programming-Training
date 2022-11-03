from collections import deque
def solution(people, limit):
    answer = 0
    l = deque(sorted(people))
    while l :
        if len(l) == 1 :
            answer += 1
            break
        if l[0] + l[-1] <= limit :
            l.pop()         #right
            l.popleft()     #left
        else :
            l.pop()
        answer += 1
    return answer

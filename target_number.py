def solution(numbers, target):
    answer = [0]
    def dfs(i, n, l) :
        if i == len(l) :
            if n == target :
                answer[0] += 1
            return 
        v = l[i]
        dfs(i + 1, n + v, l)
        dfs(i + 1, n - v, l)    
    dfs(0, 0, numbers)
    
    return answer[0]

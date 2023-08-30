def solution(numbers):
    stack = []  # 숫자들을 저장할 스택
    answer = [-1] * len(numbers)  # 결과 리스트를 -1로 초기화
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]  # 더 큰 숫자를 발견하면 스택에서 팝하며 결과를 갱신
        
        stack.append(i)  # 현재 인덱스를 스택에 추가
    
    return answer



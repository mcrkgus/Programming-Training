def solution(numbers):
    answer = ''
    total_number = list(map(str, numbers))   
    total_number.sort(key=lambda x: x*3, reverse=True)

    for i in total_number : 
        answer+=i

    return str(int(answer))

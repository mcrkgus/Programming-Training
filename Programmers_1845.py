def solution(nums):
    answer = 0
    select = len(nums)//2
    re_nums = set(nums) #nums에서 중복 제거 

    if select > len(list(re_nums)) :
        answer = len(list(re_nums))
    else : 
        answer = select
        
    return answer


class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0 :
            return [0]
        if n == 1 :
            return [0, 1]
      
        memo = [0] * (n + 1) 
        for number in range(1, n + 1):  
            memo[number] = memo[number >> 1] 
            if number % 2 == 1:     
                memo[number] += 1 
        
        return memo
    

class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {} 
        
        def memoization(n):
            if n in memo: 
                return memo[n]
            if n == 1:
                return 0
            
            if n % 2 == 0 :
                memo[n] = 1 + memoization(n / 2)
            else:
                memo[n] = 1 + min(memoization(n+1), memoization(n-1))                
            return memo[n]        
        return memoization(n)

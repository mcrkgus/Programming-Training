class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        val = 0 
        res = 0
        n = len(values)
        
        
        for i in range (n) :
            res = max(res, val + values[i] - 1)
            val = max(val - 1, values[i])
        return res

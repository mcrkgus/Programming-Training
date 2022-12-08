class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(indx,path):
            if indx == len(nums):
                res.append(path)
                return
            backtrack(indx+1,path + [nums[indx]])
            backtrack(indx+1,path)
            
        backtrack(0,[])
        return res

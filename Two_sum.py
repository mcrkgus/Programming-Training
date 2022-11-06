class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l == 2 :
            return [0, 1]
            
        dict1 = {}
    
        for i in range(l):
            if target - nums[i] in dict1:
                return [i, dict1[target-nums[i]]]
            
            dict1[nums[i]] = i

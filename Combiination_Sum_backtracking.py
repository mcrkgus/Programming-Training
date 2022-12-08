def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    track = []

    self.trackSum = 0

    def backtrack(nums, start, target):
        
        if self.trackSum == target:
            res.append(list(track))
            return

        if self.trackSum > target:
            return

        for i in range(start, len(nums)):
            self.trackSum += nums[i]
            track.append(nums[i])
            backtrack(nums, i, target)
            track.pop(-1)
            self.trackSum -= nums[i]
            
    backtrack(candidates, 0, target)
    return res

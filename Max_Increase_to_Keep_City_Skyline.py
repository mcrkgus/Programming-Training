class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        l1 = len(grid)
        l2 = len(grid[0])
        r = [0] * l1
        c = [0] * l2

        for i in range(l1):
            for j in range(l2):
                r[i] = max(r[i], grid[i][j])
                c[j] = max(c[j], grid[i][j])

        res = 0

        for i in range(l1):
            for j in range(l2):
                res += (min(r[i], c[j]) - grid[i][j])

        return res

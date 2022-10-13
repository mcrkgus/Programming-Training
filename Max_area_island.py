class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if not grid:
            return 0
        area, count = 0, 0

        def dfs(i,j):
            nonlocal count 
            nonlocal m, n
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] != 1:
                return count
            if grid[i][j] == 1:
                count += 1
            grid[i][j] = '#'
            dfs(i+1,j)  #우
            dfs(i-1,j)  #좌
            dfs(i,j-1)  #하
            dfs(i,j+1)  #상

        for i in range(m):
            for j in range(n):
                dfs(i,j)
                area = max(count,area)
                count = 0
        return area

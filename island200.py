class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        check = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, grid):
            row = len(grid)
            col = len(grid[0])
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for val in check:
                dfs(r+val[0], c+val[1], grid)        
        
        newI = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    newI += 1
                    dfs(i, j, grid)
        return newI
        
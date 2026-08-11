class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int: 
        r = len(grid) 
        c = len(grid[0])
        count = 0
        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == 1:
                    count += 4  
                    if i-1>=0 and grid[i-1][j] == 1:
                        count -= 2 
                    if j-1>=0 and grid[i][j-1] == 1:
                        count -= 2 
        return count
        
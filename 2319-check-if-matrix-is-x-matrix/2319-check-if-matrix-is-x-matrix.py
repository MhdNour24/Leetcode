class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if i==j or i==n-j-1:
                    if grid[i][j]==0:
                        return False 

                else:
                    if grid[i][j]!=0:
                        return False
        return True
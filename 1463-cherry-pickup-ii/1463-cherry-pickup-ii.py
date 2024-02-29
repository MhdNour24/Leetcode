class Solution(object):
    def cherryPickup(self, grid):

        rows, cols = len(grid), len(grid[0])
        
        # Define a memoization dictionary to store already calculated results
        memo = {}
        
        def dp(r, c1, c2):
            # Base case: If robots go out of bounds or reach the top row, return 0
            if r == rows or c1 < 0 or c1 == cols or c2 < 0 or c2 == cols:
                return 0
            
            # Check if the result for this state has already been calculated
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]
            
            # Collect cherries from the current cells
            cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
            
            # Calculate the maximum cherries collected by both robots in the next row
            max_cherries = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    max_cherries = max(max_cherries, dp(r + 1, c1 + dc1, c2 + dc2))
            
            # Add the cherries collected from the current cell to the maximum cherries from the next row
            result = cherries + max_cherries
            
            # Memoize the result
            memo[(r, c1, c2)] = result
            
            return result
        
        # Start the dynamic programming process from the top row and return the result
        return dp(0, 0, cols - 1)
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1): # Loop Through All Rows
		# Check if shifting correct
            if matrix[i][:-1]==matrix[i+1][1:]: 
                continue
            else:
                return False
        return True
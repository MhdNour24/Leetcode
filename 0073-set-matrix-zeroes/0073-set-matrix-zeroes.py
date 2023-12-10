from numpy.random import randint as ra
class Solution(object):
    def __init__(self):
        self.indexler=[]
    def aramak(self,matrix,i,j):
        for o in range(len(matrix[0])):
            if matrix[i][o]==0:
                continue
            matrix[i][o]=0
            self.indexler.append((i,o))
        for u in range(len(matrix)):
            if matrix[u][j]==0:
                continue
            matrix[u][j]=0
            self.indexler.append((u,j))        
    def setZeroes(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in self.indexler:
                    if matrix[i][j]==0:
                        self.aramak(matrix,i,j)

        return matrix
        
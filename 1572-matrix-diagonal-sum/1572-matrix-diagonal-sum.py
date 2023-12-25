class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        toplam=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if (i-j)==0:
                    toplam+=mat[i][j]
                elif i+j ==len(mat)-1:
                    toplam+=mat[i][j]
        return toplam
                
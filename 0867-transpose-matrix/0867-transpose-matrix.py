class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        Transpose_Matrix=[]
        for i in range(len(matrix[0])):
            column=[matrix[j][i]for j in range(len(matrix))]
            Transpose_Matrix.append(column)
        return Transpose_Matrix
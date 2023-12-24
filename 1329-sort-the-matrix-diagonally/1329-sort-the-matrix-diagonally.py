class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort(mat,i,j):
            while i<len(mat) and j<len(mat[0]):
                oi=i+1
                oj=j+1
                while oi<len(mat) and oj<len(mat[0]):
                    if mat[i][j]>mat[oi][oj]:
                        mat[i][j],mat[oi][oj]=mat[oi][oj],mat[i][j]
                    oi+=1
                    oj+=1
                i+=1
                j+=1
                
        for i in range(len(mat[0])):
            sort(mat,0,i)
        for j in range(1,len(mat)):
            sort(mat,j,0)
        return mat
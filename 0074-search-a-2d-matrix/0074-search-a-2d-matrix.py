class Solution(object):
    def binary_sort(self,liste,value):
        l=0
        h=len(liste)-1
        while l<=h:
            m=(l+h)//2
            if liste[m]==value:
                return True
            elif liste[m]<value:
                l=m+1
            else:
                h=m-1
        return False
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if self.binary_sort(matrix[i],target)==True:
                return True
        return False
            
class Solution(object):
    def __init__(self):
        self.liste=[]
    def diyagonal(self,mat,i,j,t):
        if t%2==1:
            while i<len(mat) and j>=0:
                self.liste.append(mat[i][j])
                i+=1
                j-=1
        elif t%2==0:
            k=[]
            while i<len(mat) and j>=0:
                k.append(mat[i][j])
                i+=1
                j-=1
            self.liste.extend(k[::-1])
            
    def findDiagonalOrder(self, mat):
        c=0
        for j in range(len(mat[0])):
            self.diyagonal(mat,0,j,c)
            c+=1
        for i in range(1,len(mat)):
            self.diyagonal(mat,i,len(mat[0])-1,c)
            c+=1
                
        return self.liste
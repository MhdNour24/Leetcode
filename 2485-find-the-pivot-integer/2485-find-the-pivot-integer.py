class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        toplam=int(n*(n+1)/2)
        for i in range(1,n):
            k=int(i*(i+1)/2)
            if k == toplam-k+i:
                return i 
        return -1
class Solution:
    def toplam(self,num):
        return int(num*(num+1)/2)
    def pivotInteger(self, n: int) -> int:
        for i in range(n+1):
            if self.toplam(i)==self.toplam(n)-self.toplam(i-1):
                return i
        return -1
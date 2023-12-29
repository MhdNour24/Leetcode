class Solution(object):
    def findGCD(self, nums):
        smallest=min(nums)
        largest=max(nums)
        ortak_bolen=1
        for i in range(2,smallest+1):
            if smallest%i==0 and largest%i==0:
                ortak_bolen=i
        return ortak_bolen
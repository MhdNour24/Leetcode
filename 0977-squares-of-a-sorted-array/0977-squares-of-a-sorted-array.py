class Solution(object):
    def sortedSquares(self, nums):
        kare_liste=list(map(lambda x:(x)**2,nums))
        return sorted(kare_liste)
        
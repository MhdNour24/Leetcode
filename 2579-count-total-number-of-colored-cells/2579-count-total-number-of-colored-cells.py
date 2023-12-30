class Solution:
    def coloredCells(self, n: int) -> int:
        return pow(n-1,2)*2+n*2-1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=0
        b=0
        for i in gain:
            a+=i
            b=max(b,a)
        return b

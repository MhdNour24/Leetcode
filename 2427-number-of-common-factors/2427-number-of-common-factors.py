class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        s=1
        while s<=a and s<=b:
            if a%s==0 and b%s==0:
                count+=1
            s+=1
        return count
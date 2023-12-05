class Solution:
    def numberOfMatches(self, n: int) -> int:
        count=0
        while n!=1:
            a,b=divmod(n,2)
            count+=a
            n=a+b
        return count
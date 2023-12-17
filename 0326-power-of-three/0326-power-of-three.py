class Solution:
    def isPowerOfThree(self, n: int,k=0) -> bool:
        if 3**k==n:
            return True
        elif 3**k>n:
            return False
        else:
            k+=1
            return self.isPowerOfThree(n,k)
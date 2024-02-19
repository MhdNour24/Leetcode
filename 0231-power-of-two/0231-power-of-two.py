class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n%2==1:
            return False
        if n==0:
            return False
        while True:
            n,kalan=divmod(n,2)
            if kalan!=0:
                return False
            if n==1 and kalan==0:
                return True
            if n==1 and kalan!=0:
                return False
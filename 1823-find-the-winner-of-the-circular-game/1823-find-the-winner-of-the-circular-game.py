class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends=list(range(1,n+1))
        a=0
        while n!=1:
            index=(a+k)%n-1
            if index<0:
                index=n-1
            del friends[index]
            a=index
            n-=1
        return friends[0]

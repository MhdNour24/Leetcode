class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k=2*n-2
        time=time%(k)
        if time>=n:
            # time=time-n+1
            time = k+1-time
            return time
        return time+1
class Solution:
    def addRungs(self, rungs, dist):
        rungs.insert(0,0)

        n, total = len(rungs), 0 

        for i in range(1,n):
            val = rungs[i]-rungs[i-1]
            total += (val-1)//dist

        return total
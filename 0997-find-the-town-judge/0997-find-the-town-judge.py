class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic=defaultdict(int)
        if n==1 and not trust:
            return 1
        for i in trust:
            a,b=i
            dic[b]+=1

        for j in trust:
            a,b=j
            if a in dic:
                del dic[a]
        
        for key,value in dic.items():
            if value==n-1:
                return key
        return -1
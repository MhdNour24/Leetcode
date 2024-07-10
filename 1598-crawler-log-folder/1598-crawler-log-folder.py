class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter=0
        for log in logs:
            if log=="./":
                pass
            elif log=="../":
                if counter==0:
                    pass
                else:
                    counter-=1
            else:
                counter+=1
        return counter
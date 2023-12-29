class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        size=len(s)
        result=[]
        c=0
        count,remainder=divmod(size,k)
        for i in range(0,count):
            result.append(s[c:c+k])
            c+=k
        if remainder!=0:
            result.append(s[c:]+fill*(k-remainder))
        return result
        



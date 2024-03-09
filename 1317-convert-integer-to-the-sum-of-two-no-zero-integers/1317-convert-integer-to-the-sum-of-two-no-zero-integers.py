class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a=1
        b=n-1
        while True:
            result=True
            for i in str(a):
                if i=="0":
                    a+=1
                    b-=1
                    result=False
                    break
            for j in str(b):
                if j=="0":
                    a+=1
                    b-=1
                    result=False
                    break
            if result:
                break
        return [a,b]

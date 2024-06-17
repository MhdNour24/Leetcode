class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(pow(c,1/2))
        for i in range(b+1):
            top=pow(a,2)+pow(b,2)
            if top<c:
                a+=1
            elif top>c:
                b-=1
            else:
                return True
        return False
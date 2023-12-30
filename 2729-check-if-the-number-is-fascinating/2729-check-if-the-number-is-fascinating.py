class Solution:
    def isFascinating(self, n: int) -> bool:
        n=int(str(n)+str(n*2)+str(n*3))
        liste=[]
        while n:
            last_digit=n%10
            n=n//10
            if last_digit==0 or last_digit in liste:
                return False
            else:
                liste.append(last_digit)
        return True
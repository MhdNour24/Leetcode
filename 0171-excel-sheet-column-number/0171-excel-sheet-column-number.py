class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum=0
        dic={}
        number=1
        for i in range(ord("A"),ord("Z")+1):
            dic[chr(i)]=number
            number+=1
        
        c=0
        for i in columnTitle[::-1]:
            sum+=26**c*dic[i]
            c+=1
        return sum
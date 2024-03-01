class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        number_1=0
        number_0=0
        for i in s:
            if int(i)==1:
                number_1+=1
            else:
                number_0+=1
        new_bin=""
        new_bin+="1"*(number_1-1)+"0"*(number_0)+"1"
        return new_bin
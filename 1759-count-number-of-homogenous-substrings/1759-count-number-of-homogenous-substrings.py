import numpy as np
class Solution:
    def countHomogenous(self, s: str) -> int:
        counter=0
        length=len(s)
        last_char=None
        count=0
        for i in range(length):
            if i==0:
                count=1
                last_char=s[i]
            else:
                if s[i]==last_char:
                    count+=1
                else:
                    last_char=s[i]
                    count=1
            counter+=count
        return counter%(np.power(10,9)+7)

class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum_s=0
        c=0
        length=len(s)
        while c<length:
            if c==length-1:
                sum_s+=dic[s[c]]
                c+=1
                break
            if dic[s[c]]<dic[s[c+1]]:
                sum_s+=(dic[s[c+1]]-dic[s[c]])
                c+=2
            else:
                sum_s+=dic[s[c]]
                c+=1
        
        return sum_s
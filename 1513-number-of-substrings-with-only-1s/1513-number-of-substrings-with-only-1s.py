class Solution:
    def numSub(self, s: str) -> int:
        length=len(s)
        c=1
        counter=0
        for i in range(length):
            if s[i]=="1":
                counter+=c
                c+=1
            elif s[i]=="0":
                c=1
        return counter % (10**9 + 7)
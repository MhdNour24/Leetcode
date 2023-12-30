class Solution:
    def sum_number(self,number):
        return  sum(list(map(int,"".join(number))))
    def digitSum(self, s: str, k: int) -> str:
        size=len(s)
        if size<=k:
            return s
        list_digit=[]
        while s:
            if size>=k:
                number=s[:k]
                s=s[k:]
                size-=k
            else:
                number=s
                s=""
                size=0
            list_digit.append(str(self.sum_number(number)))
        new_s="".join(list_digit)
        return self.digitSum(new_s,k)
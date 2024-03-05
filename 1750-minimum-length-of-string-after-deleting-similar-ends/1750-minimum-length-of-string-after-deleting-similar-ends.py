class Solution:
    def get_prefix(self,s):
        index=0
        last_char=s[0]
        for char in s[1:]:
            if char==last_char:
                index+=1
            else:
                break
        return index
    def get_suffix(self,s):
        index=-1
        last_char=s[-1]
        for char in s[::-1][1:]:
            if char==last_char:
                index-=1
            else:
                break
        return index

    def minimumLength(self, s: str) -> int:
        length=len(s)
        while True:
            if length>1:
                index_pre=self.get_prefix(s)
            if length>1:
                index_suf=self.get_suffix(s)
            else:
                break
            if (index_pre+1)==length:
                length=0
                break
            if s[index_pre]==s[index_suf]:
                s=s[index_pre+1:]
                s=s[:index_suf]
                length-=int(abs(index_suf)+index_pre+1)
            else:
                break
        return length
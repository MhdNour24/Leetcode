class Solution:
    def sortSentence(self, s: str) -> str:
        arr=s.split()
        arr=sorted(arr,key=lambda x:int(x[-1]))
        a=list(map(lambda x:x[:-1],arr))
        return " ".join(a)
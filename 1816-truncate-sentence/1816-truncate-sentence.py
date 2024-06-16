class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr=s.split()
        s=arr[:k]
        return " ".join(s)
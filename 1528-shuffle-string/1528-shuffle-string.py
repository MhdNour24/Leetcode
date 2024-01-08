class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        length=len(indices)
        new_s=[0]*length
        for i in range(length):
            new_s[indices[i]]=s[i]
        return "".join(new_s)
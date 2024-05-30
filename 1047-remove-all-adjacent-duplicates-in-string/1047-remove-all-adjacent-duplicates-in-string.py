class Solution:
    def removeDuplicates(self, s: str) -> str:
        liste=[]
        length=len(s)
        for i in range(length):
            char=s[i]
            if not liste:
                liste.append(char)
            else:
                last_char=liste[-1]
                if char==last_char:
                    liste.pop()
                else:
                    liste.append(char)
        return "".join(liste)
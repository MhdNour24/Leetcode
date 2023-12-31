class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        liste=[]
        for i,word in enumerate(words):
            for j in word:
                if j==x:
                    liste.append(i)
                    break
                    
        return liste
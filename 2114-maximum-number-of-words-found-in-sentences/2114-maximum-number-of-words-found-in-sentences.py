class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        enb=0
        for i in sentences:
            liste=i.split()
            enb=max(enb,len(liste))
        return enb

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        top=sum(chalk)
        k=k%top
        length=len(chalk)
        liste=[chalk[0]]
        if liste[-1]>k:
            return 0
        for i in range(1,length):
            value=chalk[i]
            liste.append(liste[-1]+value)
            if liste[-1]>k:
                return i
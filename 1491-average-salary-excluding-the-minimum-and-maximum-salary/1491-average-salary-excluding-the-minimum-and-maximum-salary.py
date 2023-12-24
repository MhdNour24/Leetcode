class Solution:
    def average(self, salary: List[int]) -> float:
        k=sorted(salary)
        liste=k[1:len(k)-1]
        return sum(liste)/len(liste)
        
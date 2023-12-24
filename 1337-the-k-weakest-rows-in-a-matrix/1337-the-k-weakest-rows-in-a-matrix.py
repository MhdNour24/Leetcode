class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        value_list=[]
        x=[]
        for i in range(len(mat)):
            liste=mat[i]
            value_list.append(sum(liste))
        l=len(value_list)
        for i in range(k):
            a=len(mat[0])+1
            for j in range(l):
                if value_list[j] !="_":
                    if value_list[j]<a  :
                        a=value_list[j]
                        y=j
            x.append(y)
            value_list[y]="_"


        return x
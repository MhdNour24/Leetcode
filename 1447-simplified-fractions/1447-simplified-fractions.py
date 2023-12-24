class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        liste=[]
        lst=[]
        for j in range(2,n+1):
            for i in range(1,j):
                deger=i/j
                print(deger)
                if deger not in liste:
                    liste.append(deger)
                    lst.append(f"{i}/{j}")
        return lst


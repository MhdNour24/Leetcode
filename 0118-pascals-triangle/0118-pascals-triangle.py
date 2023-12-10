class Solution:
    def __init__(self):
        self.liste=[]
    def toplam(self,top_liste):
        toplam=0
        for i in range(len(top_liste)):
            toplam+=top_liste[i]
        return toplam
    def generate(self, numRows):
        li=[1]
        self.liste.append(li)
        for i in range(numRows-1):
            lis=[1]
            for j in range(i):
                k=li[j:j+2]
                lis.append(self.toplam(k))
            lis.append(1)
            self.liste.append(lis)
            li=lis
        return self.liste
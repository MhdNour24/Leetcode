class Solution:
    def convert_binary(self,liste):
        kalan=0
        index=len(liste)-1
        t=1
        while True:
            last_number=liste[index]
            k=last_number+t+kalan
            kalan=0
            t=0
            if k==1:
                liste[index]=1
                break
            else:
                liste[index]=0
                index-=1
                kalan=1
            if index==-1 and kalan==1:
                liste.insert(0,1)
                break
        return liste
    def count_k(self,liste,k):
        count=0
        for i in liste:
            if i ==1:
                count+=1
        if count==k:
            return True
        return False
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        liste=[0]
        length=len(nums)
        c=0
        toplam=0
        while c<length:
            sonuç=self.count_k(liste,k)
            if sonuç:
                toplam+=nums[c]
            c+=1
            liste=self.convert_binary(liste)
        return toplam
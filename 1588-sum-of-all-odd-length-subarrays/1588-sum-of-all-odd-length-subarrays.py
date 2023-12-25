class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        t=1
        toplam=0
        while t<=len(arr):
            for i in range(0,len(arr)-t+1):
                liste=arr[i:i+t]
                toplam+=sum(liste)
            t+=2
        return toplam
                
        
        
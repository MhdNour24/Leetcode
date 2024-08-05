class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counting={}
        for i in range(len(arr)):
            if arr[i] not in counting:
                counting[arr[i]]=1
            else:
                counting[arr[i]]+=1
        counter=0
        liste=[]
        for value,count in counting.items():
            if count==1:
                counter+=1
                liste.append(value)
        if counter<k:
            return ""
        else:
            return liste[k-1]

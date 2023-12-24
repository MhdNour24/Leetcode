class Solution:
    def findLucky(self,arr):
        answer=-1
        first=0
        while first<len(arr):
            count=1
            t=first+1
            
            while t<len(arr):
                if arr[first]==arr[t]:
                    count+=1
                    del arr[t]
                else:
                    t+=1
            if arr[first]==count and count>answer:
                answer=count
            first+=1
        return answer
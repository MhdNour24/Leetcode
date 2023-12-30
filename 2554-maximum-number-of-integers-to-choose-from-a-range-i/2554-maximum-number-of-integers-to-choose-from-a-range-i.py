class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cnt = 0
        total = 0
        banned = set(banned)
        
        for i in range(1,n+1):
            if i not in banned and maxSum>=total+i:
                cnt+=1
                total+=i
        return cnt    

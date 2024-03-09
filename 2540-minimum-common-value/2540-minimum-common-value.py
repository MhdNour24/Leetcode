class Solution:
    def jumpSearch(self,arr , x , n ):
        
        # Finding block size to be jumped
        step = math.sqrt(n)
        
        # Finding the block where element is
        # present (if it is present)
        prev = 0
        while arr[int(min(step, n)-1)] < x:
            prev = step
            step += math.sqrt(n)
            if prev >= n:
                return -1
        
        # Doing a linear search for x in 
        # block beginning with prev.
        while arr[int(prev)] < x:
            prev += 1
            
            # If we reached next block or end 
            # of array, element is not present.
            if prev == min(step, n):
                return -1
        
        # If element is found
        if arr[int(prev)] == x:
            return prev
        
        return -1
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        len_nums1=len(nums1)
        for num in nums2:
            result=self.jumpSearch(nums1,num,len_nums1)
            if result!=-1:
                return nums1[int(result)]
        return -1
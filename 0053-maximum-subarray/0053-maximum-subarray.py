class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        max_sum = float('-inf')
        
        for num in nums:
            if curr_sum + num > 0:
                curr_sum += num
                max_sum = max(max_sum, curr_sum)
            else:
                curr_sum = 0
                
        return max_sum if max_sum != float('-inf') else max(nums)
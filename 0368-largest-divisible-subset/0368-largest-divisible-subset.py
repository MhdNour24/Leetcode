class Solution(object):
    def largestDivisibleSubset(self, nums):

        if not nums:
            return []
        
        nums.sort()  # Sort the numbers to simplify the problem
        
        # dp[i] stores the size of the largest divisible subset ending with nums[i]
        # parent[i] stores the index of the previous element in the largest divisible subset
        dp = [1] * len(nums)
        parent = [-1] * len(nums)
        
        max_index = 0  # index of the last element of the largest divisible subset
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > dp[max_index]:
                max_index = i
        
        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        
        return result[::-1]  # Return the subset in reverse order
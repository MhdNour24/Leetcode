

class Solution:
    def minOperations(self, nums , x) :

        # LC hint: find the maximum subarray greedily
        sum_nums = sum(nums)
        if sum_nums < x:
            return -1
        elif sum_nums == x:
            return len(nums)

        target = sum_nums - x
        max_len = 0
        beg = 0
        for i in range(len(nums)):
            while beg < i and target - nums[i] < 0:
                target += nums[beg]
                beg += 1
            target -= nums[i]
            if target == 0:
                max_len = max(max_len, i - beg + 1)

        return -1 if max_len == 0 else len(nums) - max_len
        
        
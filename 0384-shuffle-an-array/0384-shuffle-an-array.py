import random
class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.original = nums[:]

    def reset(self):
        # self.nums = self.original
        return self.original

    def shuffle(self):
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
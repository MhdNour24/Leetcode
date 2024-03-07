class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        nums_dict = {}
        count = 0

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        for num in nums_dict:
            if k == 0:
                if nums_dict[num] >= 2:
                    count += 1
            else:
                if num + k in nums_dict:
                    count += 1

        return count
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        temp = [(i+j, j, i) for i in range(len(nums)) for j in range(len(nums[i]))]
        temp.sort()
        return [nums[i][j] for _, j, i in temp]

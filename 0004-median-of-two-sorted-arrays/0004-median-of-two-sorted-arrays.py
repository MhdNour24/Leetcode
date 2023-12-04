class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum_nums=nums1+nums2
        sum_nums.sort()
        size_liste=len(sum_nums)
        if size_liste%2==1:
            return sum_nums[size_liste//2]
        else:
            return (sum_nums[size_liste//2] + sum_nums[(size_liste//2)-1])/2
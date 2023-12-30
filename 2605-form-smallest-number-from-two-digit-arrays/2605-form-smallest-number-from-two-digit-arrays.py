class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        min_value=int(str(nums1[0])+str(nums2[0]))
        min_nums2=min(nums2)
        for i in nums1:
            if i in nums2:
                min_value=min(i,min_value)
            else:
                new_number_1=str(i)+str(min_nums2)
                new_number_2=str(min_nums2)+str(i)

                min_value=min(min_value,int(new_number_1))
                min_value=min(min_value,int(new_number_2))
        return min_value
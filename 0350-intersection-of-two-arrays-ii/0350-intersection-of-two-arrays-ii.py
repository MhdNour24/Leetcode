class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic_nums1=defaultdict(int)
        dic_nums2=defaultdict(int)
        length_nums1=len(nums1)
        length_nums2=len(nums2)
        max_length=max(length_nums1,length_nums2)
        for i in range(max_length):
            if i<length_nums1:
                dic_nums1[nums1[i]]+=1
            if i<length_nums2:
                dic_nums2[nums2[i]]+=1
        new_lst=[]
        for item,value in dic_nums1.items():
            value2=dic_nums2[item]
            pure_value=None
            if value2>0:
                pure_value=min(value,value2)
                new_lst+=[item]*pure_value
        return new_lst


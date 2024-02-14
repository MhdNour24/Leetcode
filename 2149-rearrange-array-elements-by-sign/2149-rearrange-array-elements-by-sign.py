class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_liste=[]
        neg_liste=[]
        length=len(nums)
        for i in range(length):
            if nums[i]<0:
                neg_liste.append(nums[i])
            else:
                pos_liste.append(nums[i])
        new_nums=[]
        for i in range(length//2):
            new_nums.append(pos_liste[i])
            new_nums.append(neg_liste[i])
        return new_nums

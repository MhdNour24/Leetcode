class Solution:
    def __init__(self):
        self.top_zero=0
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic={}
        liste=[]
        l=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                top=nums1[i]+nums2[j]
                if top not in liste:
                    liste.append(top)
                    dic[top]=1
                else:
                    dic[top]+=1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                value=nums3[i]+nums4[j]
                if value>0:
                    inverse_value=-abs(value)
                if value<0:
                    inverse_value=abs(value)
                elif value==0:
                    inverse_value=0
                if inverse_value in liste:
                    l.append((value,inverse_value))
                    self.top_zero+=dic[inverse_value]
        return self.top_zero
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        dict={}
        yoğun_liste=[]
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=1
                yoğun_liste.append(nums[i])
            else:
                
                dict[nums[i]]+=1
        
        for j in range(len(yoğun_liste)):
            if dict[yoğun_liste[j]]==1:
                return yoğun_liste[j]

     
                
        
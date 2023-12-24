class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_among=max(candies)
        boolean_list=[]
        for i in candies:
            if i+extraCandies>=max_among:
                boolean_list.append(True)
            else:
                boolean_list.append(False)
        return boolean_list
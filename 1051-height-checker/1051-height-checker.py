class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter=0
        expected =sorted(heights)
        for i in range(len(expected)):
            if heights[i]!=expected[i]:
                counter+=1
        return counter
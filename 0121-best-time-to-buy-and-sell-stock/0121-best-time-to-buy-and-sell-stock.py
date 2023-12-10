class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num=prices[0]
        max_profit=0
        for price in prices[1:]:
            if price-min_num>max_profit:
                max_profit=price-min_num
            if price<min_num:
                min_num=price
        return max_profit
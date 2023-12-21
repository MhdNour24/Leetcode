class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        s=len(prices)
        if s<=1: return 0
        buy=-prices[0]
        sell=0
        for price in prices[1:]:
            buy=max(buy, sell-price)
            sell=max(sell, price-fee+buy)
        return sell
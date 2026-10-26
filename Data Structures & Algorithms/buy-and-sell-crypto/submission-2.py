class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        mincost = prices[0]

        for price in prices:
            maxprofit=max(maxprofit,price-mincost)
            mincost=min(mincost,price)
        return maxprofit
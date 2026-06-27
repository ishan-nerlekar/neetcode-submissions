class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        l,r,profitmax=0,1,0
        while(r<len(prices)):
            if(prices[r]>prices[l]):
                profitmax=max(profitmax,prices[r]-prices[l])
                r+=1
            else:
                l=r
                r=l+1
        return profitmax
        
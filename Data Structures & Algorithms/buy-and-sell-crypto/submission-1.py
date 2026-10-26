class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1:
            return 0
        
        l,r,maxprofit=0,1,0
        while r<n:
            if prices[r]>prices[l]:
                maxprofit=max(maxprofit,prices[r]-prices[l])
                r+=1
            else:
                l=r
                r=l+1
        return maxprofit

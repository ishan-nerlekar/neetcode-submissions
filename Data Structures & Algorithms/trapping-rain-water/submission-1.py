class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        lmax=[0]*n
        rmax=[0]*n
        trapped = 0

        lmax[0] = heights[0]
        rmax[n-1] = heights[n-1]

        for i in range(1,n):
            lmax[i]=max(heights[i],lmax[i-1])

        for i in range(n-2,-1,-1):
            rmax[i]=max(heights[i],rmax[i+1])
        
        for i in range(n):
            trapped+=min(lmax[i],rmax[i])-heights[i]
        
        return trapped
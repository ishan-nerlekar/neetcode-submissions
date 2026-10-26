class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i,j=0,n-1
        maxarea=0

        while(i<j):
            maxarea=max(maxarea,(j-i)*min(heights[i],heights[j]))
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return maxarea
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return [max(nums)]
        res=[]

        for i in range(len(nums)-k+1):
            window = nums[i:i+k]
            curmax=max(window)
            res.append(curmax)
        return res
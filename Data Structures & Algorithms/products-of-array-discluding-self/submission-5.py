class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeroes=0
        prod=1
        ans = [0]*len(nums)
        for n in nums:
            if n==0:
                numZeroes+=1
            else:
                prod*=n
        if numZeroes>1:
            return ans
        
        for i in range(len(nums)):
            if numZeroes == 0:
                ans[i] = prod//nums[i]
            elif nums[i]==0:
                ans[i] = prod
        
        return ans
 
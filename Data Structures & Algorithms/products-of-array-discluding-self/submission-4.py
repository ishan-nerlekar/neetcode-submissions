class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numZeroes = 0
        for n in nums:
            if n!=0:
                product *= n
            else:
                numZeroes+=1
        
        if numZeroes>1:
            return [0]*len(nums)
        
        res = [0]*len(nums)

        if numZeroes==1:
            for i in range(len(res)):
                if nums[i]==0:
                    res[i] = product         
            return res
        else:
            for i in range(len(res)):
                res[i]=product//nums[i]
            return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zerocount=0
        for n in nums:
            if n!=0:
                prod*=n
            else:
                zerocount+=1

        res=[0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i]!=0:
                if zerocount==0:
                    res[i]=prod//nums[i]
                else:
                    res[i]=0
            else:
                if zerocount>1:
                    res[i]=0
                else:
                    res[i]=prod
        return res
            
            
        
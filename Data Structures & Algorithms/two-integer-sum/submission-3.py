class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pair = {}
        for i in range(len(nums)):
            if nums[i] in num_pair:
                return [num_pair[nums[i]],i]
            else:
                num_pair[target-nums[i]]=i
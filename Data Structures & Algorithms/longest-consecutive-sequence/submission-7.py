class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 1:
            return n
        
        longest = 0
        store = set(nums)
        
        for n in store:
            if n-1 not in store:
                length=1
                while n+length in store:
                    length+=1
                longest=max(longest,length)
        return longest
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        s = set(nums)
        longest = 0

        for n in s:
            if n-1 not in s:
                curlongest=1
                while n+curlongest in s:
                    curlongest+=1
                longest=max(longest,curlongest)
        return longest

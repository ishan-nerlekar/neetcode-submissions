class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,n=0,0,len(s)
        longest=0
        myset = set()

        while r<n:
            while s[r] in myset:
                myset.remove(s[l])
                l+=1

            longest=max(longest,r-l+1)
            myset.add(s[r])
            r+=1
        return longest

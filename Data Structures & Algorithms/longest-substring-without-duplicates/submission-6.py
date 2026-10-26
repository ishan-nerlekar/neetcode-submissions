class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,n=0,0,len(s)
        cnt = set()
        longest = 0

        while(r<n):
            while s[r] in cnt:
                cnt.remove(s[l])
                l+=1
            longest=max(longest,r-l+1)
            cnt.add(s[r])
            r+=1
        return longest

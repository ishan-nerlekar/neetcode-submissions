class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store=set()
        n=len(s)
        if n<2:
            return n
        l,longest=0,1
        for r in range(n):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            store.add(s[r])
            longest=max(longest,r-l+1)
            r+=1
        
        return longest
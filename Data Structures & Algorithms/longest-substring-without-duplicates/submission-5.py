class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        store = set()
        l,res=0,0

        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            res=max(res,r-l+1)
            store.add(s[r])
            r+=1
        return res
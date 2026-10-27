class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,n=0,0,len(s)
        cnt = {}
        longest=0

        while r<n:
            cnt[s[r]]=cnt.get(s[r],0)+1
            while r-l+1 - max(cnt.values(),default=0) > k:
                cnt[s[l]]-=1
                l+=1
            longest=max(longest,r-l+1)
            r+=1
        return longest
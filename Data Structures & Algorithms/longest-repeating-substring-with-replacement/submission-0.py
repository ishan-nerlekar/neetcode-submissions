class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chardict=defaultdict(int)
        l,maxf,res=0,0,0
        for r in range(len(s)):
            chardict[s[r]]+=1
            maxf=max(maxf,chardict[s[r]])

            while(r-l+1)-maxf>k:
                chardict[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
        
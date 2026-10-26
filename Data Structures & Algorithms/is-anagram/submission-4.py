class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        cnt = {}

        for l in s:
            cnt[l] = cnt.get(l,0)+1

        for l in t:
            cnt[l] = cnt.get(l,0)-1

        for n in cnt.values():
            if n!= 0:
                return False
        
        return True
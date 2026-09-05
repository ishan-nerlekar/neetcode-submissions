class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}

        for l in s:
            count[l] = count.get(l,0)+1
        for l in t:
            count[l] = count.get(l,0)-1

        for n in count.values():
            if n!=0:
                return False

        return True
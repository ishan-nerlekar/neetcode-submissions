class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)

        for s in strs:
            cnt[''.join(sorted(s))].append(s)
        
        return list(cnt.values())

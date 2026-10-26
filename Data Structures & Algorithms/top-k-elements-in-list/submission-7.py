class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        arr = []
        res = []
        for n in nums:
            cnt[n]+=1

        buckets = [[] for _ in range(len(nums)+1)]
        for n,count in cnt.items():
            buckets[count].append(n)
        
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)

                if len(res)==k:
                    return res

        return res

        
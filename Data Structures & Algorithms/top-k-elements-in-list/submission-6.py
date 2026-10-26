class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        arr = []
        res = []
        for n in nums:
            cnt[n]+=1

        for n,cnt in cnt.items():
            arr.append([cnt,n])
        arr.sort()

        while(len(res)<k):
            res.append(arr.pop()[1])
        return res
        
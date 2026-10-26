class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cnt = {}
        for i in range(len(numbers)):
            if target-numbers[i] in cnt:
                return [cnt[target-numbers[i]]+1, i+1]
            else:
                cnt[numbers[i]]=i
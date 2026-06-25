class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(numbers)):
            if numbers[i] not in dict:
                dict[target-numbers[i]]=i
            else:
                return [dict[numbers[i]]+1,i+1]
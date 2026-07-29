class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}
        for i, j in enumerate(nums):
            rem = target - j
            if rem in exists:
                return [exists.get(rem), i]
            exists[j] = i
        
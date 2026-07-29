class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        
        for i, num in enumerate(nums):
            left = target - num
            if left in hash_map:
                return [hash_map[left], i]
            hash_map[num] = i

        

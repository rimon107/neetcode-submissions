class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_list = []
        results = []

        for i, j in enumerate(nums):
            new_nums = nums[:]
            new_nums.pop(i)
            results.append(math.prod(new_nums))

        return results

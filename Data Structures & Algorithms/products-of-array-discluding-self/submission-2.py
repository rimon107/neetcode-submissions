class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_list = []
        results = []

        for i, j in enumerate(nums):
            new_nums = nums[:]
            new_nums.pop(i)
            nums_list.append(new_nums)

        for value in nums_list:
            results.append(math.prod(value))

        return results

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        post = 1
        results = [1]

        for i in range(len(nums) - 1):
            results.append(results[i] * nums[i])

        for i in range(len(nums)-1, -1, -1):
            results[i] = post * results[i]
            post = nums[i] * post

        return results

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hold = dict()

        for num in nums:
            if hold.get(num) == num:
                return True
            hold[num] = num
        return False
        
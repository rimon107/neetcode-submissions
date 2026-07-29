class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        all_rem = set()
        small = 0
        big = 0
        for i, j in enumerate(nums):
            small = i
            rem = target - j
            if rem in all_rem:
                continue
            all_rem.add(rem)
            for x in range(len(nums) - (i + 1)):
                index = x + i + 1
                if rem == nums[index]:
                    big = index
                    flag = True
                    break
            if flag == True:
                break
        return [small, big]
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        current = 0

        for i in nums:
            if (i-1) not in nums_set:
                current = 1
                x = i
                while True:
                    x += 1
                    if x in nums_set:
                        current += 1
                    else:
                        break
                longest = max(current, longest)
        
        return longest
        



        
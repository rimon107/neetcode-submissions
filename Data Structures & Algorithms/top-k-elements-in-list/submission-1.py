class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = Counter(nums)

        return [key for key, value in result.most_common(k)]
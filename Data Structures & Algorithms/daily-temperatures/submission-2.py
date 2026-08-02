class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                s_t, s_i = stack.pop()
                result[s_i] = i - s_i
            stack.append([temp, i])

        return result

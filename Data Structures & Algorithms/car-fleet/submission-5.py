class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[-1, -1]] * (max(position)+1)

        for i in range(len(position)):
            pairs[position[i]] = [position[i], speed[i]]

        for i in range(len(pairs)-1, -1, -1):
            pair = pairs[i]
            if pair[0] == -1:
                continue
            p, s = pair[0], pair[1]
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        count = {
            ')': 0,
            '}': 0,
            ']': 0
        }


        for p in s:
            if p in ['(', '{', '[']:
                stack.append(p)
                count[match[p]] += 1 
                print(count)
            else:
                if count[p] > 0:
                    count[p] = count[p] - 1
                    if len(stack) > 0:
                            c = stack.pop()
                            if match[c] != p:
                                return False
                else:
                    return False

        if len(stack) > 0:
            return False
        return True

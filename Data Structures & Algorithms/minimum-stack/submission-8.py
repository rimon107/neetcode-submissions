class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()   

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        min_i = self.stack[0]
        for i in self.stack:
            min_i = min(i, min_i)
        return min_i

        

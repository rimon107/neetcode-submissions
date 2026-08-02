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
        min_i = None
        for i in self.stack:
            if min_i is None:
                min_i = i
            min_i = min(i, min_i)
        return min_i

        

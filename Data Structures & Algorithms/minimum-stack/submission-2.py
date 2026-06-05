class MinStack:

    def __init__(self):
        self.arr = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            curr = self.stack[-1]
        else:
            curr = float('inf')
        self.arr.append(val)
        self.stack.append(min(curr, val))
        


    def pop(self) -> None:
        self.arr = self.arr[:-1]
        self.stack = self.stack[:-1]
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.stack[-1]
class MinStack:

    def __init__(self):
        self.stack_list = []        
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.stack_min.append(val)
        

    def pop(self) -> None:
        self.stack_list.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack_list[-1]
    def getMin(self) -> int:
        return self.stack_min[-1]
            
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
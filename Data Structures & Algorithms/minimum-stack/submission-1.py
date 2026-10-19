class MinStack:

    def __init__(self):
        self.stack = []
        self.trace_min = []

    def push(self, val: int) -> None:
        if self.trace_min and val <= self.trace_min[-1]:
            self.trace_min.append(val)
        
        if not self.trace_min:
            self.trace_min.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            remove = self.stack[-1]
            del self.stack[-1]
        
        if remove == self.trace_min[-1]:
            del self.trace_min[-1]          

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.trace_min:
            return self.trace_min[-1]

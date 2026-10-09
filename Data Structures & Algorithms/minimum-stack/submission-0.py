class MinStack:

    def __init__(self):
        self.stack = []
        self.trace = []

    def push(self, val: int) -> None:
        if self.trace:
            self.trace.append(min(val, self.trace[-1]))
        else:
            self.trace.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        del self.trace[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Needs to be O(1)
        return self.trace[-1]

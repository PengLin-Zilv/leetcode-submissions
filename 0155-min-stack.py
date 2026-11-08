class MinStack:

    def __init__(self):
        # operations: push, pop, top, retrieve min element in O(1)
        # we will need 2 stack
        # stack for push, pop, top
        # min_stack will push, pop, but will use for getMin for O(1)
        # how it works is both stack push and pop, top will get stack[-1] and getMin will get min_stack[-1]
        # min_stack will always push (append) the min element to the last position

        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))

    def pop(self) -> None:
        # removes the top element
        del self.stack[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
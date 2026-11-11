class MinStack:
    # task, stack that can push pop top and get min in O(1)
    # logic: use 2 stack, 1 for regular operations: push pop top
    # min_stack for get min element, we will always put the min on the last position

    def __init__(self):
        # initialize stack object
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        # add value to both stack
        # if min stack is empty, add value directly
        # if not, compare the current last element to this value, append min 
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(self.min_stack[-1], value))

    def pop(self) -> None:
        # pop removes the top element
        del self.stack[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        # get the top element
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

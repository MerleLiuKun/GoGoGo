from operator import le
from re import S


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []


    def push(self, x: int) -> None:
        self.in_stack.append(x)


    def pop(self) -> int:
        if not self.out_stack:
            self.in_to_out()
        if self.out_stack:
            return self.out_stack.pop()


    def in_to_out(self) -> None:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def peek(self) -> int:
        if not self.out_stack:
            self.in_to_out()
        if self.out_stack:
            return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


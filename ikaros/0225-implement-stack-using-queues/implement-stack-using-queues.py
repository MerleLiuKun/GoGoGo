# 使用 Queue 实现堆栈


class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
         # 哈哈哈哈 直接 append，pop和top 就会有问题
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.pop(0))


    def pop(self) -> int:
        if self.queue:
            return self.queue.pop(0)

    def top(self) -> int:
        if self.queue:
            return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2, param_3, param_4)

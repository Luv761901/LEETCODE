class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.cnt = 0
        self.sz = k
        self.headIdx = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[(self.headIdx + self.cnt) % self.sz] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.headIdx = (self.headIdx + 1) % self.sz
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.headIdx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.headIdx + self.cnt - 1) % self.sz]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.sz


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

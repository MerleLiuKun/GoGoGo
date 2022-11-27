class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"Node(value={self.value}, next={self.next})"


class LRU:
    def __init__(self, size=5):
        self.head = None
        self.size = size
        self.used = 0
    
    def add(self, number: int):
        n = Node(number)
        # if self.head is None:
        #     self.head = n
        # elif self.used < self.size:
        #     t = self.head
        #     n.next = t
        #     self.head = n
        # else:
        #     self.pop_oldest()
        #     t = self.head
        #     n.next = t
        #     self.head = n

        if self.used >= self.size:
            self.pop_oldest()
        
        t = self.head
        n.next = t
        self.head = n

        self.used += 1

    def pop_oldest(self):
        if self.head is None:
            return
        
        t = self.head
        if t.next is None:
            self.head = None
            return

        while t.next.next is not None:
            t = t.next
        
        t.next = None
        self.used -= 1
    

    def __repr__(self):
        return f"{self.head}"

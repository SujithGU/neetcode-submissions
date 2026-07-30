class MyStack:

    def __init__(self):
        self.head = self.tail = Node()

    def push(self, x: int) -> None:
        node = Node(val=x)
        node.prev_n = self.tail
        node.next_n = None

        self.tail.next_n = node

        self.tail = node

    def pop(self) -> int:
        if self.tail:
            pop_val = self.tail.val
            self.tail = self.tail.prev_n
            self.tail.next_n = None

            return pop_val

    def top(self) -> int:
        if self.tail:
            return self.tail.val

    def empty(self) -> bool:
        if self.head == self.tail:
            return True
        else:
            return False
        
class Node:
    def __init__(self,val=None,prev_n=None,curr_n=None):
        self.val = val
        self.prev_n = prev_n
        self.curr_n = curr_n

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
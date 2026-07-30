class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(url=homepage)

    def visit(self, url: str) -> None:
        visit_node = Node(url=url)
        visit_node.prev_node = self.current
        self.current.next_node = visit_node
        self.current = visit_node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev_node:
                self.current = self.current.prev_node
            else:
                return self.current.url

        return self.current.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next_node:
                self.current = self.current.next_node
            else:
                return self.current.url

        return self.current.url
        
class Node:
    def __init__(self,url=0,prev_node=None,next_node=None):
        self.url = url
        self.prev_node = prev_node
        self.next_node = next_node

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
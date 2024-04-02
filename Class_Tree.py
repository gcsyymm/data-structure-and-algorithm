from queue import Queue


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def pre_order(self):
        print(self.val)
        if self.left:
            self.pre_order(self.left)
        if self.right:
            self.pre_order(self.right)

    def in_order(self):
        if self.left:
            self.in_order(self.left)
        print(self.val)
        if self.right:
            self.in_order(self.right)

    def post_order(self):
        if self.left:
            self.post_order(self.left)
        if self.right:
            self.post_order(self.right)
        print(self.val)

    def bfs(self):
        que = Queue()
        que.put(self)

        while not que.empty():
            cur_node = que.get()
            print(cur_node.val)
            if cur_node.left:
                que.put(cur_node.left)
            if cur_node.right:
                que.put(cur_node.right)

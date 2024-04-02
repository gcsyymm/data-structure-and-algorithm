class BinSearchTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def pre_order(self):
        print(self.val)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.val)
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.val)

    def insert_node(self, val):
        if val <= self.val and self.left:
            self.left.insert_node(val)
        elif val <= self.val:
            self.left = BinSearchTree(val)
        elif val > self.val and self.right:
            self.right.insert_node(val)
        else:
            self.right = BinSearchTree(val)

    def find_value(self, val):
        if val < self.val and self.left:
            return self.left.find_value(val)
        if val > self.val and self.right:
            return self.right.find_value(val)
        return self.val == val

    def clear_in_situ(self):
        self.val = None
        self.left = None
        self.right = None

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.val

    # remove the node with value of val if the node present in the subtree from current node, if the current node is root of a tree, then its parent is None, parent is a recorder in the recursion
    def remove_node(self, val, parent):
        # if the val is not equal to the current node, keep seaching
        # keep seaching its child and assign current node as parent
        if val < self.val and self.left:
            return self.left.remove_node(val, self)
        # if it reach the leaf and did't find the val, then this val is not exist in this tree
        elif val < self.val:
            return False
        elif val > self.val and self.right:
            return self.right.remove_node(val, self)
        elif val > self.val:
            return False

        # if the current node value equal the val
        else:
            # target has no child node
            if not self.left and not self.right and self == parent.left:
                parent.left = None
                self.clear_in_situ()
            elif not self.left and not self.right and self == parent.right:
                parent.right = None
                self.clear_in_situ()

            # target node has only left subtree or only right subtree
            elif self.left and not self.right and self == parent.left:
                parent.left = self.left
                self.clear_in_situ()
            elif self.left and not self.right and self == parent.right:
                parent.right = self.left
                self.clear_in_situ()
            elif not self.left and self.right and self == parent.left:
                parent.left = self.right
                self.clear_in_situ()
            elif not self.left and self.right and self == parent.right:
                parent.right = self.right
                self.clear_in_situ()

            # target node has both left and right subtree
            else:
                self.val = self.right.find_min()
                self.right.remove_node(self.val, self)


mytree = BinSearchTree(50)
treevals = [21, 76, 4, 32, 64, 100, 52]
for treeval in treevals:
    mytree.insert_node(treeval)


mytree.pre_order()
mytree.remove_node(21, None)
mytree.pre_order()

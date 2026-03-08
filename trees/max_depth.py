class tree_node:
    def __init__(self,val):
        self.val=val
        self.lt=None
        self.rt=None
def maxdepth(tree):
    if tree==None:
        return 0
    left=maxdepth(tree.lt)
    right=maxdepth(tree.rt)
    return 1+max(left,right)
tree=tree_node(3)
tree.lt=tree_node(5)
tree.rt=tree_node(9)
tree.lt.rt=tree_node(3)
tree.lt.lt=tree_node(3)


print(maxdepth(tree))

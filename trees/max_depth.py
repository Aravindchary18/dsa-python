class find_depth:
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
tree=find_depth(3)
tree.lt=find_depth(5)
tree.rt=find_depth(9)
tree.lt.rt=find_depth(3)
tree.lt.lt=find_depth(3)


print(maxdepth(tree))

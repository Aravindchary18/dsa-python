class tree_node:
    def __init__(self,val):
        self.val=val
        self.lt=None
        self.rt=None
def invert_tree(t):
    if t==None:
        return t
    
    p=t.lt
    lt=t.rt
    rt=p
    invert_tree(t.lt)
    invert_tree(t.rt)
    return t
t=tree_node(2)
t.lt=tree_node(9)
t.rt=tree_node(10)
t.lt.rt=tree_node(2)
t.lt.lt=tree_node(7)
inverted=invert_tree(t)

def printinvert(node):
    if node==None:
        return
    print(node.val,end=" ")
    printinvert(node.lt)
    printinvert(node.rt)
printinvert(inverted)

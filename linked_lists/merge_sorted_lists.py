class node:
    def __init__(self,val):
        self.val=val
        self.next=None
def mgll(l1,l2):
    d=node(0)
    c=d
    while l1 and l2:
        if l1.val < l2.val:
            c.next=l1
            c=c.next
            l1=l1.next
        else:
            c.next=l2
            c=c.next
            l2=l2.next
    if l1:
        c.next=l1
       
    else:
        c.next=l2
        
    return d.next
l1=node(1)
l1.next=node(3)
l1.next.next=node(5)
l2=node(2)
l2.next=node(4)
l2.next.next=node(6)
r=mgll(l1,l2)
while r:
    print(r.val,end=" ")
    r=r.next

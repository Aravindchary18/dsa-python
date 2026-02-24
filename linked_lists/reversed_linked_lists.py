class node:
    def __init__(self,val):
        self.val=val
        self.nxt=None
def reversed_lnkd_list(head):
    curr=head
    prev=None
    while curr:
        nxtcurr=curr.nxt
        curr.nxt=prev
        prev=curr
        curr=nxtcurr
    return prev
head=node(1)
head.nxt=node(2)
head.nxt.nxt=node(3)

result=reversed_lnkd_list(head)
curr=result
while curr:
    print(curr.val,end="-->")
    curr=curr.nxt

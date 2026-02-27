class nod:
    def __init__(self,val):
        self.val=val
        self.next=None
def dc(no):
    slow=no
    fast=no
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False
no=nod(1)
no2=nod(2)
no3=nod(3)
no4=nod(4)
no.next=no2
no2.next=no3
no3.next=no4
no4.next=no2
res=dc(no)
print(res)

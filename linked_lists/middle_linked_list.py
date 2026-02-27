# Middle of Linked List
# Logic : slow moves 1 step, fast moves 2 steps
#         when fast reaches end, slow = middle
# Time  : O(n)
# Space : O(1)
class mid:
    def __init__(self,val):
        self.val=val
        self.next=None
def mll(head):
    s=head
    f=head
    while f and f.next:
        s=s.next
        f=f.next.next
    return s
head=mid(1)
head.next=mid(2)
head.next.next=mid(3)
head.next.next.next=mid(4)
head.next.next.next.next=mid(5)
result=mll(head)
print(result.val)

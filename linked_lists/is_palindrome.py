class nod:
    def __init__(s,v):
        s.v=v
        s.nxt=None
def ispalindrome(h):
    dum=h
    curr=dum
    s=f=h
    while f and f.nxt:
        s=s.nxt
        f=f.nxt.nxt
    prev=None
    curr=s
    while curr:
        next=curr.nxt
        curr.nxt=prev
        prev=curr
        curr=next
    lt=h
    rt=prev
    while rt:
        if lt.v!=rt.v:
            return False
        rt=rt.nxt
        lt=lt.nxt
    return True
h=nod(1)
h.nxt=nod(2)
h.nxt.nxt=nod(3)
h.nxt.nxt.nxt=nod(2)
h.nxt.nxt.nxt.nxt=nod(1)

res=ispalindrome(h)
print(res)

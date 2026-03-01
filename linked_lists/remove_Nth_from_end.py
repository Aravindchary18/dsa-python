class nod:
    def __init__(sef,val):
        sef.val=val
        sef.nxt=None
def Nth_node(hd,n):
    d=nod(0)
    d.nxt=hd
    sl=d
    fst=d
    for o in range(n+1):
        fst=fst.nxt
    while fst:
        fst=fst.nxt
        sl=sl.nxt
    sl.nxt=sl.nxt.nxt
    return d.nxt
hd=nod(1)
hd.nxt=nod(2)
hd.nxt.nxt=nod(3)
hd.nxt.nxt.nxt=nod(4)
r=Nth_node(hd,2)
while r:
    print(r.val,end=" ")
    r=r.nxt

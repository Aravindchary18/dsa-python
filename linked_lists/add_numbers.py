class nod:
    def __init__(s,v):
        s.v=v
        s.nxt=None
def sum(l1,l2):
    dum=nod(0)
    curr=dum
    c=0

    while l1 or l2 or c:
        v1=l1.v if l1 else 0
        v2=l2.v if l2 else 0
        tot=v1+v2+c
        c=tot//10
        dig=tot%10
        curr.nxt=nod(dig)
        curr=curr.nxt
        if l1:
            l1=l1.nxt
        if l2:
            l2=l2.nxt
    return dum.nxt
l1=nod(5)
l1.nxt=nod(7)
l1.nxt.nxt=nod(2)
l2=nod(5)
l2.nxt=nod(7)
l2.nxt.nxt=nod(4)
lst=[]
re=sum(l1,l2)
while re:
    lst.append(str(re.v))

    re=re.nxt
    num= " ".join(lst[::-1])
print(num)

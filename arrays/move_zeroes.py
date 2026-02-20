def movingzeros(lst):
    l=len(lst)
    non=0
    for v in range(l):
        if lst[v]!=0:
            lst[non]=lst[v]
            non+=1
    for v in range(non,l):
        lst[v]=0
    return lst
print("after moving zeros to the end : " , movingzeros([2,3,0,3,0]))

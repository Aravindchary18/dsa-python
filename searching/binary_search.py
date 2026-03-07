def bs(n,t):
    left=0
    right=len(n)-1
    while left<=right:
        mid=(left+right)//2
        if n[mid]==t:
            return mid
        elif n[mid]<t:
            left=mid+1
        else:
            right=mid-1
    return -1
print(bs([-1,0,1,2,3,4],4))

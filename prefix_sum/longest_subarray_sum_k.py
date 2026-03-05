def lon_sub(nums,v):
    pre={0:-1}
    c=0
    max_len=0
    for i,n in enumerate(nums):
        c+=n
        if c-v in pre:
            l=i-pre[c-v]
            max_len=max(max_len,l)
        if c not in pre:
            pre[c]=i
    return  max_len
print(lon_sub([1,-1,5,-2,3],3))




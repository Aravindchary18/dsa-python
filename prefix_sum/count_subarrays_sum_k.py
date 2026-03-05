def cal_sub(nums,v):
    count=0
    pre={0:1}
    c=0
    for n in nums:
        c+=n
        if c-v in pre:
            count+=pre[c-v]
        pre[c]=pre.get(c,0)+1
    return count
print(cal_sub([1,2,3],3))
        

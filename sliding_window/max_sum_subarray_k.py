def max_sub(nums,v):
    window_sum=0
    max_sum=0
  
    for i in range(len(nums)):
        window_sum+=nums[i]
        if i>=v-1:
            max_sum=max(max_sum,window_sum)
            window_sum-=nums[i-v+1]
    return max_sum
print(max_sub([2,1,5,1,3,2],3))

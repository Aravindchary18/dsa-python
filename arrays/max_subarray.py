def maxsubarray(nums):
    currentsum=nums[0]
    maxsum=nums[0]
    for num in nums[1:]:
        currentsum=max(num,currentsum+num)
        maxsum=max(maxsum,currentsum)
    return maxsum
result=maxsubarray([1,2,3,4])
print(result)



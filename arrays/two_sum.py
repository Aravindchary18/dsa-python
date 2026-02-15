
# Two sum - bruteforce approach
# Time complexity : 0(n^2)
def two_sum_bruteforce(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
             return[i,j]
        

# Two sum - optimization approach
# Time complexity - 0(n)
def two_sum_optimization(nums,target):
    seen={}
    for i in range(len(nums)):
        needed=target-nums[i]
        if needed in seen:
            return [seen[needed],i]
        seen[nums[i]]=i
    return[]

print ("brute force:",two_sum_bruteforce([3,5,4,1],7))
print("optimization:",two_sum_optimization([45,6,6,4],10))

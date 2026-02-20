def majority_element(nums):
    candidate=None
    count=0
    for n in nums:
        if count==0:
            candidate=n
        
        elif candidate==n:
            count+=1
        else:
            count-=1

    if nums.count(candidate)>len(nums)//2:
        return candidate
    else :
        return "no majority elements"
print("majority element is:",majority_element([2,4,5,2,7,2,2]))

def removing_duplicates(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num) 
    return False

result=removing_duplicates([1,2,3,9,89,4])
print("result is:",result)




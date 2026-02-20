def mergesortedarrays(arr1,brr2):
    a=0
    b=0
    result=[]
    while a<len(arr1) and b<len(brr2):
        if arr1[a]<brr2[b]:
            result.append(arr1[a])
            a+=1
        else:
            result.append(brr2[b])
            b+=1
    while a<len(arr1):
        result.append(arr1[a])
        a+=1
    while b<len(brr2):
        result.append(brr2[b])
        b+=1
    return result
print("mergesorted array is:",mergesortedarrays([1,2,3],[4,5,6]))

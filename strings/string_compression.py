def sc(s):
    compression=[]
    count=1
    for ch in range(1,len(s)):
        if s[ch]==s[ch-1]:
            count+=1
        else:
            compression.append(s[count-1]+str(count))
            count=1
        
        
    compression.append(s[-1]+str(count))

    result="".join(compression)
    return result if len(compression)<len(s) else s
print(sc("aabbbcc"))

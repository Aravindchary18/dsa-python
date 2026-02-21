def longest_substring(s):
    lst=set()
    left=0
    max_len=0
    for r in range(len(s)):
        while s[r] in lst:
            lst.remove(s[left])
            left+=1
        lst.add(s[r])
        max_len=max(max_len,r-left+1)
    return max_len
print("longest substring without duplicates is:",longest_substring("abcabcbb"))

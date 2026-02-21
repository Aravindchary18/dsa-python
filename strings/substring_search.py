def substring_search(string,sub):
     if len(sub)>len(string):
         return false 
     for i in range(string-sub+1):
         if string[i:i+sub]==sub:
             return true
     return false
print(substring_search("abcdef","def"))
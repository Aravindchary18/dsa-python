def substring_search(string,sub):
     if len(sub)>len(string):
         return False 
     for i in range(len(string)-len(sub)+1):
         if string[i:i+len(sub)]==sub:
             return True
     return False
print(substring_search("abcdef","def"))

def mostwater(walls):
    left=0
    right=len(walls)-1
    maxarea=0
    while left <right:
        height=min(walls[left],walls[right])
        width=right-left
        area=width*height
        maxarea=max(maxarea,area)
        if walls[left]<walls[right]:
            left+=1
        else:
            right-=1
    return maxarea
print("container with most water is: ", mostwater([1,8,6,2,5,4,8,3,7]))

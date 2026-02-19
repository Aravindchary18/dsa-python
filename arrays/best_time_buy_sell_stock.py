def maxprofit(prices):
    minprice=prices[0]
    maxprofit=0
    for price in prices:
        if price<minprice:
            minprice=price
        else:
            profit=price-minprice
            maxprofit=max(maxprofit,profit)
    return maxprofit
result=maxprofit([7,1,5,3,6,4])
print("maxprofit is:",result)

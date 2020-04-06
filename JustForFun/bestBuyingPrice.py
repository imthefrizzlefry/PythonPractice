def findMaxGain(arr):
    '''Given an array of stock prices, return the maximum gain that could be made'''
    maxGain=0
    if arr:
        lowestBuy = arr[0]
        for cur in range(1,len(arr)):
            curGain = arr[cur]-lowestBuy
            if arr[cur] < lowestBuy:
                lowestBuy = arr[cur]
            
            if curGain > maxGain:
                maxGain = curGain           
            
    return maxGain

def maxProfit(prices) -> int:
    maxGain=0
    
    if prices:
        lowestBuy = prices[0]

        for cur in range(1,len(prices)):
            curGain = prices[cur]-lowestBuy
            if prices[cur] < lowestBuy:
                lowestBuy = prices[cur]

            if len(prices) > cur+1:
                if prices[cur] > prices[cur+1]:
                    maxGain += curGain if curGain >= 0 else 0
                    lowestBuy = prices[cur+1]
            elif curGain > 0:
                maxGain += curGain

    return maxGain 


if __name__ == "__main__":
    array = [7,1,5,3,6,4]
    print(findMaxGain(array))

    print(maxProfit(array))

    array = [1,2,3,4,5]
    print(maxProfit(array))

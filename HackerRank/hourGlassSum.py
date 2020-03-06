def hourglassSum(arr):
    maxSum = -64

    for x in range(4):
        for y in range(4):
            cursum = arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
            
            maxSum = cursum if cursum > maxSum else maxSum
    
    return maxSum
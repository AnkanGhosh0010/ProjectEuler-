def inputArray():
    n = int(input())
    arr = list(map(int,input().split()))
    return arr
    
def maxSubArray(arr):
    max_sum = float("-inf")
    curr_sum = 0
    for i in range (len(arr)):
        curr_sum += arr[i]
        max_sum = max(max_sum,curr_sum)

        if curr_sum<0:
            curr_sum = 0
    return max_sum

result = maxSubArray(inputArray())
print(result)


    

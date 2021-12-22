def max_sequence(arr):
    highestTotalSoFar = 0

    for left_most_digit in range(len(arr)):
        for total_to_sum in range(len(arr) - left_most_digit):
            currentSum = 0
            for idx in range(total_to_sum + 1):
                currentSum += arr[left_most_digit + idx]
            
            highestTotalSoFar = max(highestTotalSoFar, currentSum)

    return highestTotalSoFar

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 100])

#Not complete
def max_sequence(arr):
    if len(arr) == 0:
        return 0
    negative_numbers = 0    
    
    for num in arr:
        if num < 0:
            negative_numbers += 1 
    
    if negative_numbers == len(arr):
        return 0
    
    max_so_far = arr[0]
    current_max = arr[0]
    
    for i in range(1,len(arr)):
        current_max = max(current_max, current_max + arr[i])
        max_so_far = max(max_so_far, current_max )
        return max_so_far
    
    
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

a = [1,2,3,4]    

4 + -1 + 2 + 1 + -5 + 100
    
#Top rated on Code Wars   
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max









max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])




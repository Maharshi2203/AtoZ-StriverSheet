def findsecondLargest(arr):
        largest = arr[0] 
        second = -9999999999     
        for num in arr:
            if num > largest:
                second = largest 
                largest = num
            elif num > second and num != largest:
                 second = num
        return second

nums = [3,3,6,1]
print("Largest element:", findsecondLargest(nums)) 

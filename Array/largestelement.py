def findLargest(arr):
        largest = arr[0]      
        for num in arr:
            if num > largest:
                largest = num
        return largest

nums = [3,3,6,1]
print("Largest element:", findLargest(nums)) 

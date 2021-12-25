def binary_search(arr, value):
    low, high = 0, len(arr) -1

    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] > value:
            high = mid - 1

        elif arr[mid] < value:
            low = mid + 1 

        elif arr[mid] == value:
            return mid
        
    return -1
    

def binary_search(arr, value, low, high):
    # low = 0, high = len(arr)-1
    print(arr, value, low, high)
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] > value:
        return binary_search(arr, value, low, mid - 1)
    
    elif arr[mid] < value:
        return binary_search(arr, value, mid + 1, high)
    
    elif arr[mid] == value:
        return mid
    

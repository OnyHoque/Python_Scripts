arr = [10, 3, 9, 5, 20, 11, 5, 15, 1, -5, -3, 0, 12, 15, -10, 3, 6, -15]

def cocktailSort(arr):
    flag = True
    start = 0
    end = len(arr)-1
    while flag:
        flag = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
        
        if not flag:
            break
    
        flag = False

        end = end - 1

        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True

        start = start + 1
    return arr

# arr = cocktailSort(arr)
# print("Final arr:",arr)
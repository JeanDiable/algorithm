def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findsmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

print(selectionsort([4,7,2,9,25,3,8,9,0]))
        
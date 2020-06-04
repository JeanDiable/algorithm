def summ(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + summ(arr[1:])
print(summ([1,2,3,4,5]))

def count_num(arr):
    if len(arr) == 0:
        return 0
    return 1+count_num(arr[1:])
print(count_num([1,4,5,6]))

def find_max(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        elif arr[1] > arr[0]:
            return arr[1]
        else:
            return arr[0]
    else:
        arr = [find_max(arr[0:2])]+arr[2:]
        find_max(arr)
print(find_max([1,4,7,3,8,8,9]))
    
#answer
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0]>sub_max else sub_max

print(max([1,4,5,7,8,8,8,5,67,5,66]))

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([2,5,3,7,23,54,245,3564,788]))

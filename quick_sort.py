example = [1,2,6,4,7,9,5]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    less, middle, greater = [],[], []
    for i in arr:
        if i < pivot:
            less.append(i)
        if i == pivot:
            middle.append(i)
        if i > pivot:
            greater.append(i)
    return quick_sort(less) + middle + quick_sort(greater)
print(quick_sort(example))
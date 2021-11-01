a = [7,3,5,2,6,4,1]
n = len(a)
def quick_sort(a, start, end):
    if start < end:
        pivotPosition = partition(a, start, end)
        quick_sort(a, start, pivotPosition - 1)
        quick_sort(a, pivotPosition + 1, end)
    return a

def partition(a, start, end):
    left = start - 1
    pivot = a[end]
    for i in range(start, end + 1):
        if a[i] <= pivot:
            left = left + 1
            a[i], a[left] = a[left], a[i]
            if i == end:
                pivotPosition = end
    
    return pivotPosition

print(quick_sort(a, 0, n - 1))

    

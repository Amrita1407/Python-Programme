a = [7,3,5,2,6,4,1,9,12]
n = len(a)
count = 0

def merge(start, mid, end):
    global count
    i = start
    j = mid + 1
    c = []
    print("Trying to merge " + str(a[start:mid + 1]) + " and " + str(a[mid + 1:end + 1]))
    while (i <= mid and j <= end):
        if (a[i] < a[j]):
            c.append(a[i])
            i = i + 1
        else:
            c.append(a[j])
            count += (mid - i + 1)
            j = j + 1
    while (i <= mid):
        c.append(a[i])
        i = i + 1
    while (j <= end):
        c.append(a[j])
        j = j + 1
    for index in range(len(c)):
        a[start + index] = c[index]
    print("After merging " + str(a[start:end + 1]))
def mergeSort(start, end):
    if (start < end):
        print("Trying to sort subarray " + str(a[start:end + 1]))
        mid = (start + end)//2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)
        merge(start, mid, end)
print("Before sorting " + str(a))
mergeSort(0, n - 1)
print("After sorting " + str(a))
print("No of inversions = " + str(count))
# count = 0

# def count_inversion(a, start, end):
#     if start < end:
#         mid  = (start + end) // 2
#         count_inversion(a, start, mid)
#         count_inversion(a, mid + 1, end)
#         merge(a, start, mid, end)

# def merge(a, start, mid, end):
#     global count
#     i = start
#     j = mid + 1
#     c = []
#     while (i <= mid and j <= end):
#         if a[i] <= a[j]:
#             c.append(i)
#             i = i + 1
#         else:
#             count = count + (mid - i + 1)
#             c.append(a[j])
#             j = j + 1

#     while (i <= mid):
#         count = count + 1
#         c.append(a[i])
#         i = i + 1

#     while (j <= end):
#         c.append(a[j])
#         j = j + 1

#     for i in range(len(c)):
#         a[start + i] = c[i]

#     return a

                
# count_inversion(a, 0, n - 1)
# print(count)


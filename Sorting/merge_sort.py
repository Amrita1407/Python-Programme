def merge_sort(a, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid + 1, end)
        merge(a, start, mid, end)
    return a


def merge(a, start, mid, end):
    i = start
    j = mid + 1
    c = []
    while (i <= mid and j <= end):
        if a[i] <= a[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(a[j])
            j = j + 1

    while (i <= mid):
        c.append(a[i])
        i = i + 1

    while (j <= end):
        c.append(a[j])
        j = j + 1

    for i in range(len(c)):
        a[start + i] = c[i]

    return a


a = [7, 6, 1, 3, 4, 9, 2, 7, 5, 3]
print(merge_sort(a, 0, len(a) - 1))

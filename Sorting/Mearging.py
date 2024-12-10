import math


# Time taken O(m+n)
# Merge Two full list
def merge(x: list[int], y: list[int]):
    i, j, k = 0, 0, 0
    res = [0 for _ in range(0, len(x) + len(y))]
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            res[k] = x[i]
            i, k = i + 1, k + 1
        else:
            res[k] = y[j]
            j, k = j + 1, k + 1
    while i < len(x):
        res[k] = x[i]
        i, k = i + 1, k + 1
    while j < len(y):
        res[k] = y[j]
        j, k = j + 1, k + 1
    return res


# Time taken O(m+n)
def merge_single(x: list[int], l: int, mid: int, h: int):
    i, j, k = l, mid + 1, 0
    res = [0 for _ in range(l, h + 1)]
    while i <= mid and j <= h:
        if x[i] < x[j]:
            res[k] = x[i]
            i, k = i + 1, k + 1
        else:
            res[k] = x[j]
            j, k = j + 1, k + 1

    while i <= mid:
        res[k] = x[i]
        i, k = i + 1, k + 1
    while j <= h:
        res[k] = x[j]
        j, k = j + 1, k + 1

    for i in range(l, h + 1):
        x[i] = res[i - l]
    return res


def itrative_merge_sort(x: list[int]):
    i = 2
    h = 0
    while i <= len(x):
        j = 0
        while j + i - 1 < len(x):
            l = j
            h = j + i - 1
            # print(l, h, i)
            mid = math.floor((l + h) / 2)
            merge_single(x, l, mid, h)
            j = j + i
        i = i * 2
    # last merge if there are odd number of items in the mearge sort
    if i / 2 < len(x):
        merge_single(x, 0, int(i / 2) - 1, len(x) - 1)

    return x


def rec_merger_sort(x: list[int], l: int, h: int):
    if l < h:
        mid = math.floor((l + h) / 2)
        rec_merger_sort(x, l, mid)
        rec_merger_sort(x, mid + 1, h)
        merge_single(x, l, mid, h)


if __name__ == "__main__":
    x = [10, 20, 60, 80, 15, 25, 90, 100, 19]
    rec_merger_sort(x, 0, len(x) - 1)
    print(x)

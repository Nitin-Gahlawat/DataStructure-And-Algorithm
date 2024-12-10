import sys


def partioning(array: list[int], low: int, high: int):
    pvt = array[low]
    i = low + 1
    j = high

    while i <= j:
        while i <= high and array[i] <= pvt:
            i += 1

        while j >= low and array[j] > pvt:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
    print(low, high, j, i)
    array[low], array[j] = array[j], array[low]

    return j


def quick_sort(array: list[int], low: int, high: int):
    if low < high:
        j = partioning(array, low, high)
        quick_sort(array, low, j)
        quick_sort(array, j + 1, high) 


if __name__ == "__main__":
    x = [10, 70, 90, 40, 80, 50, 20, 30]
    quick_sort(x, 0, len(x) - 1)
    print(x)

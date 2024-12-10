# It is Adaptive
# It is Stable
# Time complexit o(n^2)
import copy


def Insertion_sort(given_list: list[int]) -> list[int]:
    arr = copy.deepcopy(given_list)  # creating a deepcopy
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j > -1 and arr[j] > x:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = x
    return arr


if __name__ == "__main__":
    x = [23, 29, 15, 19, 31, 7, 9, 5, 2]
    print(Insertion_sort(x))

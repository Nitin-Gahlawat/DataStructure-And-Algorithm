import copy


def selection_sort(given_list: list[int]) -> list[int]:
    arr = copy.deepcopy(given_list)  # creating a deepcopy
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(selection_sort(x))

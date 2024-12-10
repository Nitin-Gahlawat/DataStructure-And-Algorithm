import copy


# Time complexty O(n^2)
# It is Adaptive (beacuse of swapped variable)
# Number of swaps O(n^2) [n(n-1)/2]
def Bubble_sort(given_list: list[int]) -> list[int]:
    arr = copy.deepcopy(given_list)  # creating a deepcopy
    for i in range(0, len(arr) - 1):
        swapped: bool = False
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            print("not swaped")
            break
    return arr


if __name__ == "__main__":
    x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(Bubble_sort(x))

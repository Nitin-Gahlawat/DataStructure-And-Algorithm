def shellsort(x: list[int]):
    gap = len(x) // 2
    while gap > 0:
        j = gap
        while j < len(x):
            i = j - gap
            while i >= 0:
                if x[i + gap] < x[i]:
                    x[i], x[j] = x[j], x[i]
                i = i - gap

            j = j + 1

        gap = gap // 2


if __name__ == "__main__":
    x = [23, 29, 15, 19, 31, 7, 9, 5, 2]
    shellsort(x)
    print(x)

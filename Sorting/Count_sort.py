def count_sort(x: list[int]):
    max_ele = max(x)
    res = [0 for _ in range(0, max_ele + 1)]
    for i in x:
        res[i] += 1

    k = 0
    for i in range(0, len(res)):
        if res[i] != 0:
            while res[i] != 0:
                x[k] = i
                k = k + 1
                res[i] -= 1
    return x


if __name__ == "__main__":
    print(count_sort([1, 2, 6, 8, 9, 10, 5, 7, 6, 6]))

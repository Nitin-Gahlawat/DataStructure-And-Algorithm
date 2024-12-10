class bin:
    def __init__(self, ele, link=None):
        self.element = ele
        self.link = link


def create_array(res: list[bin], x):
    k = 0
    for i in range(0, len(res)):
        if res[i] != None:
            temp = res[i]
            while temp != None:
                x[k] = temp.element
                k = k + 1
                temp = temp.link
    return x


def create_bins(base: int, x: list[int], dig):
    res: list[bin] = [None for _ in range(0, base)]
    d = lambda a: ((a) % (10**dig)) // (10 ** (dig - 1))
    for i in x:
        if res[d(i)] == None:
            res[d(i)] = bin(i, None)
        else:
            temp = res[d(i)]
            while temp.link != None:
                temp = temp.link
            temp.link = bin(i, None)
    return res


# Time complexity O(n)
def radix_sort(x: list[int], base: int):
    # clalulating the length of the maximum elemnt in the list
    max_len = len(str(abs(max(x))))

    for i in range(1, max_len + 1):
        res = create_bins(base, x, i)
        x = create_array(res, x)
    return x


if __name__ == "__main__":
    print(radix_sort([18, 27, 66, 89, 15, 2000, 25, 90, 100, 19, 10], 10))

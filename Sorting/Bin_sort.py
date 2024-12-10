class bin:
    def __init__(self, ele, link=None):
        self.element = ele
        self.link = link


# Time complexity O(n)
def bin_sort(x: list[int]):
    max_ele = max(x)
    res: list[bin] = [None for _ in range(0, max_ele + 1)]
    for i in x:
        if res[i] == None:
            res[i] = bin(i, None)
        else:
            temp = res[i]
            while temp.link != None:
                temp = temp.link
            temp.link = bin(i, None)

    k = 0
    for i in range(0, len(res)):
        if res[i] != None:
            temp = res[i]
            while temp != None:
                x[k] = temp.element
                k = k + 1
                temp = temp.link
    return x


if __name__ == "__main__":
    print(bin_sort([10, 20, 60, 80, 15, 25, 90, 100, 19, 10, 10, 10]))

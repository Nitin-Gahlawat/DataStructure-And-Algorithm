def insert_maxheap(heap: list[int], n: int):
    i = n
    temp = heap[n]
    while i > 1 and temp > heap[i // 2]:
        heap[i] = heap[i // 2]
        i = i // 2
    heap[i] = temp
    return heap


def delete_maxheap(heap: list[int], n: int):  # n is the element index
    val = heap[1]
    heap[1] = heap[n]
    i = 1
    j = 2 * i

    while j < n - 1:
        if heap[j] < heap[j + 1]:
            j = j + 1
        if heap[i] < heap[j]:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j = 2 * j
        else:
            break

    heap[n] = val
    return val


def heapsort(array: list[int], n: int):
    for i in range(n, 1, -1):
        delete_maxheap(array, i)


def create_heap_max(array: list[int]):
    for i in range(1, len(array)):
        insert_maxheap(array, i)


def insert_minheap(heap: list[int], n: int):
    i = n
    temp = heap[n]
    while i > 1 and temp < heap[i // 2]:
        heap[i] = heap[i // 2]
        i = i // 2
    heap[i] = temp
    return heap


def delete_minheap(heap: list[int], n: int):  # n is the element index
    val = heap[1]
    heap[1] = heap[n]
    i = 1
    j = 2 * i

    while j < n - 1:
        if heap[j] > heap[j + 1]:
            j = j + 1
        if heap[i] > heap[j]:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j = 2 * j
        else:
            break

    heap[n] = val
    return val


def heapsort_minele(array: list[int], n: int):
    for i in range(n, 1, -1):
        delete_minheap(array, i)


def create_heap_min(array: list[int]):
    for i in range(1, len(array)):
        insert_minheap(array, i)


if __name__ == "__main__":
    # creating a min heap
    ele = [0, 70, 5, 100, 150, 500, 35, 50]
    create_heap_min(ele)
    print(ele)
    heapsort(ele, 7)
    print(ele)

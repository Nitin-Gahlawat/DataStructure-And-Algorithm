class Queue:
    # Time Complexity O(1)
    def __init__(self, Numberele) -> None:
        self.queue_size = Numberele
        self.rear = self.front = -1
        self.queue = [0] * self.queue_size

    # Time Complexity O(1)
    def isFull(self) -> bool:
        if self.rear + 1 == self.queue_size:
            return True
        return False

    # Time Complexity O(1)
    def isEmpty(self) -> bool:
        if self.rear == self.front:
            return True
        return False

    # Time Complexity O(n)
    def __str__(self) -> str:
        if self.isEmpty():
            return "[]"

        res_queue = "["
        # Starting from the next term of the first and up to rear
        for i in range(self.front + 1, self.rear + 1):
            res_queue += f"{str(self.queue[i])},"
        return res_queue[0 : len(res_queue) - 1] + "]"

    # Time Complexity O(1)
    def queue_size(self) -> int:
        return self.queue_size

    # Time Complexity O(1)
    def font_loc(self) -> int:
        return self.front

    # Time Complexity O(1)
    def rear_loc(self) -> int:
        return self.rear

    # Time Complexity O(1)
    # return number of elements in the array
    def __len__(self) -> int:
        return self.rear - self.front

    # Time Complexity O(1)
    def enqueue(self, ele: int) -> None:
        if self.isFull():
            raise Exception("The queue is full")
        self.rear = self.rear + 1
        self.queue[self.rear] = ele

    # Time Complexity O(1)
    def dequeue(self) -> int:
        if self.isEmpty():
            raise Exception("The queue is Empty")
        x = self.queue[self.front + 1]
        self.queue[self.front + 1] = 0
        self.front = self.front + 1
        return x

    # Time Complexity O(1)
    def get_Front(self) -> int:
        return self.queue[self.front + 1]

    # Time Complexity O(1)
    def get_rare(self) -> int:
        return self.queue[self.rear]


if __name__ == "__main__":
    text = Queue(5)
    text.enqueue(10)
    text.enqueue(20)
    text.enqueue(30)
    print(text)
    print(text.dequeue())
    print(text)

    print(len(text))
    print(text.get_rare())
